def getMaxVal(items, cap=2000):
    n = len(items)
    dp = [[(0, []) for _ in range(cap + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(cap + 1):
            itemValue, itemWeight = items[i - 1]
            if itemWeight <= w:  # Item fits
                without_item = dp[i - 1][w]
                with_item = (dp[i - 1][w - itemWeight][0] + itemValue,
                             dp[i - 1][w - itemWeight][1] + [i])
                dp[i][w] = max(without_item, with_item, key=lambda x: x[0])
            else: 
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][cap]

items = [ (500,10), (300,12), (800,8), (400,6), (500,10), (300, 10), (700,40), (100,15), (200,25), (400,15) ] # (value, weight)
print(getMaxVal(items, 100))


# left is weight, right is value
# Gold (bar/ingot)	10	500	Highly valuable, universal currency.
# Silver (ingot)	12	300	Medium-high value, versatile.
# Gold Jewelry	    8	800	Includes gemstones for added value.
# Silver Jewelry	6	400	Intricate designs add to value.
# Silk	10	500	Lightweight, high demand for luxury and trade.
# Bottles of Pepper, Salt	10	300	Spices highly valued historically; lightweight but consumed quickly.
# Alcohol	40	700	Useful for trade, celebrations, and preservation; moderate value.
# Wheat	15 100	Heavy but essential for sustenance; low per-unit value.
# Water	25	200	Essential for survival but low trade value; widely available.
# Med Kit	15	400	Lightweight and highly 

