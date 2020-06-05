# список
import randomize
colors = ["red", "blue", "green", "black", "white"]
numbers = [1, 53, 93, 2, 2, 2, 2, 45, 9]
for i in range(len(colors)):
    print(colors[i])
print(colors[2:5])
print(numbers.count(27))
print(colors)
colors.append("yellow")
print(colors)
colors.pop(1)
print(colors)
while numbers.count(2) != 0:
    numbers.remove(2)
print(numbers)
colors.sort()
numbers.sort()
print(colors)
print(numbers)
lists = [i for i in range(50) if i % 3 == 0]
print(lists)
