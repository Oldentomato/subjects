def countVowels(input):
    vowels = {"a","e","i","o","u"}
    count = 0
    for i in input.strip():
        if i in vowels:
            count += 1

    print(f"모음 개수: {count}")

countVowels("Python is awesome")