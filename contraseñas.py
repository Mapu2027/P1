import random
while True:
    simbolos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    Caracteres = int(input("¿Cuantos caracteres quieres que tenga tu contraseña?:"))
    password = ""
    for i in range(Caracteres):
        password += random.choice(simbolos)
    print(password)
