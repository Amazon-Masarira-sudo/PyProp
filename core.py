# Main PyProp logic

# pyprop/core.py
from .dumyprop import DumyProp

class PyProp:
    def __init__(self):
        self.accounts = {}

    def add_account(self, firm_name, balance=100000):
        """Add a new prop firm account."""
        if firm_name == "DumyProp":
            self.accounts[firm_name] = DumyProp(balance=balance)
        else:
            raise ValueError("Unknown prop firm. Use DumyProp for testing.")

    def check_trade(self, firm_name, trade_loss):
        """Check if a trade violates the firm's rules."""
        if firm_name in self.accounts:
            return self.accounts[firm_name].check_violation(trade_loss)
        else:
            return "Firm not found."

    def list_firms(self):
        """List all active accounts in PyProp."""
        return list(self.accounts.keys())
