# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished"
# после выполнения декорированной функции.


def finish_me(func):

    def wrapper(some_text):
        func(some_text)
        print(f'FUNCTION {func.__name__} FINISHED')

    return wrapper


@finish_me
def print_text(some_text):
    print(some_text)


print_text('¡Hola amigos!')
