from datetime import datetime
#------------------------------------------------------------------------------------
def validate_Product():#
    while True:
        product = input("Ingrese el numero identificador del producto (solo números positivos, no inicia en 0, mínimo 3 digitos o si deseas cancelar solo escribe: cancel): ").strip()

        if product == "cancel":
            print("\033[91mProceso cancelado\033[0m")
            break
        elif not product.isdigit():
            print("Error: El documento debe contener solo números.")
        elif product.startswith('0'):
            print("Error: El documento no debe comenzar con 0.")
        elif len(product) < 3:
            print("Error: El documento debe tener al menos 3 digitos.")
        else:
            return product
#------------------------------------------------------------------------------------
"""Valida que el numero identificador ingresado cumpla con los requisitos minimos (numeros positivos, sin ceros iniciales, minimo 3 digitos, ningun tipo de caracter)."""
def register(inventory,product_Identifier):
    author = input("Enter author: ").strip().lower()
    product_name = input("Enter product name: ").strip().lower()
    category= input("Enter category: ").strip().lower()


    while not author or not product_name or not category:
        print("Los espacios no pueden estar vacios.")
        author = input("Enter author: ").strip().lower()
        product_name = input("Enter product name: ").strip().lower()
        category= input("Enter category").strip().lower()
    while True:
        try:
            
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            
            if price <=0 or stock <=0:
                print("Valores invalidos,No pueden ser negativos y la cantidad debe ser un numero entero")
            
            else:
                inventory[product_Identifier] = {
                    "product": product_name,
                    "author": author,
                    "categoria": category,
                    "price": price,
                    "stock": stock }
                print("\n\033[92mProceso realizado correctamente.\033[0m")
                break
        except ValueError:
            print("datos invalidos, no pueden haber espacios vacios, la cantidad debe ser un numero entero positivo.")

#------------------------------------------------------------------------------------
"""Valida que el producto se encuentre en el inventario y si lo esta muestra todos sus datos"""
def show_products(inventory,consult_product):
    if not consult_product in inventory:
        print("\033[91mElproducto no esta registrado.\033[0m")
    else:
        total= inventory[consult_product]['price'] * inventory[consult_product]['stock']
        print(f"\nId: {consult_product}")
        print(f"Author: {inventory[consult_product]['author']}")
        print(f"Product: {inventory[consult_product]['product']}")
        print(f"category: {inventory[consult_product]['category']}")
        print(f"Price: {inventory[consult_product]['price']}")
        print(f"Stock: {inventory[consult_product]['stock']}")

        print(f'Total value in the products: {total:.2f}')
#------------------------------------------------------------------------------------
"""Valida que el producto este en el inventario y si lo esta llama a la funcion "register()" para actualizar"""
def update_Products(inventory,update_product):
    if not update_product in inventory:
        print("\033[91mElproducto no esta registrado.\033[0m")
    else:
        register(inventory,update_product)
#------------------------------------------------------------------------------------
#Elimina completamente un producto del sistema.
def delete_product(inventory,delete):
    if not delete in inventory:
        print("\033[91mElproducto no esta registrado.\033[0m")
    else:
        print(f'\033[92mEl producto "{inventory[delete]['product']}" se elimino correctamente.\033[0m')
        inventory.pop(delete)
#------------------------------------------------------------------------------------

quantity_discount = 3
percentage_discount = 0.1

def register_Sale(inventory, id_product):
    if not id_product in inventory:
        print("\033[91mEl producto no está registrado.\033[0m")
    else:
        try:
            customer = input("Ingrese cliente: ").strip().lower()
            stock = int(input("Ingrese cantidad a vender: "))

            while not customer:
                print("El nombre del cliente no puede estar vacío.")
                customer = input("Ingrese cliente: ").strip().lower()
                stock = int(input("Ingrese cantidad a vender: "))

            if stock <= 0:
                print("La cantidad debe ser mayor a 0")
            elif stock > inventory[id_product]["stock"]:
                print("No hay suficiente stock disponible.")
                return
            else:
                # Descontar stock vendido
                inventory[id_product]["stock"] -= stock

                unit_price = inventory[id_product]["price"]
                total_gross = unit_price * stock

                apply_discount = ""
                if stock >= quantity_discount:
                    apply_discount = "yes"
                else:
                    apply_discount = "No"

                # Calcular descuento solo si aplica
                if apply_discount == "yes":
                    discount = total_gross * percentage_discount
                else:
                    discount = 0

                total_neto = total_gross - discount

                # Guardar la venta
                sale = {
                    "customer": customer,
                    "producto_id": id_product,
                    "stock": stock,
                    "fecha": datetime.now().strftime("%Y-%m-%d"),
                    "apply_discount": apply_discount,
                    "total_gross": total_gross,
                    "total_neto": total_neto
                }
                sales.append(sale)
                print("Venta registrada correctamente.")
        except ValueError:
            print("Error: datos no válidos.")
#------------------------------------------------------------------------------------------
#Muestra todas las ventas realizadas
def show_sales(sales):

    if len(sales) == 0:
        print("No hay ventas registradas")
    else:
        print("--- Lista de Ventas Registradas ---")
        for sale in sales:
            product = inventory[sale["producto_id"]]
            print(f"Cliente: {sale['customer']} | Producto: {product['product']} | "
                f"Cantidad: {sale['stock']} | Fecha: {sale['fecha']} | "
                f"Descuento: {sale['apply_discount']} | "
                f"Ingreso Bruto: {sale['total_gross']:.2f} | Ingreso Neto: {sale['total_neto']:.2f}")




inventory= {
    "123":{"author":"adrian","product":"arroz","price":1000,"stock":10, "category": "grain"},
    "456":{"author":"alesis","product":"papa","price":1500,"stock":50, "category": "vegetables"},
    "789":{"author":"alex","product":"azucar","price":2000,"stock":15, "category": "grain"},
    "987":{"author":"maria","product":"leche","price":2500,"stock":20, "category": "dairy"},
    "654":{"author":"kate","product":"panela","price":300,"stock":25, "category": "grain"},
}

sales= []
#------------------------------------------------------------------------------------
while True:
    print("\n\033[92m-----------------inventory management-------------\033[0m\n")
    print("\033[94mMAIN MENU.\033[0m\n")
    print("1- Register product.")
    print("2- Query product.")
    print("3- Update product.")
    print("4- Delete product.")
    print("5- Register sale.")
    print("6. show sales")
    print("7- Exit the program.\n")
    
    option = input("\033[93mEnter the number between 1 and 5, of the option you wish to perform: \033[0m")

    
    match option:
            case "1":
                print("\n\033[94mRegister product.\033[0m")
                product_Identifier= validate_Product()

                if product_Identifier not in inventory and product_Identifier != None :
                    register(inventory, product_Identifier)
                    

                elif product_Identifier in inventory:
                    print("\033[91mEl producto ya está registrado.\033[0m")
                    
            case "2":
                print("\n\033[94mQuery product.\033[0m")
                consult_product = validate_Product()
                if consult_product!= None:
                    show_products(inventory,consult_product)
                    

            case "3":
                print("\n\033[94mUpdate product.\033[0m")
                update_product= validate_Product()
                if update_product!= None:
                    update_Products(inventory,update_product)

            case "4":
                print("\n\033[94mDelete product.\033[0m")
                delete= validate_Product()
                if delete != None:
                    delete_product(inventory,delete)

            case "5":
                print("\n\033[94mRegister sale.\033[0m")
                id_product= validate_Product()
                if id_product != None:
                    register_Sale(inventory,id_product)

            case "6":
                show_sales(sales)

            case "7":
                print("\n\033[94mThank you for using the program. \n"
                "See you soon\033[0m")
                break
        
            case _ :
                print("\n\033[91m Invalid option.\033[0m \n")