def stringProcess():
    print("Hello","World")
    print("Hello World".upper())
    print("Hello World"[-5:])
    print("Python is fun".split(' '))
    print(*(char for i,char in enumerate("abcdef") if i % 2 == 0), sep='')
    print(*("Hello" for _ in range(0,3)), sep='')


stringProcess()