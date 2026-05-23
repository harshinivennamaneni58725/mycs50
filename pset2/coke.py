amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount_due -= coin

# Calculate and display change (absolute value changes negative amount due to positive change)
print(f"Change Owed: {abs(amount_due)}")
