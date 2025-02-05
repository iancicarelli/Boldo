from utils.excel_processor import ExcelProcessor
import json

class CostProcessor:
    def __init__(self, maestra_path, orion_path, bd_ila_path):
        self.maestra_processor = ExcelProcessor(maestra_path)
        self.orion_processor = ExcelProcessor(orion_path)
        self.ila_processor = ExcelProcessor(bd_ila_path) 

    def get_matching_groups(self):
    # Leer los archivos Excel
        self.maestra_processor.read_excel()
        self.orion_processor.read_excel()
    # Obtener las hojas de trabajo
        maestra_sheet = self.maestra_processor.get_sheet()
        orion_sheet = self.orion_processor.get_sheet()
    # Extraer códigos desde la columna A de maestra.xlsx
        maestra_codes = [row[0].value for row in maestra_sheet.iter_rows(min_row=2, max_row=maestra_sheet.max_row, min_col=1, max_col=1) if row[0].value]
    # Diccionario para almacenar coincidencias {codigo: descripcion}
        matching_dict = {}
    # Buscar coincidencias en BD ORION.xlsx (columna D) y obtener la descripción de la columna F
        for row in orion_sheet.iter_rows(min_row=2, max_row=orion_sheet.max_row, min_col=4, max_col=6):
            orion_code = row[0].value  # Código en columna D
            group = row[2].value  # Descripción en columna F
            if orion_code in maestra_codes:
                matching_dict[orion_code] = group  # Guardar la coincidencia
        matching_groups = [matching_dict.get(code, "N/A") for code in maestra_codes]
    
        return matching_groups
  
    def get_ila_values(self):
        self.ila_processor.read_excel()
        ila_sheet = self.ila_processor.get_sheet()

        ila_mapping = {}
        for row in ila_sheet.iter_rows(min_row=2, max_row=ila_sheet.max_row, min_col=2, max_col=5):
            name = row[0].value  # Valor en columna B
            value = row[3].value  # Valor en columna E
            if name and value:  # Solo agregar si ambos valores existen
                ila_mapping[name] = value     
        return ila_mapping

    def match_ila_values_with_groups(self):
        matching_groups = self.get_matching_groups()
        ila_values = self.get_ila_values()
        result = []
        for group in matching_groups:
            if group != "N/A" and group in ila_values:
                result.append(ila_values[group])  # Retorna el valor de ILA si hay coincidencia
            else:
                result.append("N/A")  # Si no hay coincidencia o el valor es "N/A"

        return result
    
    def compare_with_json(self):
        # Cargar el archivo JSON
        json_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\ilas.json"
        with open(json_path, "r", encoding="utf-8") as f:
            ila_json = json.load(f)
        # Crear un diccionario de nombres y montos desde el JSON
        json_mapping = {entry["Nombre"]: entry["MONTO"] for entry in ila_json}
        # Obtener la lista de valores de ILA desde match_ila_values_with_groups
        ila_values = self.match_ila_values_with_groups()
        # Comparar y crear la lista de montos correspondientes
        result_montos = []
        for value in ila_values:
            if value != "N/A" and value in json_mapping:
                result_montos.append(json_mapping[value])  # Retorna el MONTO si existe
            else:
                result_montos.append(1.19)  # Retorna el valor por defecto 1.19 si no hay coincidencia

        return result_montos