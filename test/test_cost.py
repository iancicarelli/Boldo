import sys
import os
import unittest

# Agregar la ruta a 'src' para que Python pueda encontrar los módulos allí
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.excel_processor import ExcelProcessor
from utils.cost_processor import CostProcessor  # Asumiendo que cost_processor.py está en 'src'

class TestCostProcessor(unittest.TestCase):
    def setUp(self):
    # Rutas de los archivos de entrada
        self.maestra_path = r"C:\Users\HP\Desktop\BoldoGit\pldcostos.xlsx"
        self.orion_path = r"C:\Users\HP\Desktop\BoldoGit\BD ORION.xlsx"
        self.bd_ila_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\BDilas.xlsx"
    
    # Crear una instancia de CostProcessor con ila_path
        self.cost_processor = CostProcessor(self.maestra_path, self.orion_path, self.bd_ila_path)

    def test_get_matching_groups(self):
        # Llamar al método get_matching_groups para obtener las coincidencias
        matching_groups = self.cost_processor.get_matching_groups()

        # Verificar que se encontraron coincidencias
        self.assertIsNotNone(matching_groups)
        self.assertGreater(len(matching_groups), 0)
        
        # Imprimir las coincidencias por consola
        print("Coincidencias encontradas:")
        for group in matching_groups:
            print(group)
        


if __name__ == "__main__":
    unittest.main()