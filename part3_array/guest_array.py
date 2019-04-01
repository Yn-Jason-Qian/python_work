guests = ["Li", "Yang", "West"]
message = "I will invite " + guests[0] + "," +guests[1] + "," + guests[2] + " for dinner."
print(message)
print("But " + guests[0] + " is so busy for coming that i'll invite another friend.")

guests[0] = "Eric"
message = "I will invite " + guests[0] + "," +guests[1] + "," + guests[2] + " for dinner."
print(message)

print("Now i have a bigger table for about six people. So i can invite more persons coming for dinner.")
guests.append("Chen")
guests.insert(0, "Zheng")
guests.insert(2, "Fei")
print(guests)


print("Something happened now, that i can only invite two persons now.")
print("Sorry, I can not invite " + guests.pop() + " now")
print("Sorry, I can not invite " + guests.pop() + " now")
print("Sorry, I can not invite " + guests.pop() + " now")
print("Sorry, I can not invite " + guests.pop() + " now")

print("I will invite " + guests[0])
print("I will invite " + guests[1])
del guests[0]
del guests[0]
print(guests)
