import random
import string

def generate_password(length):
    if length < 4:
        print("Password should be at least 4 characters long.")
        return ""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator 🔐")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        if password:
            print("Generated password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
