def best_timesell2(prices):
    best_timesell2 = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            best_timesell2 += prices[i] - prices[i - 1]
    return best_timesell2

prices = [7, 1, 5, 3, 6, 4]
print(best_timesell2(prices))

prices = [1, 2, 3, 4, 5]
print(best_timesell2(prices))

prices = [7, 6, 4, 3, 1]
print(best_timesell2(prices))
