def emailVaild(email):
    if "@" not in email or "." not in email:
        print("유효하지 않음")
    else:
        print("유효함")

emailVaild("user@example.com")
emailVaild("user@example")