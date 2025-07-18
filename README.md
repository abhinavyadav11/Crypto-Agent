#  CryptoAgent — Your Personal AI Crypto Analyst

CryptoAgent is a full-stack GenAI-powered assistant that:
- 🧾 Answers natural language crypto questions (price, market cap, trends)
- 📊 Pulls real-time data from CoinGecko API
- 🧠 Uses LLM (OpenRouter/Ollama) to generate insights
- 🌐 Has a FastAPI backend + Streamlit frontend

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourname/CryptoAgent.git
cd CryptoAgent

# 2. Create virtual env
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run backend
uvicorn main:app --reload

# 5. Run frontend
cd ui
streamlit run app.py
