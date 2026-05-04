from collections import *

list = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
counter = Counter(list)

my_dic = {"edad": 44}
my_dic = defaultdict(lambda: "Value not found", my_dic)

city_list = deque(["Londo", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])
city_list.appendleft("Tokyo")