location = {"Ball": "1"}
print("A changes cup between 1 and 2",
      "\nB changes cup between 2 and 3",
      "\nC changes between 1 and 3")

sample = input("\nInput order of change: ")
#so input will be capitalized
a = sample.upper()
#listing the order
b = list(a)

#change in A
def change12():
    if location["Ball"] == "1":
        location["Ball"] = "2"
    elif location["Ball"] == "2":
        location["Ball"] = "1"

#change in B
def change23():
    if location["Ball"] == "2":
        location["Ball"] = "3"
    elif location ["Ball"] == "3":
        location["Ball"] = "2"

#change in C
def change13():
    if location["Ball"] == "1":
        location["Ball"] = "3"
    elif location["Ball"] == "3":
        location["Ball"] = "1"

#for each word in list, location of ball might change
for change in b:
    if change == "A":
        change12()
    elif change == "B":
        change23()
    elif change == "C":
        change13()
print("Final location of ball: ", location["Ball"])
