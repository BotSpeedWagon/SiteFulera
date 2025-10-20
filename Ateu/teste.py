def func(string):
    def wrapper():
        print("Iniciada")
        print(string)
        print("Finalizada")
    return wrapper()