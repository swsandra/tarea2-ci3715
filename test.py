#test.py



import unittest
from tarifa import tarifa
from tiempoDeTrabajo import tiempoDeTrabajo
from main import calcularPrecio


class test_calcularPrecio(unittest.TestCase):

	def setUp(self):
		self.tarifa = tarifa(15,19)


	def test_15min(self):
		inicio = tiempoDeTrabajo(2018,5,7,0,0,0)
		final = tiempoDeTrabajo(2018,5,7,0,15,0)
		tiempoDeServicio = [inicio, final]
		res = calcularPrecio(self.tarifa, tiempoDeServicio)
		self.assertEqual(res, 15, "Espera 15. Dio " + str(res) )

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
		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 15, "test_menosDeUnaHora fallo")


	def test_trabajoDosHoras(self):
		inicio = tiempoDeTrabajo(2018,5,9,3,50,53)
		final  = tiempoDeTrabajo(2018,5,9,5,50,53)
		tiempoDeServicio = [inicio, final]
		#tiempoDeServicio[0] = inicio
		#tiempoDeServicio[1] = final

		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 30, "test_trabajoDosHoras fallo")


	def test_trabajoUnaHoraFin(self):
		inicio = tiempoDeTrabajo(2018,5,6,3,50,53)
		final = tiempoDeTrabajo(2018,5,6,4,50,53)
		tiempoDeServicio = [inicio, final]
		self.assertEqual(calcularPrecio(self.tarifa, tiempoDeServicio), 19, "test_trabajoUnaHoraFin fallo")

	def test_tresDias(self):
		inicio = tiempoDeTrabajo(2018,5,7,3,50,53)
		final = tiempoDeTrabajo(2018,5,10,3,50,52)
		tiempoDeServicio = [inicio, final]
		res = calcularPrecio(self.tarifa, tiempoDeServicio)
		self.assertEqual(res, 1080, "Espera 1080. Dio " + str(res) )


	def test_casi7Dias(self):
		#COMIENZO UN LUNES, TERMINO UN SABADO A LAS 23:59 6 Dias.
		inicio = tiempoDeTrabajo(2018,5,7,0,0,0)
		final = tiempoDeTrabajo(2018,5,12,23,59,0)
		tiempoDeServicio = [inicio, final]
		res = calcularPrecio(self.tarifa, tiempoDeServicio)
		self.assertEqual(res, 2256, "Espera 2256. Dio " + str(res) )


	def test_8Dias(self):
		inicio = tiempoDeTrabajo(2018,5,7,0,0,0)
		final = tiempoDeTrabajo(2018,5,14,0,0,0)
		tiempoDeServicio = [inicio, final]
		#res = calcularPrecio(self.tarifa, tiempoDeServicio)
		self.assertRaises(Exception, calcularPrecio, self.tarifa, tiempoDeServicio)
		#self.assertEqual(res, 2712, "Espera 2712. Dio " + str(res) )

	def test_14min(self):
		inicio = tiempoDeTrabajo(2018,5,7,0,0,0)
		final = tiempoDeTrabajo(2018,5,7,0,14,0)
		tiempoDeServicio = [inicio, final]
		#res = calcularPrecio(self.tarifa, tiempoDeServicio)
		self.assertRaises(Exception, calcularPrecio, self.tarifa, tiempoDeServicio)

	def test_finItermedio(self):



def suite():
    suite = unitest.TestSuite()

    #Fronteras
    suite.addTest(test_calcularPrecio('test_15min'))
    suite.addTest(test_calcularPrecio('test_14min'))
    suite.addTest(test_calcularPrecio('test_8Dias'))

    suite.addTest(test_calcularPrecio('test_trabajoUnaHoraFin'))

    suite.addTest(test_calcularPrecio('test_trabajoDosHoras'))
    suite.addTest(test_calcularPrecio('test_menosDeUnaHora'))
    suite.addTest(test_calcularPrecio('test_mismoDia'))
    suite.addTest(test_calcularPrecio('test_tresDias'))
    suite.addTest(test_calcularPrecio('test_casi7Dias'))


    return suite



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())