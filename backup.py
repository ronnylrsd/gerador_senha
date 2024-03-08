import random
import string

def password_generator(length, special_chars, include_uppercase, include_lowercase):
    if length < 4:
        print("The length of the password is too short.")
        return
    
    password = []
    
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if special_chars:
        password.append(random.choice(special_chars))
    
    # Garante pelo menos um dígito
    password.append(random.choice(string.digits))
    
    # Calcula quantos caracteres faltam adicionar
    remaining_length = length - len(password)
    
    possibilities = string.digits + special_chars
    if include_uppercase:
        possibilities += string.ascii_uppercase
    if include_lowercase:
        possibilities += string.ascii_lowercase
    
    password.extend(random.choices(possibilities, k=remaining_length))
    random.shuffle(password)
    return "".join(password)

# Solicitações ao usuário
length = int(input("Enter the length of the password: "))
special_chars_input = input("Enter the special characters you want to include: ")
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'

print(password_generator(length, special_chars_input, include_uppercase, include_lowercase))
