inventory = []

age = input("How old are you? ")
if int(age) > 16:
    inventory.append("sword")
else:
    inventory.append("nerf gun")

#game happens...
    
if "sword" in inventory:
    print("You beat the monster.")
    inventory.remove("sword")

else:
    print("The monster eats you...")

print(inventory)