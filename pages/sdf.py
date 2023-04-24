import random


def generate_symbol(length):
    letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяЁёabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


stroka = generate_symbol(5)
print(stroka)