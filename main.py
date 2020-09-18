from connection.conn import Conexion
from Productos.productos import Productos

conn = Conexion('mongodb://localhost:27017', 'Productos')

###################################
# Insertar Registros
###################################

# nro_registros = int(input("Por favor introduzca el # de registros que va ingresar: "))

# try:
#     lista_productos = []
#     while True:
#         for i in range(nro_registros):
#             categoria = ""
#             categoria = input("Por favor introduzca la categoría a la cual pertenece su producto: ")
#             nombre = input(f'Ingrese el nombre de su roducto: ')
#             precio = float(input(f'Por favor introduzca el precio del {nombre}: '))
#             cantidad = float(input(f'Por favor introduzca la cantidad {nombre} que va ingresar: '))

#             producto = Productos(nombre, precio, cantidad, categoria)
#             lista_productos.append(producto)

#         if lista_productos:
#             Productos.ingresar_productos(conn, lista_productos)

#         break

# except Exception as e:
#     print(f'{str(e)}')

# finally:
#     pass

###################################
# Generar Registro
###################################

# Productos.generar_registro(conn)

###################################
# Modificar Registro
###################################


print("Bienvenido al mercado de San Miguel")
print("Estos son los productos que tenemos actualmente")
print("################################################")
Productos.generar_registro(conn)
print("################################################")

try:
    lista_productos = []
    while True:
        categoria = ""
        categoria = input("Por favor introduzca la categoría a la cual pertenece su producto: ")
        nombre = input(f'Ingrese el nombre de su roducto: ')
        cantidad = int(input(f'Por favor introduzca la cantidad de {nombre} que va comprar: '))
        precio = 0

        producto = Productos(nombre, precio, cantidad, categoria)
        lista_productos.append(producto)

        if lista_productos:
            Productos.modificar_productos(conn, lista_productos)

        break

except Exception as e:
    print(f'{str(e)}')

finally:
    pass
