def my_or(x1, x2):
    return x1 or x2

def my_and(x1, x2):
    return x1 and x2

def my_xor(x1, x2):
    return my_or(x1, x2) and not my_and(x1, x2)

def get_input():
    while True:
        try:
            x1 = int(input("Введіть перше число (0 або 1): "))
            x2 = int(input("Введіть друге число (0 або 1): "))
            if (x1 in [0, 1]) and (x2 in [0, 1]):
                return bool(x1), bool(x2)
            else:
                print("Введіть тільки 0 або 1.")
        except ValueError:
            print("Помилка вводу! Будь ласка, введіть число 0 або 1.")

def main():
    while True:
        x1, x2 = get_input()
        result = my_xor(x1, x2)
        print(f"XOR({x1}, {x2}) = {result}")

        user_choice = input("\nБажаєте спробувати знову? (так/ні): ").strip().lower()
        if user_choice != 'так':
            print("Вихід з програми!")
            break

if __name__ == "__main__":
    main()
