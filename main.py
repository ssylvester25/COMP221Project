from collections import Counter

import tkinter as tk
from tkinter import ttk

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


# GUI Implementation
def run_knapsack():
    try:
        capacity = int(capacity_var.get())
        new_caps = [int(entry.get()) for entry in cap_entries]
        result = boundedKnapsack(items, new_caps, capacity)
        total_value = result[0]
        itemUsed = result[1]
        itemCounter = Counter(itemUsed)

        result_text = f"The value gained is: {total_value}\n"
        for key in itemCounter:
            result_text += f"{itemNumToName[key]}: {itemCounter[key]} times\n"
        result_label.config(text=result_text)
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

def reset_inputs():
    capacity_var.set("100")
    for i, entry in enumerate(cap_entries):
        entry.delete(0, tk.END)
        entry.insert(0, str(caps[i]))

# Main window setup
root = tk.Tk()
root.title("Bounded Knapsack Solver")

# Capacity Input
tk.Label(root, text="Knapsack Capacity:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
capacity_var = tk.StringVar(value="100")
tk.Entry(root, textvariable=capacity_var, width=10).grid(row=0, column=1, padx=5, pady=5)

# Item Caps Input
tk.Label(root, text="Item Caps:").grid(row=1, column=0, padx=5, pady=5, sticky="ne")
cap_frame = tk.Frame(root)
cap_frame.grid(row=1, column=1, padx=5, pady=5, sticky="w")
cap_entries = []
for i, name in enumerate(itemNumToName.values()):
    tk.Label(cap_frame, text=name).grid(row=i, column=0, sticky="w")
    entry = tk.Entry(cap_frame, width=5)
    entry.insert(0, str(caps[i]))
    entry.grid(row=i, column=1, padx=5, pady=2)
    cap_entries.append(entry)

# Buttons
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Run Knapsack", command=run_knapsack).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Reset", command=reset_inputs).grid(row=0, column=1, padx=5)

# Result Display
result_label = tk.Label(root, text="", justify="left", anchor="w", width=50, wraplength=400, relief="sunken")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

root.mainloop()

