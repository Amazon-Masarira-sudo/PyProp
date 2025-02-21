# PyProp

PyProp is an open-source multi-agent trading assistant designed to help traders manage multiple prop firm accounts seamlessly. It tracks rules, executes trades across firms, monitors dynamic market variables, and optimizes portfolio performance.

## 🚀 Features

- **Multi-Agent System**
  - Fundamental Agent: Analyzes market news and sentiment
  - Technical Agent: Processes price action and indicators
  - Risk Agent: Monitors position sizing and exposure
  - Execution Agent: Optimizes trade entry and exit

- **Rule Tracking**
  - Automated monitoring of maximum drawdowns
  - Daily loss limit tracking
  - Real-time execution policy compliance
  - Cross-firm rule synchronization

- **Dynamic Monitoring**
  - Spread analysis across multiple brokers
  - Slippage measurement and optimization
  - Order execution quality metrics
  - Real-time performance analytics

- **Multi-Account Trade Execution**
  - Synchronized trading across accounts
  - Smart order routing for minimal slippage
  - Position sizing optimization
  - Risk-adjusted trade allocation

- **Real-Time Insights**
  - Market condition dashboard
  - Risk exposure metrics
  - Performance attribution
  - Custom alert system

## 🛠 Installation

```bash
git clone https://github.com/yourusername/PyProp.git
cd PyProp
pip install -r requirements.txt
```

## 📖 Usage

```python
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
```

## 📊 Prop Firm Tracking Commands

| Command | Description |
|---------|------------|
| `prop.compare("FTMO", "MFF")` | Compare rules between two firms |
| `prop.plot("FTMO", "spreads")` | Plot historical spreads for a firm |
| `prop.describe("MFF")` | Get detailed statistics on a firm's rules |
| `prop.ratings()` | See performance & reviews of different prop firms |

## 🌍 Contributing

We're building the future of prop firm trading. Open to contributions—join the revolution!

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Documentation](https://pyprop.readthedocs.io/)
- [Issue Tracker](https://github.com/yourusername/PyProp/issues)
- [Change Log](CHANGELOG.md)

## ⚠️ Disclaimer

PyProp is provided as-is without any guarantees. Trading involves risk of loss. Always verify and validate trading decisions independently.
