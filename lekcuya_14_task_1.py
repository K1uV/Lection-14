def decorator(func):
    def wrapper():
        print('l = 4 + 5') 
        func()
    return wrapper   

@decorator
def add(x = 4, y = 5):
    l = x + y
    print(l)

adds = decorator(add)
add()