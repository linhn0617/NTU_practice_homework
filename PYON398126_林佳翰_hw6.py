math = {"柯南","灰原","步美","美環","光彦"}
english = {"柯南","灰原","丸尾","野口","步美"}
ans3 = math.intersection(english)
ans1 = math - ans3
ans2 = english - ans3
ans1_list = list(ans1)
ans2_list = list(ans2)
ans3_list = list(ans3)
ans1_list.sort()
ans2_list.sort()
ans3_list.sort()
print(ans1_list)
print(ans2_list)
print(ans3_list)