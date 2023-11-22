import unittest

class Personaje:
    def __init__(self):
        self.vida = 100
        self.monedas = 0
        self.diamantes = 0

    def agregar_monedas(self, cantidad):
        self.monedas += cantidad
        # Por cada 10 monedas, se recibe 1 punto de vida adicional
        self.vida += self.monedas // 10
        self.verificar_diamante()

    def perder_vida(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0

    def verificar_diamante(self):
        # Por cada 200 monedas, se obtiene un diamante
        self.diamantes += self.monedas // 200
        self.monedas %= 200

    def esta_vivo(self):
        return self.vida > 0

    def obtener_estado(self):
        return f"Puntos de vida: {self.vida}, Monedas: {self.monedas}, Diamantes: {self.diamantes}"

class TestPersonaje(unittest.TestCase):
    def setUp(self):
        self.personaje = Personaje()

    def test_creacion_personaje(self):
        self.assertEqual(self.personaje.vida, 100)
        self.assertEqual(self.personaje.monedas, 0)

    def test_agregar_monedas(self):
        self.personaje.agregar_monedas(30)
        self.assertEqual(self.personaje.monedas, 30)
        self.assertEqual(self.personaje.vida, 103)  # 100 + (30 // 10)

    def test_perder_vida(self):
        self.personaje.perder_vida(20)
        self.assertEqual(self.personaje.vida, 80)

    def test_verificar_diamante(self):
        self.personaje.agregar_monedas(200)
        self.assertEqual(self.personaje.diamantes, 1)
        self.assertEqual(self.personaje.monedas, 0)

    def test_esta_vivo(self):
        self.assertTrue(self.personaje.esta_vivo())
        self.personaje.perder_vida(110)
        self.assertFalse(self.personaje.esta_vivo())

    def test_obtener_estado(self):
        estado = self.personaje.obtener_estado()
        self.assertEqual(estado, "Puntos de vida: 100, Monedas: 0, Diamantes: 0")

if __name__ == '__main__':
    unittest.main()
