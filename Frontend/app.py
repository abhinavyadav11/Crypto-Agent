import streamlit as st
import requests

st.title("CryptoAgent Test")
query = st.text_input("Ask a crypto question:")

button = st.button("Ask CryptoAgent")

if button:
    if query:
        with st.spinner("Fetching answer..."):
            # Placeholder button to trigger the request
            try:
                response = requests.get("http://127.0.0.1:8000/query", params={"q": query})
                data = response.json()
                answer = data.get("answer", "")
                
                # Basic cleaning example:
                # Replace multiple spaces/newlines with single space
                answer_clean = " ".join(answer.split())
                
                st.markdown(f"**Answer:**  \n{answer_clean}")
            except Exception as e:
                st.error(f"Error: {e}")
