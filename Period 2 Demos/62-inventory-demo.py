inventory = []

#player solves puzzle
inventory.append("room 1 key")

#player tries to open door
if "room 1 key" in inventory:
    print("Door is open")
    inventory.remove("room 1 key")

else:
    print("Door is locked. Go get the key.")
    
print(inventory)