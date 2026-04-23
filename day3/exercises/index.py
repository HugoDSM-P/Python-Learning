word = "computer"
print(word[4])

phrase = "In theory, the theory and the practice are the same. In the practice, they aren't."
print(phrase.index("practice"))

phrase = "In theory, the theory and the practice are the same. In the practice, they aren't."
print(phrase.rindex("practice"))

phrase2 = "Controlling the complexity is the essence of programming"
print(phrase2[0:11])

phrase3 = "Never trust in a computer that you cannot throw out off a window"
print(phrase3[8::3])
print(phrase3[::-1])

list5 = ["Python","is","fun."]
print(" ".join(list5))

phrase4 = "If deployment is hard to explain, maybe is a bad idea."
phrase4 = phrase4.replace("hard", "easy")
print(phrase4.replace("bad", "good"))

print("Repeat" * 15)

transport = ["plane", "car", "ship", "bike"]
transport.append("motorbike")

dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(dict["points"]["points2"][1])

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
my_list = list(my_tuple)
print(my_list)

tuple1 = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(tuple1.count(2))

tuple2 = (1, 2, 3, 4)
a, b, c, d = tuple2

my_set_1 = {1, 2, "three", "four"}
my_set_2 = {"three", 4, 5}
my_set_1.update(my_set_2)
my_set_3 = my_set_1

test = 5 == 5

print(17834/34 > 87*56)

print(25 ** 0.5 == 5)