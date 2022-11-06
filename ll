
if 'yes' in test:
    print("Door is locked you need a key to enter!")

if 'no' in test:
    direction = input("Where do you want to go, North, South, West or East? ")

if 'yes' in server:
    inside = input("You are in the server room, you want to leave or continue ahead? ")



   print("Hello welcome to the LAB16")
action = input("Do you want to Enter? ")

if 'yes' in action:
    direction = input("Where do you want to go, North, South, West or East? ")

if 'north' in direction:
    test = input("You have reached the testing room, do you wish to enter? ")

if 'south' in direction:
    server = input("You have reached the server room, do you wish to enter? ")

if server == 'yes':
    print("You are in the server room, you want to leave or continue ahead? ")
elif server == 'no':
    input(direction)

if 'west' in direction:
    basement = input("You have reached the stairs to the basement, do you want to go down? ")

if 'east' in direction:
    power = input("You have reached the power room, do you wish to enter? ")

if server() == 'yes':
    print("You are in the server room, you want to leave or continue ahead? ")