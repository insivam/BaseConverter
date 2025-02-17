while True:
    number = int(input("Your target number: "))
    base = int(input("Base number: "))

    result = ""
    while number > 0:
        result = str(number  % base) + result
        number = number // base

    print("="*25)
    print(f"RESULT = {result}".center(25))
    print("="*25, end="\n\n")
