# Dummy prop firm logic

# pyprop/dumyprop.py
class DumyProp:
    def __init__(self, balance=100000, max_daily_loss=5000, max_overall_loss=10000, leverage=30):
        self.balance = balance
        self.max_daily_loss = max_daily_loss
        self.max_overall_loss = max_overall_loss
        self.leverage = leverage
        self.current_loss = 0  # Track current drawdown
    
    def check_violation(self, trade_loss):
        """Check if a trade violates prop firm rules."""
        self.current_loss += trade_loss
        if self.current_loss > self.max_daily_loss:
            return "Daily loss limit exceeded!"
        elif self.balance - self.current_loss < self.max_overall_loss:
            return "Overall loss limit exceeded!"
        return "Trade allowed"
