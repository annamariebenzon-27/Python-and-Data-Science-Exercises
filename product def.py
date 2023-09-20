a=input('First number: ')
b=input('Second number: ')
try:
    af=float(a)
    bf=float(b)
    if af>0 or af>0 and bf<0 or bf>0:
        print('Nice pick')
    elif af==0 and bf==0:
        print('Zero')
except:
    print('Please enter numbers only')
    print('Try again')
else:
    def multiply(af,bf):
        product=af*bf
        return product
    x=multiply(af,bf)
    print(x)
