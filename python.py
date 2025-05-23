clientes = {

    "Ricardo": {

        "precioapagar": 70600,

        "numtarjeta": "4012343357690032",

        "direccion": "Tablada",

        "propina": "no",

        "numtelefono": "3429980032"

    },

    "Natalia": {

        "precioapagar": 10500,

        "numtarjeta": "324488886503592",

        "direccion": "Paladini",

        "propina": "si",

        "numtelefono": "3428889403"

    }

}

 

def agregar_cliente():

    print("\n--- Agregar nuevo cliente ---")

    nombre = input("Nombre: ")

    precioapagar = float(input("Precio a pagar: "))

    numtarjeta = input("Número de tarjeta: ")

    direccion = input("Dirección (barrio): ")

    propina = input("Propina (si/no): ").lower()

    numtelefono = input("Número de teléfono: ")

    

    clientes[nombre] = {

        "precioapagar": precioapagar,

        "numtarjeta": numtarjeta,

        "direccion": direccion,

        "propina": propina,

        "numtelefono": numtelefono

    }

    print(f"\nCliente {nombre} agregado correctamente.")

 

def modificar_cliente():

    print("\n--- Modificar cliente ---")

    nombre = input("Ingrese el nombre del cliente a modificar: ")

    

    if nombre in clientes:

        print("\nDatos actuales del cliente:")

        mostrar_cliente(nombre)

        

        print("\nIngrese los nuevos datos (deje en blanco para mantener el valor actual):")

        precioapagar = input(f"Nuevo precio a pagar [{clientes[nombre]['precioapagar']}]: ")

        numtarjeta = input(f"Nuevo número de tarjeta [{clientes[nombre]['numtarjeta']}]: ")

        direccion = input(f"Nueva dirección [{clientes[nombre]['direccion']}]: ")

        propina = input(f"Nueva propina (si/no) [{clientes[nombre]['propina']}]: ").lower()

        numtelefono = input(f"Nuevo número de teléfono [{clientes[nombre]['numtelefono']}]: ")

        

        if precioapagar:

            clientes[nombre]['precioapagar'] = float(precioapagar)

        if numtarjeta:

            clientes[nombre]['numtarjeta'] = numtarjeta

        if direccion:

            clientes[nombre]['direccion'] = direccion

        if propina:

            clientes[nombre]['propina'] = propina

        if numtelefono:

            clientes[nombre]['numtelefono'] = numtelefono

        

        print("\nCliente modificado correctamente.")

    else:

        print("Cliente no encontrado.")

 

def mostrar_cliente(nombre):

    if nombre in clientes:

        datos = clientes[nombre]

        print(f"\nNombre: {nombre}")

        print(f"Precio a pagar: {datos['precioapagar']}")

        print(f"Número de tarjeta: {datos['numtarjeta']}")

        print(f"Dirección: {datos['direccion']}")

        print(f"Propina: {datos['propina']}")

        print(f"Teléfono: {datos['numtelefono']}")

    else:

        print("Cliente no encontrado.")

 

def mostrar_clientes():

    print("\n--- Listado de clientes ---")

    if clientes:

        for nombre in sorted(clientes.keys()):

            mostrar_cliente(nombre)

            print("----------------------")

    else:

        print("No hay clientes registrados.")

 

def eliminar_cliente():

    print("\n--- Eliminar cliente ---")

    nombre = input("Ingrese el nombre del cliente a eliminar: ")

    

    if nombre in clientes:

        del clientes[nombre]

        print(f"Cliente {nombre} eliminado correctamente.")

    else:

        print("Cliente no encontrado.")

 

def buscar_cliente_por_telefono():

    print("\n--- Buscar cliente por teléfono ---")

    telefono = input("Ingrese el número de teléfono a buscar: ")

    

    encontrados = [nombre for nombre, datos in clientes.items() if datos['numtelefono'] == telefono]

    

    if encontrados:

        for nombre in encontrados:

            mostrar_cliente(nombre)

    else:

        print("No se encontraron clientes con ese número de teléfono.")

 

def menu():

    while True:

        print("\n--- MENÚ PRINCIPAL ---")

        print("1. Agregar cliente")

        print("2. Modificar cliente")

        print("3. Mostrar todos los clientes")

        print("4. Eliminar cliente")

        print("5. Buscar cliente por teléfono")

        print("6. Salir")

        

        opcion = input("Seleccione una opción (1-6): ")

        

        match opcion:

            case "1":

                agregar_cliente()

            case "2":

                modificar_cliente()

            case "3":

                mostrar_clientes()

            case "4":

                eliminar_cliente()

            case "5":

                buscar_cliente_por_telefono()

            case "6":

                print("Saliendo del programa...")

                break

            case _:

                print("Opción inválida. Intente nuevamente.")

 

if __name__ == '__main__':

    menu()