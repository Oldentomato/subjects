def dictProcess():
    dict1 = {"name": "John", "age": 30}
    dict2 = {"math": 90, "science": 85, "history": 78}
    dict3 = {'apple': 3, 'banana': 5}

    print(f"나이: {dict1.get('age')}")
    print(f"과목들: {list(dict2.keys())}")
    dict3["apple"] += 2
    print(dict3)


dictProcess()