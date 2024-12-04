from collections import Counter
def boundedKnapsack(items, caps, cap=2000):
    """
    Solves the bounded knapsack problem using the min(cap, j / weight) optimization.
    items: List of tuples (value, weight).
    caps: List of maximum counts for each item.
    cap: Knapsack capacity.
    Returns a tuple of maximum value and the list of items used.
    """
    n = len(items)
    # Initialize DP table with (value, item list)
    dp = [[(0, []) for _ in range(cap + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        itemValue, itemWeight = items[i - 1]
        maxCount = caps[i - 1]
        for w in range(cap + 1):  
            dp[i][w] = dp[i - 1][w]
            max_items = min(maxCount, w // itemWeight)  
            for k in range(1, max_items + 1): 
                with_item = (dp[i - 1][w - k * itemWeight][0] + k * itemValue,
                             dp[i - 1][w - k * itemWeight][1] + [i] * k)
                dp[i][w] = max(dp[i][w], with_item, key=lambda x: x[0])
    return dp[n][cap]

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

# Item	       Value v)	Weight (w)	Ratio (𝑣/𝑤)	Suggested Cap
# Gold Jewelry	800	8	100.0	3
# Silver Jewelry	400	6	66.7	3
# Gold (bar/ingot)	500	10	50.0	2
# Silk	500	10	50.0	2
# Med Kit	400	15	26.7	1
# Bottles of Pepper, Salt	300	10	30.0	1
# Silver (ingot)	300	12	25.0	1
# Water	200	25	8.0	1
# Alcohol	700	40	17.5	1
# Wheat	100	15	6.7	1

### Plug data in
items = [
    (500, 10),  # Gold (bar/ingot)
    (300, 12),  # Silver (ingot)
    (800, 8),   # Gold Jewelry
    (400, 6),   # Silver Jewelry
    (500, 10),  # Silk
    (300, 10),  # Bottles of Pepper, Salt
    (700, 40),  # Alcohol
    (100, 15),  # Wheat
    (200, 25),  # Water
    (400, 15)   # Med Kit
]

itemNumToName = {
    1: "Gold (bar/ingot)",
    2: "Silver (ingot)",
    3: "Gold Jewelry",
    4: "Silver Jewelry",
    5: "Silk",
    6: "Bottles of Pepper, Salt",
    7: "Alcohol",
    8: "Wheat",
    9: "Water",
    10: "Med Kit"
}

caps = [2, 1, 3, 3, 2, 1, 1, 1, 1, 1]

res = boundedKnapsack(items, caps, 100)
print("The value gained is:", res[0])
itemUsed = res[1]
itemCounter = Counter(itemUsed)
for key in itemCounter:
    print(itemNumToName[key], "is used", itemCounter[key], "times")




