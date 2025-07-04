# Gestión de inventario

Este es un programa interactivo de consola desarrollado en **Python**, diseñado para gestionar un sistema de inventario de una tienda. Permite registrar productos, consultar, actualizar, eliminar, registrar ventas y vizualizar ventas junto con su descuento.


## Requisitos para ejecutar sistema

- Consola o terminal para ejecutar el archivo
- Python 3
- Editor de código recomendado: Visual Studio Code

## Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Interfaz:** Consola
- **Estilo:** Uso de colores para la salida en terminal

-----------------------------------------------------------------------------------

## Cómo ejecutar el programa:

### 1. Clona el repositorio o descarga el archivo

Descarga el archivo `gestion_inventario.py` y guardalo en una carpeta local.

### 2. Ejecutar desde la consola

#### En Windows:
cd /ruta\donde\guardaste\el\archivo
python gestion_inventario.py

#### En Linux :
cd /ruta/donde/guardaste/el/archivo
python3 gestion_inventario.py


### 3. Ejecutar desde Visual Studio Code 

1. Abre VS Code.
2. Ve a `Archivo > Abrir carpeta` y selecciona la carpeta donde está `gestion_inventario.py`.
3. Abre el archivo.
4. Haz clic derecho dentro del código y selecciona “Ejecutar archivo en la terminal” o presiona el boton triangular ubicado arriba a la derecha.

-----------------------------------------------------------------------------------

## Funcionalidades del programa

Al iniciar, se muestra un menú con 7 opciones:

1. **Registrar Producto**  
   - Pide número Identificador de cada producto, nombre de autor, cantidad, precio y categoria.
   - Valida que los datos estén correctamente ingresados.
   - se muestra como debes ingresar los datos, si en caso de ingresar un dato invalido notificara de manera correspondiente.

2. **Consultar producto** 
   - solicita el numero identificador del producto a consultar y lo valida.
   - Muestra todos los datos del producto
   - si el producto no esta registrado, lo notificara.

3. **Actualizar producto**  
   - solicita el numero identificador del producto al que se va actualizar y lo valida.
   - Permite ingresar todos los datos del producto nuevamente excepto su identificador
   - si el producto no esta registrado, lo notificara.

4. **Eliminar producto**  
   - solicita el numero identificador del producto a eliminar y lo valida.
   - Elimina del sistema al producto según su numero identificador.
   - si el producto no esta registrado, lo notificara.

5. **Registrar venta**  
   - solicita el numero identificador del producto al registrar la venta
   - valida que se encuentre disponible a la venta

6. **Mostrar ventas**
   - Muestra un registro de todas las ventas realizadas

7. **Salir del programa**  
   - Finaliza la ejecución del programa.
   - muestra un mensaje de despedida.

-----------------------------------------------------------------------------------

## ¿Que hace cada parte en el codigo?

- `inventory`  
  Diccionario principal que almacena los datos. Cada producto se guarda con su numero de numero identificador como clave.

- `validate_Product()`  
  Valida que el numero identificador ingresado cumpla con los requisitos minimos (numeros positivos, sin ceros iniciales, minimo 3 digitos, ningun tipo de caracter).

- `show_products(inventory,consult_product)`
  Valida que el producto se encuentre en el inventario y si lo esta muestra todos sus datos

- `update_Products(inventory,update_product)`  
  Valida que el producto este en el inventario y si lo esta llama a la funcion "register()" para actualizar

- `delete_product(inventory,delete)`  
  Elimina completamente un producto del sistema.

- `show_sales(sales)`  
  Muestra todas las ventas realizadas.

- `register_Sale(inventory, id_product):`  
  Realiza el registro de cada venta 

- `while True:`  
  Bucle principal que muestra el menu e invoca las funciones segun la opción elegida.

-----------------------------------------------------------------------------------

##  Detalles adicionales

  - Se usan **colores en la consola** para mejorar la experiencia del usuario:
  - Verde: acciones exitosas
  - Rojo: errores o advertencias
  - azul: opcion elegida
  - Amarillo: informacion o instrucciones

- El sistema incluye **validaciones exhaustivas** para evitar errores comunes en la entrada del usuario.
- Totalmente funcional y ejecutable completamente desde consola.

-----------------------------------------------------------------------------------

## Autor

Este programa fue desarrollado por **Adrian Arboleda**# gestion_inventario
