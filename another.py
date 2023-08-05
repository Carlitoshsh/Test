import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a strong password with default length of 12 characters
strong_password = generate_strong_password()
print("Generated Strong Password:", strong_password)
