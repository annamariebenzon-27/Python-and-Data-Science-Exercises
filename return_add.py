a=input('First number: ')
b=input('Second number: ')
try:
    af=float(a)
    bf=float(b)
    if af>0 or af>0 and bf<0 or bf>0:
        print('Nice pick')
    elif af==0 and bf==0:
        print('0')
except:
    print('Please enter numbers only')
    print('Click cancel when asked to quit if you like to continue adding numbers')
    quit()
def addtwo(a,b):
    added=a+b
    return added
x=addtwo(a, b)
print(x)

