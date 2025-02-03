from utils.excel_processor import ExcelProcessor
from utils.data_processor import DataProcessor

class Constructor:
    def __init__(self, input_path, output_path, maestra_path):
        self.input_path = input_path
        self.output_path = output_path
        self.maestra_path = maestra_path

    def execute(self):
        # Crear una instancia del procesador de Excel
        excel_processor = ExcelProcessor(self.input_path)

        # Copiar el archivo de entrada a la ubicación de salida
        excel_processor.copy_excel_file(self.input_path, self.output_path)
        # excel_processor.write_excel(self.output_path)
        # Procesar los datos del Excel
        data_processor = DataProcessor(self.maestra_path, self.output_path)
        data_processor.process_excel_data()

        # Aquí puedes agregar más lógica de procesamiento si lo necesitas

