import sqlite3

conexion = sqlite3.connect("sql.db")
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    precioapagar INTEGER,
    numtarjeta INTEGER PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    propina TEXT,
    numtelefono INTEGER
)
''')
conexion.commit()

atributos = ["precioapagar", "numtarjeta", "nombre", "direccion", "propina", "numtelefono"]

def menu():
    while True:
        print('''
--- MENÚ ---
1. Agregar cliente
2. Modificar un campo de un cliente
3. Mostrar todos los clientes
4. Eliminar cliente 
5. Buscar cliente 
6. Salir
''')
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                datos = (
                    int(input("Precio a pagar: ")),
                    int(input("Número de tarjeta: ")),
                    input("Nombre: "),
                    input("Dirección: "),
                    input("¿Propina (si/no)?: "),
                    int(input("Número de teléfono: "))
                )
                cursor.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)", datos)
                conexion.commit()
                print("Cliente agregado.\n")

            case "2":
                campo_busqueda = input("Campo por el que buscar al cliente: ").lower()
                if campo_busqueda not in atributos:
                    print("este campo no es valido")
                    continue
                valor_busqueda = input(f"Valor de '{campo_busqueda}': ")

                campo_modificar = input("Campo que deseas modificar: ").lower()
                if campo_modificar not in atributos:
                    print("Campo no válido.")
                    continue
                nuevo_valor = input(f"Nuevo valor para '{campo_modificar}': ")

                cursor.execute(f"UPDATE clientes SET {campo_modificar}=? WHERE {campo_busqueda}=?", (nuevo_valor, valor_busqueda))
                conexion.commit()
                print("Cliente modificado.\n")

            case "3":
                for cliente in cursor.execute("SELECT * FROM clientes ORDER BY nombre"):
                    print(cliente)

            case "4":
                campo = input("Campo para eliminar cliente: ").lower()
                if campo not in atributos:
                    print("Campo no válido.")
                valor = input(f"Valor de '{campo}': ")
                cursor.execute(f"DELETE FROM clientes WHERE {campo}=?", (valor,))
                conexion.commit()
                print("Cliente eliminado.\n")

            case "5":
                campo = input("Campo por el cual buscar: ").lower()
                if campo not in atributos:
                    print("Campo no válido.")
                    continue
                valor = input(f"Valor de '{campo}': ")
                cursor.execute(f"SELECT * FROM clientes WHERE {campo}=?", (valor,))
                resultados = cursor.fetchall()
                if resultados:
                    for cliente in resultados:
                        print(cliente)
                else:
                    print("No se encontró ningún cliente.\n")

            case "6":
                print("Saliendo...")
                break

            case _:
                print("Opción inválida.")

    conexion.close()

menu()

