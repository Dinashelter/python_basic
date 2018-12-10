clgo_students_list = ["Dan", "Clark"]

# Append 在列表中添加元素
clgo_students_list.append("Gin")

# Insert 在列表中插入数据
clgo_students_list.insert(2, "lisa")

# Extend 在列表末尾插入数据
added_list = ["Jim", "Kimmy", "Allen"]
clgo_students_list.extend(added_list)

# Remove 移除查询对应值的第一个列表数据
clgo_students_list.remove("Clark")

# Pop 移除该位置的值并返回这个值
popped_student = clgo_students_list.pop(3)

# Del 删除列表的值
del clgo_students_list[3]

# 列表的长度
print(str(len(clgo_students_list)))

# 列表中特定值的个数
print(str(clgo_students_list.count("Dan")))

print(clgo_students_list, popped_student)

# 列表中值的排序
# 升序
clgo_students_list.sort()
print(clgo_students_list, popped_student)

# 降序
clgo_students_list.sort(reverse=True)
print(clgo_students_list, popped_student)

# 列表的反转
clgo_students_list.reverse()
print(clgo_students_list)

# 遍历
for name in clgo_students_list:
    print(name)

SjtuPeople newPeople = new StjuPeople("刘祎骏"， 28)
print(newPeople.name)