ticker_symbols = {
    "GM":"General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "AMZM":"Amazon",
    "GE":"General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 ),
    ( 'EK', 150, '2-mar-1998', 16),
    ( 'GE', 100, '10-sep-2002', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 60 ),
    ( 'EK', 150, '2-mar-1998', 20),
    ( 'GE', 100, '10-feb-2004', 38 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-2004', 52 ),
    ( 'AMZM', 875, '21-jun-2007', 4)
]

purchase_summary = {}

def display_purchases():
    for stock, count, date, price in purchases:
        total = count * price
        print(f"{ticker_symbols[stock]} stock purchased for ${total}")

def generate_purchase_summary():
    for company in ticker_symbols.keys():
        stock_purchases = []
        
        for purchase in purchases:
            if purchase[0] == company:
                stock_purchases.append(purchase)
        
        purchase_summary[company] = stock_purchases

def generate_portfolio():
    overall_total = 0

    for company, sales in purchase_summary.items():
        total = 0
        for stock, count, date, price in sales:
            total += count * price
        
        print(f"{ticker_symbols[company]}: ${total}")
        overall_total += total

    print("")
    print("Portfolion Total")
    print("----------------")
    print(f"Total value of stock in portfolio: ${overall_total}")


generate_purchase_summary()
generate_portfolio()