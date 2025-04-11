def NumParser(input):
    birth = input.split("-")[0]
    print(f"{'20' if int(birth[:2]) <= 21 else '19'}{birth[:2]}년 {birth[2:4]}월 {birth[4:6]}일")

NumParser("901212-1234567")