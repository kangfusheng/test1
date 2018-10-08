#装饰器
#@log
'''
* 无名字的参数
** 有名字的参数
'''
def log(func):
    def wrapper(*args, **kvargs):
        print('before calling ',func.__name__)
        print('args', args, 'kvargs', kvargs)
        func(*args, **kvargs)
        print('end calling ',func.__name__)
    return wrapper

@log
def hello(name,age):
    print('hello', name, age)


if __name__ == '__main__':
    hello('newcoder', 2) #这个2是无名字参数
    hello('newcoder', age = 2) #这个2是有名字的参数


