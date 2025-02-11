import sys
from pathlib import Path
import os

class PathManager:
    def __init__(self):
        self.is_frozen = getattr(sys, 'frozen', False)
        self.BASE_DIR = self.get_base_dir()
        self.DATA_DIR = self.BASE_DIR / "data"
        self.THEMES_DIR = self.BASE_DIR / "visuals" / "themes"  # Agregado para gestionar los temas
        self.IMAGE_DIR = self.BASE_DIR / "visuals" / "themes"  # Agregado para gestionar las imágenes

    def get_base_dir(self):
        """Obtiene el directorio base del proyecto, dependiendo si está empaquetado o en desarrollo."""
        if self.is_frozen:
            # Si se ejecuta como .exe (empaquetado con PyInstaller)
            return Path(sys._MEIPASS).resolve()
        else:
            # Si se ejecuta como un script en desarrollo
            return Path(__file__).resolve().parent.parent

    def get_input_path(self):
        """Obtiene la ruta al archivo de entrada."""
        return str(self.DATA_DIR / "formatosalida.xlsx")

    def get_bd_ila_path(self):
        """Obtiene la ruta al archivo BD ILA."""
        return str(self.DATA_DIR / "BDilas.xlsx")

    def get_json_path(self):
        """Obtiene la ruta al archivo JSON de ILA."""
        json_path = self.DATA_DIR / "ilas.json"
        if self.is_frozen:
            # Si está empaquetado, busca el archivo en el directorio temporal
            json_path = Path(sys._MEIPASS) / "data" / "ilas.json"
        return str(json_path)

    def get_output_path(self, output_dir, output_name):
        """Construye la ruta de salida del archivo Excel."""
        return os.path.join(output_dir, f"{output_name}.xlsx")

    # Métodos para obtener la ruta del tema y la imagen
    def get_theme_path(self, theme_name):
        """Obtiene la ruta al archivo de tema."""
        theme_path = self.THEMES_DIR / theme_name
        if self.is_frozen:
            # Si está empaquetado, busca el tema en el directorio temporal
            theme_path = Path(sys._MEIPASS) / "visuals" / "themes" / theme_name
        return str(theme_path)

    def get_image_path(self, image_name):
        """Obtiene la ruta a la imagen."""
        image_path = self.IMAGE_DIR / image_name
        if self.is_frozen:
            # Si está empaquetado, busca la imagen en el directorio temporal
            image_path = Path(sys._MEIPASS) / "visuals" / "themes" / image_name
        return str(image_path)
