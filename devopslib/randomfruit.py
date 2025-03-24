from random import choices


def meal(beverage):
    my_fruit = fruit()
    print(my_fruit)
    if my_fruit == "cherry":

        return f"Your meal is {my_fruit} and {beverage}"

    return f"Your meal is steak and {beverage}"


def fruit():
    return choices(["apple", "cherry", "strawberry"])[0]
