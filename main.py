print("Welcome LAB16")
print("This place has been abandoned for years!")
print("Where do you want to go first")


answer = input("The Server or Testing room? ")

if answer == 'server':
    print("You are inside the Server room")
    print("All the servers are scattered around the place")
    print("Everything is ruined")
    print("But there is a switch on the right")
    answer2 = input("Do you want to press the switch? ")

elif answer == 'test':
    print("Your are in the testing")
    print("The room is filled with all sorts of tubes and test subjects")
    print("At the opposite end of the room you can see red light")
    answer3 = input("Do you want to approach the light")

if answer == "server" and answer2 == "yes":
    print("A secret door which was in the floor starts to open")
    print("There are steps leading to a underground room")
    answer4 = input("Do you want to go down? ")

elif answer == "test" and answer3 == "yes":
    print("The switch turned on the power to the room")
    print("The machines in the room are turning on")
    print("All the windows in the room open")
    answer5 = input("do you want to explore the testing room further? ")

if answer2 == "yes" and answer4 == "yes":
    print("The underground room is filled with big pods")
    print("Pods that looks like hibernation pods")
    answer6 = input("do you want to look inside...?")

