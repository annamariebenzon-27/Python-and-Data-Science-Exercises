sh=input('Enter Hours: ')
sr=input('Enter Rate: ')
try:
    fh=float(sh)
    fr=float(sr)
except:
    fh=-1
    fr=-1
if fh>0 and fr>0:
    print ('Your pay is:')
else:
    print('Please enter a number only, not in words')

if fh>40:
    #print('overtime')
    reg=fr*fh
    otp=(fh-40.0)*(fr*0.5)
    #print(reg,otp)
    xp=reg+otp

else:
    #print('regular')
    xp=fh*fr
if xp==1:
    print('please repeat')
else:
    print(xp)
