# Import required libraries
import secrets  # For generating cryptographically strong random numbers
import string   # For accessing string constants (letters, digits, etc.)

# Default password length
PSW_LENGTH = 12  # Changed to uppercase as it's a constant

def generate_password(psw_length):
    """
    Generates a random password with specified length
    
    Args:
        psw_length (int): Desired length of the password
    
    Returns:
        str: Generated password or error message
    """
    # Set default length if None is provided
    if psw_length is None:
        psw_length = 12
    
    # Validate minimum password length
    if psw_length < 10:
        return "La longitud minima es 10 caracteres"
    
    # Convert input to integer
    psw_length = int(psw_length)

    # Define character sets for password generation
    letters = string.ascii_letters      # Both uppercase and lowercase letters
    digits = string.digits              # Numbers from 0-9
    special_chars = string.punctuation  # Special characters

    # Combine all character sets
    all_chars = letters + digits + special_chars
    
    # Generate password using list comprehension for better performance
    password = ''.join(secrets.choice(all_chars) for _ in range(psw_length))
    return password

# Generate and print a password with default length
print("Contraseña generada:", generate_password(PSW_LENGTH))