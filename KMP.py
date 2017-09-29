#for capital letters only in the alphabet
alphabet = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#function to find the capital letters by comparing with list
def short():
    for i in separate:
        if i in alphabet:
            print(i, end="")
    return

#You can input many times
while True:
    sample = input("\nInput Last names only: ")
    last_names = sample.title()
    separate = list(last_names)
    print("Output: ", end="")
    short()
