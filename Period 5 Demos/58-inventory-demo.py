inventory = []

#player battled and won
inventory.append("room 1 key")

#player tries to go through door
if "room 1 key" in inventory:
    print("Door is open.")
    inventory.remove("room 1 key")
else:
    print("You need a key. Go get it.")

print(inventory)