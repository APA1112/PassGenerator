import unittest
import string
from script import generate_password  # Reemplaza con el nombre real de tu módulo

class TestPasswordGenerator(unittest.TestCase):
    
    def test_length(self):
        """Verifica que la contraseña tenga la longitud especificada"""
        length = 16
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_minimum_length(self):
        """Verifica que la función retorna un error si la longitud es menor a 10"""
        password = generate_password(9)
        self.assertEqual(password, "La longitud minima es 10 caracteres")

    def test_contains_valid_characters(self):
        """Verifica que la contraseña solo contiene caracteres alfanuméricos y especiales"""
        valid_chars = string.ascii_letters + string.digits + string.punctuation
        password = generate_password(12)
        self.assertTrue(all(char in valid_chars for char in password))

    def test_contains_digits(self):
        """Verifica que la contraseña contiene al menos un dígito"""
        password = generate_password(12)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_contains_uppercase(self):
        """Verifica que la contraseña contiene al menos una letra mayúscula"""
        password = generate_password(12)
        self.assertTrue(any(char.isupper() for char in password))

    def test_contains_lowercase(self):
        """Verifica que la contraseña contiene al menos una letra minúscula"""
        password = generate_password(12)
        self.assertTrue(any(char.islower() for char in password))

    def test_contains_special_characters(self):
        """Verifica que la contraseña contiene al menos un carácter especial"""
        special_chars = string.punctuation
        password = generate_password(12)
        self.assertTrue(any(char in special_chars for char in password))

    def test_no_spaces(self):
        """Verifica que la contraseña no contiene espacios"""
        password = generate_password(12)
        self.assertNotIn(" ", password)

    def test_randomness(self):
        """Genera varias contraseñas y comprueba que no sean idénticas"""
        passwords = {generate_password(12) for _ in range(10)}
        self.assertGreater(len(passwords), 1)  # Se espera que al menos dos sean diferentes

if __name__ == '__main__':
    unittest.main()
