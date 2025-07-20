Project: Stock Market Dashboard
Name: Pranyga B

Technologies Used:
- Backend: FastAPI, yFinance
- Frontend: HTML, Chart.js, CSS

Features:
- Company list displayed on the left side
- Interactive stock price chart in the center
- Period selector (1 week, 1 month, 3 months)
- Meta information panel showing:
  • Current Price
  • Open / High / Low
  • Market Capitalization

How to Run:
1. Open a terminal and run FastAPI backend:
   uvicorn main:app --reload
2. Open index.html in browser (suggested: use Live Server)

Note:
• Internet connection is required to fetch stock data from yFinance.
• Compatible with modern browsers.
