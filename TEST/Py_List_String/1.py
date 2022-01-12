my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('print(my_list)')
print(my_list[:])

print('\nprint(my_list[0])')
print(my_list[0])

print('\nprint(my_list[5])')
print(my_list[5])

print('\nprint(my_list[-1])')
print(my_list[-1])

print('\nprint(my_list[0:5])')
print(my_list[0:5])
print('print from list[0] to list[5 - 1]')

print('\nprint(my_list[1:9])')
print(my_list[1:9])
print('print from list[1] to list[9 - 1]')

print('\nprint(my_list[1:-1])')
print(my_list[1:-1])
print('print from list[1] to list[-1 + SIZE - 1]')

print('\nprint(my_list[5:])')
print(my_list[5:])
print('print from list[5] to list[END]')

print('\nprint(my_list[:5])')
print(my_list[:5])
print('print from list[BEGIN] to list[5 - 1]')

print('\nprint(my_list[::-1])')
print(my_list[::-1])
print('print from list[BEGIN] to list[END] with -1 step')

print('\nlist[begin:end:step]\n****************************************\n')

nums = [10, 12, 13, 14, 15, 16, 17, 18, 19]

print('1. append')
for n in nums:
    my_list.append(n)
print(my_list)
for n in nums:
    my_list.append(n * n)
print(my_list)
my_list.clear()
for n in nums:
    if n % 2 == 0:
        my_list.append(n * n)
print(my_list)


print('\n2. map + lambda')
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [n * n * n for n in my_list]
print(list1)
list2 = map(lambda n: n * n * n * n, my_list)
print(*list2)
list3 = filter(lambda n: n % 2 == 0, nums)  # n % 2 == 0 is condition
print(*list3)
list4 = []
for letter in 'abcdefghij':
    for n in my_list:
        list4.append((letter, n))
print(list4)

print('\n3. dictionary & zip')
names = ['Bruce,Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'ISuperman', 'Spiderman', 'Wolverine', 'Deadpool']
list5 = zip(names, heros)
print(*list5)
dict1 = {}
for name, hero in zip(names, heros):
    if(name != 'Logan'):
        # or: dict1 = {name : hero for name, hero in zip(names, heros)}
        dict1[name] = hero
print(dict1)

print('\n4. set')
nums1 = [1, 5, 4, 7, 8, 1, 3, 0, 2, 9, 6, 5, 5, 2, 0, 7, 9, 0, 0, 6]
set1 = set()
for n in nums1:
    set1.add(n)
    # or: set1 = {n for n in nums}
print(set1)

print('\n5. generator')


def gen_func(nums):
    for n in nums:
        yield n * n


gen1 = gen_func(nums)
print(*gen1)

print('****************************************\n')
li = [1, 5, -2, 0, 3, -6, 8, 4, 9, -7]
sort_li = sorted(li)
# or: li.sort() but change li ONLY
print('Sorted: \t', sort_li)
print('Original:\t', li)
li.sort(reverse=True)
print('De Sorted:\t', li)
li = [1, 5, -2, 0, 3, -6, 8, 4, 9, -7]
sort_li2 = sorted(li, key=abs)
print('abs_Sorted:\t', sort_li2)

tup1 = (0, 5, 6, 3, 2, 1, 8, 9, 7, 4)
s_tup1 = sorted(tup1)
print('Tuple:  \t', s_tup1)

dict2 = {'nam ': 'Corey', 'job': 'programming', 'age': None, 'os':  'Mac'}
sort_dict2 = sorted(dict2)
print('Dict:   \t', sort_dict2)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employees = [e1,e2,e3]

def e_sort(em):
    return em.salary

s_employees = sorted(employees, key=e_sort)
print('\n',s_employees)