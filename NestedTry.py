L=[10,20,30,40,50]

try:
    try:
        index=int(input('Enter Index'))
        print(L[index])
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
except Exception as e:
    print(e)