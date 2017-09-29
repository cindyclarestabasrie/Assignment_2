winner = {"Odd": "Alice", "Even": "Bob"}

#function to print winner
def stone():
    if sample in even:
        print("Winner: ", winner["Even"])
    elif sample == 0:
        print("No stones")
    else:
        print("Winner: ", winner["Odd"])

sample = int(input("Input number of stones: "))
even =  [value*2 for value in range(1,sample+1)]
stone()
