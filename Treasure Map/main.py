row1 = ["🔲", "🔲", "🔲"]
row2 = ["🔲", "🔲", "🔲"]
row3 = ["🔲", "🔲", "🔲"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

p1 = int(position[0])
p2 = int(position[1])

map[p2-1][p2-1] = "❌"

print(f"{row1}\n{row2}\n{row3}")
