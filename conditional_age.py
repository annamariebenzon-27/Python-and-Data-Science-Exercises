x=input('Enter your age: ')
try:
    age=int(x)
except:
    print('Please enter numbers only')
else:
    if age>18:
        print('You can enter')
    elif age==18:
        print('Go see Pink Floyd')
    else:
        print('Go see Meat Loaf')
    print('move on')
