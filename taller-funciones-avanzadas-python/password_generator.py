from random import randint, choice

def random_letter():
    random_n = randint(97,122)
    return chr(random_n)

def random_letter_upper():
    return random_letter().upper()

def random_number():
    return randint(0,9)

def random_simbol():
    simbols = '&%$(#)'
    return choice(simbols)


def gen_password(len_password):
    list_f = [random_letter, random_letter_upper,random_number, random_simbol]
    password = ''.join([str(list_f[randint(0,3)]()) for i in range(len_password)])
    return password

print(gen_password(10))