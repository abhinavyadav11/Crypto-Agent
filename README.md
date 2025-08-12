# 🤖 CryptoAgent - AI-Powered Cryptocurrency Analysis Platform

A comprehensive cryptocurrency analysis platform that combines real-time data fetching, machine learning recommendations, and intelligent Q&A capabilities using RAG (Retrieval-Augmented Generation) technology.

![CryptoAgent Dashboard]

<img width="1319" height="838" alt="Screenshot 2025-08-12 at 11 23 09 PM" src="https://github.com/user-attachments/assets/2537ebc0-5f7f-40d8-8b96-5048f71b3459" />




## 🌟 Features

### 📊 Real-time Market Data
- Fetches live cryptocurrency data from CoinGecko API
- Stores historical data for technical analysis
- Automatic data pipeline with scheduled updates

### 🤖 AI-Powered Q&A System
- RAG-based question answering using ChromaDB and Ollama
- Intelligent responses about market conditions
- Context-aware cryptocurrency insights

### 📈 Trading Recommendations
- Machine learning models (Decision Tree & Logistic Regression)
- Technical indicators (RSI, MACD, Moving Averages)
- Buy/Hold/Sell recommendations with confidence scores

### 📊 Interactive Visualizations
- Market treemap showing price changes
- Top gainers/losers display
- Technical analysis charts

## 🏗️ Architecture

```
CryptoAgent/
├── frontend/           # Streamlit web application
├── backend/           # FastAPI backend server
├── data_pipeline/     # Data fetching and processing
├── RAG/              # ChromaDB and retrieval system
├── models/           # ML model training notebooks
├── trained_model/    # Saved ML models
├── insights/         # Data visualization components
├── db_storage/       # SQLite database and ChromaDB
└── testing/          # Test scripts and utilities
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Ollama (for AI responses)
- Git

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd CryptoAgent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up Ollama (for AI features)**
```bash
# Install Ollama (visit https://ollama.com)
ollama pull llama3.2
```

4. **Initialize the database**
```bash
cd db_storage
sqlite3 crypto.db < init.sql
```

### 🔄 Data Pipeline Setup

1. **Run the data pipeline**
```bash
cd data_pipeline
python run_pipeline.py
```

2. **Index data to ChromaDB**
```bash
cd scripts
python index_to_chroma.py
```

### 🎯 Train ML Models

1. **Open the training notebook**
```bash
cd models
jupyter notebook train_recommendation_model.ipynb
```

2. **Run all cells to train models**
   - This will create trained models in `trained_model/` directory
   - Models include Decision Tree and Logistic Regression classifiers

### 🌐 Start the Application

#### Option 1: Streamlit Frontend (Recommended)
```bash
cd frontend
streamlit run app.py
```

#### Option 2: FastAPI Backend + Frontend
```bash
# Terminal 1: Start FastAPI backend
cd backend
uvicorn main:app --reload

# Terminal 2: Start Streamlit frontend
cd frontend
streamlit run app.py
```

Visit `http://localhost:8501` for the Streamlit interface.

## 📱 Application Pages

### 🤖 Main - CryptoAgent Q&A
- Ask natural language questions about cryptocurrencies
- Get AI-powered responses using RAG technology
- Example queries:
  - "What is Bitcoin's current price?"
  - "Which crypto gained the most today?"
  - "Compare Ethereum and Solana market caps"

### 📊 Insights - Market Analysis
- Interactive treemap of price changes
- Top gainers and losers
- Market overview statistics
- Real-time data visualization

### 🎯 Recommendations - ML Trading Signals
- Select any cryptocurrency symbol
- Get Buy/Hold/Sell recommendations
- View model confidence scores
- Technical indicator analysis
- Feature importance display

## 🛠️ Technical Components

### Data Pipeline (`data_pipeline/`)
- **`fetch.py`**: Fetches data from CoinGecko API
- **`process.py`**: Cleans and processes market data
- **`run_pipeline.py`**: Orchestrates the entire pipeline

### RAG System (`RAG/`)
- **`chroma_rag.py`**: ChromaDB integration and query handling
- Embeddings generation using Ollama
- Context-aware response generation

### Machine Learning (`models/`)
- **Technical Indicators**: RSI, MACD, Moving Averages
- **Features**: Price changes, volume analysis, momentum indicators
- **Models**: Decision Tree and Logistic Regression
- **Labels**: Buy (>3% gain), Sell (<-3% loss), Hold (otherwise)

### Visualization (`insights/`)
- **`treemap.py`**: Interactive treemap visualization
- **`routes.py`**: FastAPI routes for data endpoints

## 🔧 Configuration

### Environment Variables
Create a `.env` file with:
```env
PINECONE_API_KEY=your_pinecone_key  # Optional: for alternative vector DB
```

### Model Parameters
In training notebook, adjust:
- `FUTURE_HORIZON = 3`: Prediction period (days)
- `BUY_THRESHOLD = 3.0`: Buy signal threshold (%)
- `SELL_THRESHOLD = -3.0`: Sell signal threshold (%)

## 📊 API Endpoints

### FastAPI Backend (`http://localhost:8000`)
- `GET /`: Welcome message
- `GET /query?q=<question>`: Ask crypto questions
- `GET /insights/data`: Get market data for visualizations

## 🔄 Data Flow

1. **Data Collection**: CoinGecko API → Raw JSON files
2. **Processing**: Clean data → CSV files → SQLite database
3. **Indexing**: Processed data → ChromaDB vector store
4. **ML Training**: Historical data → Trained models
5. **Inference**: Live data + Models → Recommendations
6. **Visualization**: Processed data → Interactive charts

## 🧪 Testing

### Test Individual Components
```bash
# Test data pipeline
python data_pipeline/run_pipeline.py

# Test RAG system
python scripts/index_to_chroma.py

# Test Ollama connection
python testing/test_ollama.py

# Test FastAPI
python testing/test_fastAPI.py

# Test Streamlit
python testing/test_streamlit.py
```

## 📈 Model Performance

### Current Model Metrics
- **Decision Tree**: ~97% test accuracy
- **Features Used**: 7 technical indicators
- **No Data Leakage**: Future price changes excluded from features
- **Balanced Classes**: Handles class imbalance with balanced weights

### Feature Importance (Decision Tree)
1. `price_to_ath_ratio`: 20.0%
2. `current_price`: 19.3%
3. `log_price`: 18.1%
4. `ath`: 14.9%
5. `volume_to_market_cap`: 9.0%

## 🚨 Troubleshooting

### Common Issues

1. **"No trained model found"**
   ```bash
   cd models
   jupyter notebook train_recommendation_model.ipynb
   # Run all cells to train models
   ```

2. **"RAG system error"**
   ```bash
   # Ensure Ollama is running
   ollama serve
   ollama pull llama3.2
   ```

3. **"No data available"**
   ```bash
   python data_pipeline/run_pipeline.py
   python scripts/index_to_chroma.py
   ```

4. **"ChromaDB issues"**
   ```bash
   # Clear ChromaDB and rebuild
   rm -rf db_storage/chromadb/
   python scripts/index_to_chroma.py
   ```

## 🔮 Future Enhancements

- [ ] Real-time WebSocket data streaming
- [ ] Advanced deep learning models (LSTM, Transformers)
- [ ] Portfolio optimization algorithms
- [ ] Social sentiment analysis integration
- [ ] Multi-timeframe analysis
- [ ] Risk management metrics
- [ ] Mobile app development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CoinGecko API](https://www.coingecko.com/en/api) for cryptocurrency data
- [Ollama](https://ollama.com) for local LLM inference
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [Streamlit](https://streamlit.io/) for the web interface
- [FastAPI](https://fastapi.tiangolo.com/) for the backend API

## 📞 Support

For questions and support:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the test scripts in `testing/`

---

**⚠️ Disclaimer**: This tool is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. Always do your own research and consider consulting with financial advisors before making investment decisions.
