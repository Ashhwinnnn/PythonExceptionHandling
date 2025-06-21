def fun():
    try:
        x=int('256')
        return x
    
    except exception as e:
        raise e
    finally:
        print('End of function')

res=fun()
print(res)