import sys
import os
import unittest

# Agregar la ruta a 'src' para que Python pueda encontrar los módulos allí
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.excel_processor import ExcelProcessor
from utils.cost_processor import CostProcessor

class TestMatch(unittest.TestCase):
    def setUp(self):
        # Rutas de los archivos de entrada
        self.maestra_path = r"C:\Users\HP\Desktop\BoldoGit\maestra.xlsx"
        self.orion_path = r"C:\Users\HP\Desktop\BoldoGit\BD ORION.xlsx"
        self.bd_ila_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\BDilas.xlsx"
        
        # Crear una instancia de CostProcessor con el path de BD_ILA
        self.cost_processor = CostProcessor(self.maestra_path, self.orion_path, self.bd_ila_path)

    def test_match_ila_values_with_groups(self):
        ila_values = self.cost_processor.match_ila_values_with_groups()
        print("Lista de valores ILA: ", ila_values)

if __name__ == "__main__":
    unittest.main()