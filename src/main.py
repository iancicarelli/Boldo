from utils.excel_processor import ExcelProcessor
def main():
    # Input en este caso se refiere para obtener las hojas 1 y 2 
    #output es la salida del archivo final en el formato correspondiente
    input_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\sheets12.xlsx"
    output_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\eje2.xlsx"

    # Crear una instancia del procesador de Excel
    processor = ExcelProcessor(input_path)

    # Llamar a la función de combinación de hojas
    processor.copy_excel_file(input_path, output_path)

    # Leer el archivo de entrada
    processor.read_excel()

    # Si tienes datos que escribir en el Excel
    out_formats = []  # Debes definir la lista de objetos que quieres procesar aquí
    # Escribir en un nuevo archivo de salida
    processor.write_excel(out_formats, output_path)

if __name__ == "__main__":
    main()