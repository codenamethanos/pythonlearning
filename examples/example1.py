course = 'Python for Beginners'
print('This is ' + course[0:3])
print(course[2:])   
print(course[:5])
print(course[:])    
print(course[1:-1])

# formatted string
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg.upper())
print(msg.find('o'))
print(msg.find('John'))
print(msg.replace('John', 'Jane'))  
print("John" in msg)