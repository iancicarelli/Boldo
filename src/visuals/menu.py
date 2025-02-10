from ttkthemes import ThemedTk
from utils.constructor import Constructor
from tkinter import Label, Button, Entry, filedialog, StringVar
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import os

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("BOLDO")
        self.root.geometry("700x400")
        self.root.tk.call("source", "C:/Users/HP/Desktop/BoldoGit/Boldo/src/visuals/themes/forest-light.tcl")
        self.root.tk.call("ttk::style", "theme", "use", "forest-light")
        ttk.Style().theme_use("forest-light")
        
        # Rutas fijas
        self.input_path = r"C:/Users/HP/Desktop/BoldoGit/Boldo/src/data/sheets12.xlsx"
        self.bd_ila_path = r"C:/Users/HP/Desktop/BoldoGit/Boldo/src/data/BDilas.xlsx"
        
        self.create_widgets()
        
    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.input_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.input_frame, text="Configuración")

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

if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    menu.show()