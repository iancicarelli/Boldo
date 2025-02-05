from utils.constructor import Constructor

def main():
    # Definir las rutas de los archivos
    input_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\sheets12.xlsx"
    output_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\eje2.xlsx"
    maestra_path = r"C:\Users\HP\Desktop\BoldoGit\maestra.xlsx"
    orion_path = r"C:\Users\HP\Desktop\BoldoGit\BD ORION.xlsx"
    bd_ila_path = r"C:\Users\HP\Desktop\BoldoGit\Boldo\src\data\BDilas" 

    # Crear una instancia del Constructor y ejecutar el proceso
    constructor = Constructor(input_path, output_path, maestra_path)
    constructor.execute()

if __name__ == "__main__":
    main()
