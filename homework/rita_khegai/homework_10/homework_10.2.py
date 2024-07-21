# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция.


def repeat_me(func):

    def wrapper(what, how_many):
        count = 0
        while count < how_many:
            func(what)
            count += 1

    return wrapper


@repeat_me
def print_text(text):
    print(text)


print_text('ура', 3)
