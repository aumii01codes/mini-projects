import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("Enter the length of the password: "))
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)


'''
Enter the length of the password: 12
Generated Password: M06LsxGBPsEe
'''