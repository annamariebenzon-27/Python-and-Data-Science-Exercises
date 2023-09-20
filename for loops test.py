x=input('Pick a number: ')
try:
    xf=int(x)
except:
    print('Please enter number only')
else:
    xf>0
    while xf>0:
        print(xf)
        xf=xf-1
    print('Blastoff')
    print(xf)
