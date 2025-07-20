from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
import yfinance as yf

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the frontend HTML page
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Company symbols
@app.get("/companies")
def get_companies():
    return [
        "TCS.NS", "INFY.NS", "RELIANCE.NS", "WIPRO.NS", "HDFCBANK.NS",
        "ICICIBANK.NS", "HCLTECH.NS", "SBIN.NS", "LT.NS", "BAJFINANCE.NS"
    ]

# Stock price and metadata
@app.get("/stock/{symbol}")
def get_stock_data(symbol: str, period: str = "1mo"):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period)

        try:
            info = ticker.info or {}
        except Exception:
            info = {}

        if data.empty:
            return {"dates": [], "prices": [], "meta": {}}

        return {
            "dates": data.index.strftime("%Y-%m-%d").tolist(),
            "prices": data["Close"].fillna(0).tolist(),
            "meta": {
                "currentPrice": info.get("currentPrice", "N/A"),
                "open": info.get("open", "N/A"),
                "high": info.get("dayHigh", "N/A"),
                "low": info.get("dayLow", "N/A"),
                "marketCap": info.get("marketCap", "N/A"),
            }
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})