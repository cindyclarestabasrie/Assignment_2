numbers = []
result = []
#function which input will always modulo by 42
def mod(x):
    y = 42
    return x%y

#to limit input to just 10 numbers
while len(numbers) < 10:
    sample = int(input("Input numbers: "))
    numbers.append(sample)
    print(numbers)

#calculates answer
for i in numbers:
    result.append(mod(int(i)))

#counts the distinct results
output = []
for j in set(result):
    output.append(j)
print("\nDistinct results: ", len(output))






