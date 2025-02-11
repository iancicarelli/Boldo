from utils.excel_processor import ExcelProcessor
from models.out_format import OutFormat
from utils.cost_processor import CostProcessor

class DataProcessor:
    def __init__(self, input_path, output_path, maestra_path, orion_path, bd_ila_path):
        self.input_path = input_path
        self.output_path = output_path
        self.excel_processor = ExcelProcessor(maestra_path)
        self.cost_processor = CostProcessor(maestra_path, orion_path, bd_ila_path)

    def add_cost_to_data(self, processed_data):
        """Agrega los costos calculados y retorna los datos procesados con costos."""
        # Obtener los valores calculados
        multiplied_values = self.cost_processor.multiply_lists()
        cleaned_values = self.cost_processor.replace_non_numeric_values(multiplied_values)
        print(f"Numero de costos procesados = {len(cleaned_values)}")

        # Verificar que la cantidad de costos coincida con la cantidad de datos procesados
        if len(cleaned_values) != len(processed_data):
            raise ValueError("La cantidad de valores de costo no coincide con la cantidad de datos procesados")

        # Agregar los costos a los datos procesados
        for index, value in enumerate(cleaned_values):
            processed_data[index]["cost_neto"] = value
    
        return processed_data



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

    def convert_to_out_format(self, processed_data):
        """Convierte los datos en la estructura final `OutFormat`."""
        return [OutFormat(lin=data["lin"], code=data["codigo"], name=data["nombre"], uxe=data["uxe"], cost_neto=data["cost_neto"]) 
            for data in processed_data]

    def process_excel_data(self):
        """Orquesta el procesamiento de datos y genera el archivo Excel final."""
        # Obtener datos procesados sin los costos
        processed_data = self.get_processed_data()
        print(f"datos procesados con uxe = {len(processed_data)}")
        # Agregar los costos a los datos procesados
        processed_data_with_cost = self.add_cost_to_data(processed_data)

        # Convertir los datos a la estructura final `OutFormat`
        out_formats = self.convert_to_out_format(processed_data_with_cost)

        # Escribir los datos en el archivo Excel
        self.excel_processor.write_excel(out_formats, self.output_path)
