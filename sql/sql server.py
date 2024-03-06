import sqlite3

# Crear conexión
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS productos
               (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL, stock INTEGER)''')
conn.commit()

# Insertar datos
productos = [
    ('producto A', 50.0, 100),
    ('producto B', 70.0, 80),
    ('producto C', 60.0, 120),
    ('producto D', 90.0, 60),
    ('producto E', 55.0, 150)    
]
cursor.executemany('INSERT INTO productos (nombre, precio, stock) VALUES (?,?,?)', productos)
conn.commit()

# Consultar datos
cursor.execute('SELECT * FROM productos WHERE precio > 50')
resultados = cursor.fetchall()
print("Productos con precios superiores a $50:")
for producto in resultados:
    print(producto)

# Actualizar datos
cursor.execute('UPDATE productos SET precio = 80.0 WHERE id = 1')
conn.commit()
print("Precio actualizado para el producto A")

# Eliminar datos
cursor.execute('DELETE FROM productos WHERE id = 2')
conn.commit()
print("Producto B eliminado de la base de datos productos")

# Cerrar conexión
conn.close()