def getMaxVal(items, cap=8):
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

items = [ (5,2), (6,3), (3,1), (2,2), (15,4), (3,1) ] # (value, weight)
print(getMaxVal(items))


# Gold (bar/ingot)	1	500–1000	Highly valuable, universal currency.
# Silver (ingot)	1	300–600	Medium-high value, versatile.
# Gold Jewelry	0.5–1	800–1200	Includes gemstones for added value.
# Silver Jewelry	0.5–1	400–800	Intricate designs add to value.
# Gemstone Jewelry	0.2–0.5	1000–2000	higher value than gold and silver due to their rarity, aesthetic appeal, and specialized demand
