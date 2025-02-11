from ttkthemes import ThemedTk
from utils.constructor import Constructor
from utils.path_manager import PathManager
from tkinter import Label, Button, Entry, filedialog, StringVar
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageTk
from pathlib import Path
import sys

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Pino")
        self.root.geometry("700x400")
        self.root.resizable(False, False)
        self.path_manager = PathManager()

        # Cargar el tema forest-light
        theme_path = self.path_manager.get_theme_path("forest-light.tcl")
        self.root.tk.call("source", theme_path)
        self.root.tk.call("ttk::style", "theme", "use", "forest-light")
        ttk.Style().theme_use("forest-light")

        # Cargar imagen de fondo
        bg_image_path = self.path_manager.get_image_path("fondoboldo.jpg")
        self.bg_image = Image.open(bg_image_path)
        self.bg_image = self.bg_image.resize((700, 400), Image.Resampling.LANCZOS)  # Ajustar tamaño
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Crear canvas y colocar imagen
        self.canvas = tk.Canvas(self.root, width=700, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
       

        # Construir las rutas a los archivos dentro de 'data'
        self.input_path = self.path_manager.get_input_path()
        self.bd_ila_path = self.path_manager.get_bd_ila_path()


        self.create_widgets()

    def create_widgets(self):
       
        # Crear un Frame sobre el Canvas para los widgets
        self.input_frame = ttk.Frame(self.root, padding="20")
        self.input_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centrar en la ventana

        self.maestra_path_var = tk.StringVar()
        self.orion_path_var = tk.StringVar()
        self.output_dir_var = tk.StringVar()
        self.output_name_var = tk.StringVar()

        ttk.Label(self.input_frame, text="Selección de directorios", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(self.input_frame, text="Seleccione una maestra:").grid(row=1, column=0, sticky="e", pady=5)
        ttk.Entry(self.input_frame, textvariable=self.maestra_path_var, width=40).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.input_frame, text="Buscar", command=self.select_maestra).grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Productos Orion:").grid(row=2, column=0, sticky="e", pady=5)
        ttk.Entry(self.input_frame, textvariable=self.orion_path_var, width=40).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.input_frame, text="Buscar", command=self.select_orion).grid(row=2, column=2, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Directorio de salida:").grid(row=3, column=0, sticky="e", pady=5)
        ttk.Entry(self.input_frame, textvariable=self.output_dir_var, width=40).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(self.input_frame, text="Seleccionar", command=self.select_directory).grid(row=3, column=2, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Nombre del archivo de salida:").grid(row=4, column=0, sticky="e", pady=5)
        ttk.Entry(self.input_frame, textvariable=self.output_name_var, width=40).grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(self.input_frame, text="Ejecutar", command=self.run).grid(row=5, column=0, columnspan=3, pady=20)

    def select_maestra(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        if file_path:
            self.maestra_path_var.set(file_path)

    def select_orion(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        if file_path:
            self.orion_path_var.set(file_path)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir_var.set(directory)

    def run(self):
        maestra_path = self.maestra_path_var.get()
        orion_path = self.orion_path_var.get()
        output_dir = self.output_dir_var.get()
        output_name = self.output_name_var.get()
        output_path = f"{output_dir}/{output_name}.xlsx"

        if not maestra_path or not orion_path or not output_dir or not output_name:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return
        
        try:
            constructor = Constructor(self.input_path, output_path, maestra_path, orion_path, self.bd_ila_path)
            constructor.execute()
            messagebox.showinfo("Éxito", f"Archivo generado en: {output_path}")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def show(self):
        self.root.mainloop()

    def get_input_path(self):
        return self.input_path

    def get_bd_ila_path(self):
        return self.bd_ila_path    

if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    menu.show()