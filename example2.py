is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")


has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

i = 1
while i<=5:
    print('*' * i)
    i = i + 1
else:
    print("Done")

for item in "Python":
    print(item)

for item in ["Nifal", "Hareb"]:
    print(item)

for item in range(5, 10, 2):
    print(item)


numbers = [5, 2, 5, 2, 2]
for item in numbers:
    star = ''
    for x in range(item):
        star = star + '*'
    print(star)

list = [1, 2, 3, 4, 15, 6, 7, 8, 9]
max = list[0]
for item in list:
    if item >= max:
        max = item
print(max) 