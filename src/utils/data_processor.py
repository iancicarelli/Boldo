from utils.excel_processor import ExcelProcessor
from models.out_format import OutFormat

class DataProcessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.excel_processor = ExcelProcessor(input_path)
    
    def convert_to_out_format(self, processed_data):
        out_formats = []
        for data in processed_data:
            # Asignar el valor de LIN en la conversión
            out_formats.append(OutFormat(lin=data["lin"], code=data["codigo"], name=data["nombre"], uxe=data["uxe"], cost_neto=""))
        return out_formats

    def calculate_lin(self, products):
        for index, product in enumerate(products, start=1):
            product["lin"] = index  # Asignar número secuencial
        return products

    def get_processed_data(self):
        # Leer el archivo Excel
        self.excel_processor.read_excel()
        sheet = self.excel_processor.get_sheet()
        processed_data = []  # Lista para almacenar los datos procesados
        # Iterar sobre las filas del archivo Excel (comenzando desde la fila 2 para saltar los encabezados)
        for index, row in enumerate(sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=4), start=1):
            codigo = row[0].value  # Columna A (Código)
            nombre = row[1].value  # Columna B (Nombre)
            uxe = row[3].value     # Columna D (UXE)
            # Guardar los valores procesados con el LIN
            processed_data.append({"lin": index, "codigo": codigo, "nombre": nombre, "uxe": uxe})
        return processed_data

    def process_excel_data(self):
        # Obtener los datos del Excel
        processed_data = self.get_processed_data()
        # Convertir los datos al formato requerido
        out_formats = self.convert_to_out_format(processed_data)
        # Escribir los datos en un nuevo archivo Excel
        self.excel_processor.write_excel(out_formats, self.output_path)
