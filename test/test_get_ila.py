import sys
import os
import unittest

# Agregar la ruta a 'src' para que Python pueda encontrar los módulos allí
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.excel_processor import ExcelProcessor
from utils.cost_processor import CostProcessor

class TestIla(unittest.TestCase):
    def setUp(self):
        # Rutas de los archivos de entrada
        self.maestra_path = r"C:\Users\HP\Desktop\BoldoGit\maestra.xlsx"
        self.orion_path = r"C:\Users\HP\Desktop\BoldoGit\BD ORION.xlsx"
        self.bd_ila_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\BDilas.xlsx"
        
        # Crear una instancia de CostProcessor con el path de BD_ILA
        self.cost_processor = CostProcessor(self.maestra_path, self.orion_path, self.bd_ila_path)

    def test_get_ila_values(self):
        # Ejecutar el método
        ila_results = self.cost_processor.get_ila_values()

        # Imprimir los resultados obtenidos
       # print("Resultados obtenidos desde BD_ILA:")
        #print(ila_results)

        # Verificar que el diccionario de resultados no esté vacío
        self.assertIsNotNone(ila_results)
        self.assertGreater(len(ila_results), 0)

        # Verificar que los valores tengan la forma correcta {nombre_col_B: valor_col_E}
        for name, value in ila_results.items():
            print(f"Nombre: {name}, Impuesto asociado: {value}")
            self.assertIsInstance(name, str)
            self.assertIsInstance(value, str)

if __name__ == "__main__":
    unittest.main()
