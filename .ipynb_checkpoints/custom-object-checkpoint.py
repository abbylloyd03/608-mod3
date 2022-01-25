# Abby Lloyd custom-object.py

class Purchase(object):
    def __init__(self, amount):
        """initiate?"""
        self.amount = amount
    
    def calculateTax(self, taxPercent):
        "Given the rate of tax, calculate the tax to add to bill"""
        return self.amount * taxPercent/100.0
    
    def calculateTip(self, tipPercent):
        """Given the rate of tip, calculate the tip to add to bill"""
        return self.amount * tipPercent/100.0
    
    def calculateTotal(self, taxPercent, tipPercent):
        """Given the rate of tax and tip, calculate the total bill"""
        return self.amount * (1 + taxPercent/100.0 = tipPercent/100.0)
    
# Create Purchse object given an amount
purchase = Purchase(100.00)

# Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# Display some useful information
print('Tax:', tax)
print('Tip:', tip)
print('Total:', purchase.calculateTotal(taxPercent, tipPercent)

    
    