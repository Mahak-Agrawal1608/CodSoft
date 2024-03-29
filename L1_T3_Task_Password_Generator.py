import random
import string

def generate_password(length):
    # Define the characters to be used in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for password length.")
            return

        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
