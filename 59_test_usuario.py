import unittest


class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class TestUsuario(unittest.TestCase):
    def test_saludar(self):
        u = Usuario("Jose", 25)
        self.assertEqual(u.saludar(), "Hola, mi nombre es Jose y tengo 25 años.")
if __name__ == '__main__':
    unittest.main()