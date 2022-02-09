def greet (first_name, last_name):
    print (f"Hi {first_name}, {last_name}")
    print("Hello ")

greet("emmanuel", "Eliarms")


def get_greeting(name):
    return f"Hi{name}"
message = get_greeting("me")
file = open ("note.txt", "w")
file.write(message)

def increment (number, by=1):
    return number + by
print(increment(2))

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *=number
    return total


print(multiply(2,3,4))

def save_user(**user):
    print (user)

save_user(id=1, name="john", age=22)


def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 ==0:
        return "Fizz"
    if input % 5 ==0:
        return "Buzz"

    return input
print(fizz_buzz(7))