# Boldo

**Boldo Data Processor** es una aplicación de escritorio diseñada para manejar y procesar datos en formato Excel, específicamente enfocada en la creación de listas de costos para el sistema Orion. Desarrollada en Python y utilizando la librería `ttkthemes`, Boldo ofrece una interfaz intuitiva y funcionalidades robustas para la gestión de datos.

## Funcionamiento

### Maestra

La **Maestra** es un archivo Excel que contiene la información esencial de los productos necesaria para generar una lista de costos. Este archivo incluye los siguientes campos:

- **Código de barras**: Identificador único del producto.
- **Nombre del producto**: Descripción del producto.
- **Código del proveedor**: Identificador del proveedor asociado al producto.
- **Unidad por embalaje (UxE)**: Cantidad de unidades por embalaje.
- **Precio en bruto**: Precio base del producto antes de aplicar cualquier cálculo.

Estos valores son fundamentales para que Boldo pueda generar una lista de costos precisa y actualizada.

![imagen](https://github.com/iancicarelli/Boldo/blob/main/img/maestraFormato.png)

### BD Orion

La **BD Orion** es una base de datos exportada desde el sistema Orion, que contiene todos los productos registrados en dicho sistema. Dado que Orion exporta los datos en formato Excel, Boldo utiliza este archivo para realizar comparaciones y actualizaciones. Es importante mantener esta base de datos actualizada, ya que nuevos productos se añaden constantemente al sistema Orion. Como Boldo funciona sin conexión, es necesario descargar y actualizar manualmente la BD Orion para incluir los nuevos productos.

![imagen](https://github.com/iancicarelli/Boldo/blob/main/img/ProductosBDFormato.png)

### Interfaz

La interfaz de Boldo fue desarrollada utilizando `ttkthemes`, una librería de Python que permite crear interfaces gráficas modernas y personalizables. La interfaz de Boldo cuenta con las siguientes características:

![interfaz](https://github.com/iancicarelli/Boldo/blob/main/img/interfaz.png)

1. **Búsqueda de archivos**:
   - **Primer campo**: Para seleccionar el archivo de la Maestra.
   - **Segundo campo**: Para seleccionar el archivo de la BD Orion.
   - **Tercer campo**: Para seleccionar el directorio de salida donde se guardará el archivo generado.

2. **Input de nombre de archivo**: Un campo de texto donde el usuario puede ingresar el nombre del archivo de salida.

3. **Botón de procesar**: Un botón que inicia el proceso de generación de la lista de costos una vez que todos los archivos necesarios han sido seleccionados.

### Proceso de generación de listas de costos

Una vez que el usuario ha seleccionado los archivos necesarios y ha ingresado el nombre del archivo de salida, Boldo realiza los siguientes pasos:

1. **Lectura de datos**: Boldo lee los datos de la Maestra y la BD Orion.
2. **Comparación de productos**: Compara los productos de la Maestra con los de la BD Orion para identificar coincidencias y diferencias.
3. **Cálculo de costos**: Aplica los cálculos necesarios para generar los precios finales de los productos.
4. **Generación del archivo de salida**: Crea un nuevo archivo Excel con la lista de costos actualizada y la guarda en el directorio seleccionado por el usuario.

### Requisitos del sistema

- **Python 3.x**: Boldo está desarrollado en Python, por lo que es necesario tener instalada una versión reciente de Python.
