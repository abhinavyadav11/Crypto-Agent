import os
import sys
import json
import difflib
import ollama as olm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agent.tools import get_top_crypto, get_crypto_by_name, get_all_cryptos

class CryptoAgentLLM:
    def __init__(self, model: str = 'llama3.2'):
        self.model = model

    def call_llm(self, prompt: str)-> str:
       response = olm.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
       return response['message']['content']
    
    def extract_crypto_from_query(self, query: str):
        query_lower = query.lower()
        all_cryptos = get_all_cryptos()

        for _, name, symbol, price, market_cap in all_cryptos:
            if name.lower() in query_lower or symbol.lower() in query_lower:
                return {
                    "name": name,
                    "symbol": symbol,
                    "price": price,
                    "market_cap": market_cap
                }
        return None

    
    def fuzzy_intent_match(self, query: str)-> str:
        top_keywords = ["top coin", "top coins", "top crypto", "top cryptocurrencies", "top cryptos"]
        price_keywords = ["price of", "btc price", "bitcoin price", "price"]
        query_lower = query.lower()

        for kw in top_keywords:
            if difflib.get_close_matches(kw, [query_lower], cutoff=0.6):
                return "top_crypto"
            
        for kw in price_keywords:
            if kw in query_lower:
                return "price_crypto"
        
        return "other"
    
    def generate_context(self, intent: str, query: str)-> str:
        """
        Generate a textual context from DB based on user intent & query
        """
        coin_info = self.extract_crypto_from_query(query)
        if coin_info:
            return(
                f"{coin_info['name']} ({coin_info['symbol'].upper()}): "
                f"Current Price = ${coin_info['price']}, "
                f"Market Cap = ${coin_info['market_cap']}" 
            )

        intent = self.fuzzy_intent_match(query) #defined

        if intent == 'top_crypto':
            top_coins = get_top_crypto(limit=5)
            context = "Top 5 Cryptocurrencies by Market Cap:\n"
            for i, (cid, name, symbol, price, market_cap) in enumerate(top_coins, 1):
                context += f"{i}. {name} ({symbol.upper()}): Price = ${price}, Market Cap = ${market_cap}\n"
            return context.strip()
        
        elif intent == "price_crypto":
            for word in query.lower().split():
                results = get_crypto_by_name(word)
                if results:
                    _, symbol, name, image, current_price, market_cap, *_ = results[0]
                    return f"{name} ({symbol.upper()}): Current Price = ${current_price}, Market Cap = ${market_cap}"
            return "Sorry, I couldn't find that cryptocurrency."

        else:
            return ""
        
    def answer_query(self, query: str)-> str:
        intent = self.fuzzy_intent_match(query)
        context = self.generate_context(intent, query)

        if context:
            prompt =f"""Use the following data to answer the user's query.
            Data : {context}
            User query : {query}
            Answer based on the above data.
        """
            return self.call_llm(prompt)
        else:
            return self.call_llm(query)
        

if __name__ == "__main__":
    agent = CryptoAgentLLM()  
    print("Ask anything about crypto")
    while True:
        user_query = input("🧠 Your query: ").strip()
        if user_query.lower() in ("exit", "quit"):
            break
        answer = agent.answer_query(user_query)
        print(f"🧾 Answer:\n{answer}\n")



