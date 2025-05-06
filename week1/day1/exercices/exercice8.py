sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while len(sandwich_orders) > 0:
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.pop(0)

for sandwich in finished_sandwiches:
    print("I made your", sandwich)