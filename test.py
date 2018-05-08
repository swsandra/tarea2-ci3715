#test.py



import unittest
from tarifa import tarifa
from tiempoDeTrabajo import tiempoDeTrabajo
from main import calcularPrecio


class test_calcularPrecio(unittest.TestCase):

	def setUp(self):
		self.tarifa = tarifa(15,19)

	def test_mismoDia(self):
		inicio = tiempoDeTrabajo(2018,5,9,2,50,53)
		final = tiempoDeTrabajo(2018,5,9,3,50,53)
		tiempoDeServicio = [inicio, final]
		#tiempoDeServicio[0] = inicio
		#tiempoDeServicio[1] = final

		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 15, "test_mismoDia fallo")

	def test_menosDeUnaHora(self):
		inicio = tiempoDeTrabajo(2018,5,9,2,50,53)
		final = tiempoDeTrabajo(2018,5,9,3,7,50)
		tiempoDeServicio = [inicio, final]
		#tiempoDeServicio[0] = inicio
		#tiempoDeServicio[1] = final
		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 0, "test_menosDeUnaHora fallo")


	def test_trabajoDosHoras(self):
		inicio = tiempoDeTrabajo(2018,5,9,4,50,53)
		final  = tiempoDeTrabajo(2018,5,9,3,50,53)
		tiempoDeServicio = [inicio, final]
		#tiempoDeServicio[0] = inicio
		#tiempoDeServicio[1] = final

		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 30, "test_trabajoDosHoras fallo")


	def test_trabajoUnaHoraFin(self):
		inicio = tiempoDeTrabajo(2018,5,6,4,50,53)
		final = tiempoDeTrabajo(2018,5,6,3,50,53)
		tiempoDeServicio = [inicio, final]
		#tiempoDeServicio[0] = inicio
		#tiempoDeServicio[1] = final

		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 19, "test_trabajoUnaHoraFin fallo")


if __name__ == '__main__':
    unittest.main()
