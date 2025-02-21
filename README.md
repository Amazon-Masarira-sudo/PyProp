PyProp is an open-source multi-agent trading assistant designed to help traders manage multiple prop firm accounts seamlessly. It tracks rules, executes trades across firms, monitors dynamic market variables, and optimizes portfolio performance.

🚀 Features
✔ Multi-Agent System – Fundamental, Technical, Risk, and Execution Agents
✔ Rule Tracking – Keeps up with each firm’s max drawdowns, daily limits, and execution policies
✔ Dynamic Monitoring – Tracks spreads, slippage, and order execution across firms
✔ Multi-Account Trade Execution – Places one trade across multiple accounts with minimal slippage
✔ Real-Time Insights – Get instant feedback on market conditions and risk exposure

🛠 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/PyProp.git
cd PyProp
pip install -r requirements.txt
📖 Usage
python
Copy
Edit
from pyprop.multi_agent.fundamental_agent import FundamentalAgent
from pyprop.multi_agent.risk_agent import RiskAgent

# Initialize agents
fund_agent = FundamentalAgent(news_api_url="https://forexnewsapi.com/news")
risk_agent = RiskAgent(firm_api_url="https://dummyprop.com/api/rules")

# Get market news and analyze sentiment
news = fund_agent.get_market_news()
sentiment = fund_agent.analyze_sentiment(news.get("headline", ""))

# Check risk limits
risk_agent.update_rules()
risk_check = risk_agent.check_trade_risk(current_loss=5000)

print("Market Sentiment:", sentiment)
print("Risk Check:", risk_check)
📊 Prop Firm Tracking Commands
Command	Description
prop.compare("FTMO", "MFF")	Compare rules between two firms
prop.plot("FTMO", "spreads")	Plot historical spreads for a firm
prop.describe("MFF")	Get detailed statistics on a firm’s rules
prop.ratings()	See performance & reviews of different prop firms
🌍 Contributing
We’re building the future of prop firm trading. Open to contributions—join the revolution!

Fork the repo
Create a feature branch
Submit a pull request
