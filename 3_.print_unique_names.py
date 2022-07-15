number = int(input())
names_list = set()
for _ in range(number):
    names = input()
    names_list.add(names)
for el in names_list:
    print(el)
