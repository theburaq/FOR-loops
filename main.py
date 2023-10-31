for item in 'Zero to Mastery':
  print(item)

for item in [1,2,3,4,5]:
  print(item)

for item in (1,2,3,4,5):
  print(item)
print(item)

#Making a Counter using 'for' loop
#using looping to loop over this iterable list and sum up the total of the list.
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
 counter = counter + item
print(counter)

#instead we do like below then output would be different
counter = 0
for item in my_list:
  counter = counter + item
  print(counter)

#or like this
for item in my_list:
  counter = 0
  counter = counter + item
print(counter)

#using Range
for number in range(0, 10):
  print(number)

for number in range(0, 10):
  print('email email list')

for _ in range(0, 10):
  print('email email list')

for _ in range(0, 10):
  print(_)

#using Range with Step
for _ in range(0, 10, 2):
  print(_)

for _ in range(10, 0, -2):
  print(_)

#converting a range to a list:
my_list = list(range(0, 10))
print(my_list)

for _ in range(2):
  print(list(range(10)))

for _ in range(10, 0, -2):
  print(list(range(10)))

#using Enumerate 
for i, char in enumerate('Helllooo'):
  print(i, char)

for i, char in enumerate(range(100)):
  print(i, char)

for i, char in enumerate(range(100)):
  if char == 50:
    print(f'index of 50 is: {i}')
