L=[10,20,30,40,50]
try:
    index=9
    print(L[index])
except IndexError:
    print('Invalid Index')
except TypeError:
    print('Index should be int')
except:
    print('some errror')
print('End of program')