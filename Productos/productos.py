import os

class Productos:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    @staticmethod
    def ingresar_productos(conn, data):
        productos_total = []
        for i in data:
            productos = []
            insert = {
                'Producto' : i.nombre,
                'Precio' : i.precio,
                'Cantidad' : i.cantidad
            }
            productos.append(insert)
            productos_total.append(insert)
            conn.insertar_registros(i.categoria, productos)

        if productos_total:
            conn.insertar_registros('Productos', productos_total)
            
    @staticmethod
    def generar_registro(conn):
        productos = conn.obtener_registros('Productos')
        try:
            file = open('productos.txt', 'w')
            fila_productos = ''
            n = 1
            for i in productos:
                fila_productos += f'Nro {n}, Nombre: {i["Producto"]}, Precio: {i["Precio"]}, Cantidad: {i["Cantidad"]}\n'
                n += 1
            file.write(fila_productos)
            print('Se genero el reporte de productos')

        except Exception as e:
            print(f'{str(e)}')
        finally:
            if file:
                file.close()


    @staticmethod
    def modificar_productos(conn, data):
        pass
        try:
            for i in data:
                # print(i.categoria)
                # print(i.nombre)
                # print(i.cantidad)
                conn.actualizar_registro(i.categoria, {
                    'Producto' : i.nombre
                    }, {
                        'Cantidad' : i.cantidad
                    })
        except Exception as e:
            print(f'{str(e)}')

        finally:
            pass