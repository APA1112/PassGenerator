# Import required libraries
import secrets  # For generating cryptographically strong random numbers
import string   # For accessing string constants (letters, digits, etc.)

# Default password length
pswLenght = 12

def generate_password(pswLenght):
    """
    Generates a random password with specified length
    Args:
        pswLenght (int): Desired length of the password
    Returns:
        str: Generated password or error message
    """
    # Set default length if None is provided
    if pswLenght is None:
        pswLenght = 12
    
    # Validate minimum password length
    if pswLenght < 10:
        return "La longitud minima es 10 caracteres"
    
    # Convert input to integer
    pswLenght = int(pswLenght)

    # Define character sets for password generation
    letters = string.ascii_letters      # Both uppercase and lowercase letters
    digits = string.digits              # Numbers from 0-9
    special_chars = string.punctuation  # Special characters

    # Combine all character sets
    all_chars = letters + digits + special_chars
    
    # Generate password by randomly selecting characters
    psw = ""
    for i in range(pswLenght):
        psw += ''.join(secrets.choice(all_chars))
    return psw

# Generate and print a password with default length
print("Constraseña generada:", generate_password(12))