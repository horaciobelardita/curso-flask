integer: int = 4
decimal: float = 2.5
is_active: bool = False
text: str = "Alan Walker"
status = "online" if is_active else "offline"
print(f"Status: {status}")


def show_multiplication_table(base: int, start: int = 1, end: int = 10):
    for i in range(start, end + 1):
        print(f"{i} x {base} = {i*base}")


def table():
    try:
        base = int(input("Ingrese un numero?: "))
        show_multiplication_table(base)
    except ValueError as e:
        print(f"Error: {str(e)}")


def try_catch():
    x = 10
    y = 0
    try:
        print(x // y)
    except ZeroDivisionError as e:
        print(f"Error: {str(e)}")


colors = ["red", "green", "blue"]
colors.append("white")
print(colors)
user = ("Mark", 34)  # tupla
# destructuring
name, age = user
print(name, age)
person = {
    "gender": "male",
    "name": {"title": "mr", "first": "brad", "last": "gibson"},
}
for key, value in person.items():
    print(f"key: {key} -> {value}")
fullname = lambda person: f"{person['name']['first']} {person['name']['last']}"
print(f"Hello, {fullname(person)}")

# comprehension
letters_whithout_i = [letter for letter in fullname(person) if letter != "i"]
print("".join(letters_whithout_i))
