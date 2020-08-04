"""creating the list """

bicycle = ['trek','cannondale','redline','specialized']

#printing the list

print(bicycle)
print(bicycle[1])
print(bicycle[2].title())
print(bicycle[-1])

#using an individual value from the list

message = f'my firswt bycyle is {bicycle[0]}'
print(message.title())

# try it urself
print("-----try it your self-----")
print('q.3-1')
friends = ['chinamy', ' ronak', 'jay','rutvik']
print(friends)

# q3-2
print("q.3-2")
new_message = f'hello {friends[0]} my friend '
print(new_message)

print('-----------------------------------------------------------------------')
#replacing to the list
bike = ['honda','yamaha','suzuki']
print(bike)
bike[1] = 'ducati'
print(bike)

# adding to the end of list
bike.append('yamaha')
print(bike)

# incerting at the particular position
bike.insert(0,'tvs')
print(bike)

#removing element from the list
print('-------------------------',bike,'-----------------')
del bike[0]
print(bike)

#removing element by pop() method
print('--------------------',bike,'-------------------')
poped_bike = bike.pop(0)
print(bike)
print(poped_bike)

#removing an item by value
print('------',bike,"--------")
bike.remove('ducati')
print(bike)

too_expencive = 'yamaha'
bike.remove(too_expencive)
print(bike)
print(f'removed {too_expencive.title()} because it is beyound my buget')

# try it yourself
print('----try it yourself -----')
print('q.3-4')
guest_list = ['x','y','z']
print('hello',guest_list)

print('q3-5')
print(f'guest name {guest_list[1]} can not attend ' )
del guest_list[1]
guest_list.insert(1,'p')
print('new guest list ', guest_list)

print('q.3-6')
print('-----',guest_list,'-------')
guest_list.insert(0,'a')
guest_list.insert(2,'c')
guest_list.append('e')
print(guest_list)
print('-----')
i = len(guest_list)
for i in range(4) :
    poped_name = guest_list.pop(2)
    print(guest_list)
    print(poped_name)

print('-----------------------------------------------------')
cars = ['bmw','audi','toyota','mg']
print(cars)
print(sorted(cars))
print(sorted(cars,reverse=True))
new = f'{cars.sort()}'
print(new)

#try it yourself
print('=---------------------------- Try it your self -----------------------------')
locations = ['Ireland', 'kashi', 'vridhavan', 'uk','NOrth poal']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
locations.reverse()
print(locations)
locations.reverse()
print(locations)
print('q.3-9')
print(len(guest_list))
