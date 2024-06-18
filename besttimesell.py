def best_timesell(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    best_timesell = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        
        current_profit = price - min_price
        if current_profit > best_timesell:
            best_timesell = current_profit
    
    return best_timesell

prices = [7, 1, 5, 3, 6, 4]
print(best_timesell(prices))

prices = [7, 6, 4, 3, 1]
print(best_timesell(prices))
