def best_trade(prices):
    if not prices or len(prices) < 2:
        return None  

    min_price = prices[0]
    max_profit = 0
    best_buy = best_sell = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price  
        if price - min_price > max_profit:
            max_profit = price - min_price
            best_buy = min_price
            best_sell = price

    return best_buy, best_sell

prices = [5, 2, 1, 6, 9, 7]
print(best_trade(prices))  
