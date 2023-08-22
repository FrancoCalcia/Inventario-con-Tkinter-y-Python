import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import sqlite3


class Menu:
    def __init__(self,ventana): #En esta funcion se ve el programa principal
        self.inventario={} #inventario donde se van a guardar los productos
        
        
        #conectar y crear la BDD
        self.conexion=sqlite3.connect("inventario.db")
        #self.conexion.commit()
        self.cursor=self.conexion.cursor()
        
         # Verificar si la tabla ya existe
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventario';")
        table_exists = self.cursor.fetchone()

        if not table_exists:
            self.cursor.execute(    
                '''CREATE TABLE inventario (
                        codigo text primary key,
                        descripción text,
                        marca text,
                        stock integer,
                        precio real
                    )''' 
            )
            #self.conexion.close()
        self.conexion.commit()
        
        self.cursor.execute("SELECT * FROM inventario")
        db_data = self.cursor.fetchall()
        for row in db_data:
            codigo, descripcion, marca, stock, precio = row
            self.inventario[codigo] = {
                "Descripción": descripcion,
                "Marca": marca,
                "Stock": stock,
                "Precio": precio
            }
        
        
        self.ventana=ventana
        self.ventana.title("Inventario de productos") #nombre de la ventana
        self.ventana.configure(bg="black")  # Fondo negro para la ventana
        titulo_font = font.Font(family="Helvetica", size=20, weight="bold")
        boton_font = font.Font(family="Helvetica", size=12)
        
        # Frame para el título
        titulo_frame = tk.Frame(self.ventana, bg="black")
        titulo_frame.pack(pady=20) #ubicacion del titulo

        #diseño del titulo
        titulo_label = tk.Label(titulo_frame, text="Gestión de Productos", bg="black", fg="white", font=titulo_font)
        titulo_label.pack()
        
        
        #frame de los botones
        self.frame1 = tk.Frame(self.ventana, bg="black") #Frame sirve para contener a los widgets
        self.frame1.pack(padx=90, pady=60) #Esta es la dimension del contenedor
        
        #De aca en adelante se van a crear los botones donde si se presionan te redirije a la
        #ventana de cada uno
        
        
        self.AgrProd = tk.Button(self.frame1, text="Agregar Producto",command=self.AgregarProducto, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.AgrProd.pack(padx=20,pady=10)
        
        self.MostDesc=tk.Button(self.frame1, text="Actualizar la descripción", command=self.GUIDescripcion, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.MostDesc.pack(padx=20,pady=10)
        
        self.MostMarc=tk.Button(self.frame1, text="Actualizar la marca", command=self.GUIMarca, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.MostMarc.pack(padx=20,pady=10)
        
        self.ActStock = tk.Button(self.frame1, text="Actualizar el stock",command=self.GUIStock, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.ActStock.pack(padx=20,pady=10)
        
        self.ActPrecio = tk.Button(self.frame1, text="Actualizar el precio",command=self.GUIPrecio, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.ActPrecio.pack(padx=20,pady=10)
        
        self.MostInven=tk.Button(self.frame1, text="Eliminar producto", command=self.GUIEliminar, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.MostInven.pack(padx=20,pady=10)
        
        self.MostInven=tk.Button(self.frame1, text="Mostrar Inventario", command=self.mostrarInventario, bg="#D161FF", width=20, font=boton_font, fg="white")
        self.MostInven.pack(padx=20,pady=10)
        
    
    
     
    def AgregarProducto(self): #Funcion donde se van a poder crear los productos
        
        self.ventanaProducto= Toplevel() #Toplevel sirve para la creacion de otra ventana
        self.ventanaProducto.title("Agregar productos") #nombre de productos
        self.ventanaProducto.configure(bg="black")
        
        self.frame = tk.Frame(self.ventanaProducto, bg="#D161FF") 
        self.frame.pack(padx=90, pady=60)
        
        label_font = font.Font(family="Helvetica", size=12)
        entry_font = font.Font(family="Helvetica", size=10)
        boton_font = font.Font(family="Helvetica", size=10) 

        self.codigo=tk.Label(self.frame, text="Código del producto", bg="#AF7AC5", fg="white", font=label_font) #Crea una etiqueta
        self.entry = tk.Entry(self.frame, font=entry_font) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #.pack() sirve para empaquetar los widgets
        
        
        self.descripcion=tk.Label(self.frame, text="Descripción",bg="#AF7AC5", fg="white", font=label_font) 
        self.entry1 = tk.Entry(self.frame, font=entry_font) 
        self.descripcion.pack()
        self.entry1.pack() 
        
        
        self.marca=tk.Label(self.frame, text="Marca", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry2 = tk.Entry(self.frame,font=entry_font) 
        self.marca.pack()
        self.entry2.pack() 
        
        
        self.stock=tk.Label(self.frame, text="Stock", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry3 = tk.Entry(self.frame, font=entry_font) 
        self.stock.pack()
        self.entry3.pack() 
        
        
        self.precio=tk.Label(self.frame, text="Precio", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry4 = tk.Entry(self.frame, font=entry_font)
        self.precio.pack()
        self.entry4.pack()  
        
        self.button = tk.Button(self.frame, text="Guardar cambios",command=self.guardarEnInventario,  bg="#9B59B6", fg="white", width=20, font=boton_font) #Se le da el comando al boton de que guarde en el inventario lo ingresado
        self.button.pack(pady=5)
       
       #Cuando se presione el boton de "Cerrar", se procederá a cerrar la ventana 
        self.Cerrar = tk.Button(self.frame, text="Cerrar",command=self.ventanaProducto.destroy,  bg="#C00C0C", fg="white", width=20, font=boton_font)
        self.Cerrar.pack()
        
    
    def GUIDescripcion(self): #GUI para actualizar la descripcion
        self.ventanaDescripcion= Toplevel()
        self.ventanaDescripcion.title("Actualizar la descripción")
        self.ventanaDescripcion.configure(bg="black")
        
        self.frame = tk.Frame(self.ventanaDescripcion, bg="#D161FF") 
        self.frame.pack(padx=90, pady=60)

        label_font = font.Font(family="Helvetica", size=12)
        entry_font = font.Font(family="Helvetica", size=10)
        boton_font = font.Font(family="Helvetica", size=10) 
        
        self.codigo=tk.Label(self.frame, text="Código del producto", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry = tk.Entry(self.frame, font=entry_font) 
        self.codigo.pack()
        self.entry.pack()
        
        self.precio=tk.Label(self.frame, text="Nueva descripción", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry1 = tk.Entry(self.frame, font=entry_font)
        self.precio.pack() 
        self.entry1.pack()
        
        self.guardar = tk.Button(self.frame, text="Guardar cambios",command=self.actualizarDescripcion, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5) 
        
        self.Cerrar = tk.Button(self.frame, text="Cerrar",command=self.ventanaDescripcion.destroy, bg="#C00C0C", fg="white", width=20, font=boton_font)
        self.Cerrar.pack() 
    
    
    def GUIMarca(self): #GUI para actualizar la marca
        self.ventanaMarca= Toplevel()
        self.ventanaMarca.title("Actualizar la marca")
        self.ventanaMarca.configure(bg="black")
        
        self.frame = tk.Frame(self.ventanaMarca, bg="#D161FF") 
        self.frame.pack(padx=90, pady=60) 

        label_font = font.Font(family="Helvetica", size=12)
        entry_font = font.Font(family="Helvetica", size=10)
        boton_font = font.Font(family="Helvetica", size=10) 

        self.codigo=tk.Label(self.frame, text="Código del producto", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry = tk.Entry(self.frame, font=entry_font) 
        self.codigo.pack()
        self.entry.pack() 
        
        self.precio=tk.Label(self.frame, text="Nueva marca", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry2 = tk.Entry(self.frame, font=entry_font)
        self.precio.pack() 
        self.entry2.pack()
        
        self.guardar = tk.Button(self.frame, text="Guardar cambios",command=self.actualizarMarca, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5) 
        
        self.Cerrar = tk.Button(self.frame, text="Cerrar",command=self.ventanaMarca.destroy, bg="#C00C0C", fg="white", width=20, font=boton_font)
        self.Cerrar.pack()
    
    
    def GUIStock(self): #GUI para actualizar el Stock
        self.ventanaStock= Toplevel()
        self.ventanaStock.title("Actualizar Stock")
        self.ventanaStock.configure(bg="black")
        
        self.frame = tk.Frame(self.ventanaStock, bg="#D161FF")
        self.frame.pack(padx=90, pady=60)
        
        label_font = font.Font(family="Helvetica", size=12)
        entry_font = font.Font(family="Helvetica", size=10)
        boton_font = font.Font(family="Helvetica", size=10) 

        self.codigo=tk.Label(self.frame, text="Código del producto", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry = tk.Entry(self.frame, font= entry_font) 
        self.codigo.pack()
        self.entry.pack() 
        
        self.precio=tk.Label(self.frame, text="Nuevo stock",  bg="#AF7AC5", fg="white", font=label_font) 
        self.entry3 = tk.Entry(self.frame, font=entry_font)
        self.precio.pack() 
        self.entry3.pack()
        
        self.guardar = tk.Button(self.frame, text="Guardar cambios",command=self.actualizarStock, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5) 
        
        self.Cerrar = tk.Button(self.frame, text="Cerrar",command=self.ventanaStock.destroy, bg="#C00C0C", fg="white", width=20, font=boton_font)
        self.Cerrar.pack() 
    
         
    def GUIPrecio(self): #GUI para actualizar el precio
        self.ventanaPrecio= Toplevel()
        self.ventanaPrecio.title("Actualizar precio")
        self.ventanaPrecio.configure(bg="black")
        
        label_font = font.Font(family="Helvetica", size=12)
        entry_font = font.Font(family="Helvetica", size=10)
        boton_font = font.Font(family="Helvetica", size=10)
        
        self.frame = tk.Frame(self.ventanaPrecio, bg="#D161FF") 
        self.frame.pack(padx=90, pady=60) 

        self.codigo=tk.Label(self.frame, text="Código del producto", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry = tk.Entry(self.frame,font=entry_font) 
        self.codigo.pack()
        self.entry.pack() 
        
        self.precio=tk.Label(self.frame, text="Nuevo precio", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry4 = tk.Entry(self.frame,font=entry_font)
        self.precio.pack() 
        self.entry4.pack()
        
        self.guardar = tk.Button(self.frame, text="Guardar cambios",command=self.actualizarPrecio,bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5)
        
        self.Cerrar = tk.Button(self.frame, text="Cerrar",command=self.ventanaPrecio.destroy,bg="#C00C0C", fg="white", width=20, font=boton_font)
        self.Cerrar.pack()
        
    def GUIEliminar(self):
        self.ventanaEliminar= Toplevel()
        self.ventanaEliminar.title("Eliminar producto")
        self.ventanaEliminar.configure(bg="black")
        
        label_font = font.Font(family="Helvetica", size=12)
        entry_font = font.Font(family="Helvetica", size=10)
        boton_font = font.Font(family="Helvetica", size=10)
        
        self.frame = tk.Frame(self.ventanaEliminar, bg="#D161FF") 
        self.frame.pack(padx=90, pady=60) 

        self.codigo=tk.Label(self.frame, text="Código del producto", bg="#AF7AC5", fg="white", font=label_font) 
        self.entry = tk.Entry(self.frame,font=entry_font) 
        self.codigo.pack()
        self.entry.pack() 
        
        self.guardar = tk.Button(self.frame, text="Guardar cambios",command=self.eliminarProducto,bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5)
        
        self.Cerrar = tk.Button(self.frame, text="Cerrar",command=self.ventanaEliminar.destroy,bg="#C00C0C", fg="white", width=20, font=boton_font)
        self.Cerrar.pack()

                
    def guardarEnInventario(self): #Funcion para guardar en el inventario
        codigo = self.entry.get() #Obtiene el contenido del campo de entrada de texto
        descripcion = self.entry1.get()
        marca = self.entry2.get()
        stock = self.entry3.get()
        precio = self.entry4.get()

        
        #en este caso lo que hago es evaluar si la entrada de precio y stock
        #son numeros int o float. En caso de no ser asi con el ValueError lo que
        # hago es que no me imprima el error por pantalla
        try:
            stock1 = int(stock)
        except ValueError:
            stock1 = None
            
        try:
            precio1 = float(precio)
        except ValueError:
            precio1 = None
        
        self.entry.delete(0, tk.END) #.delete() sirve para eliminar la entrada de texto luego de guardar los datos
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        
        if codigo in self.inventario: #Evaluamos que no se repitan los codigos de los productos y si el ingreso de stock y precio es correcto.
            messagebox.showinfo("Error", "El codigo ya existe en el inventario")
        elif stock1 == None:
            messagebox.showinfo("Error", "Ingrese el stock correcto")
        elif precio1 == None:
            messagebox.showinfo("Error", "Ingrese el precio correcto")   
        else:
            self.inventario[codigo] = {"Descripción": descripcion,"Marca": marca ,"Stock": stock, "Precio": precio}
            messagebox.showinfo("Éxito", "Producto cargado con éxito") #guardamos el codigo con sus respectivos datos

            self.cursor=self.conexion.cursor()
            self.cursor.execute('INSERT INTO inventario (Codigo, Descripción, Marca, Stock, Precio) VALUES (?,?,?,?,?)',(codigo,descripcion,marca,stock,precio))
            self.conexion.commit()
            
    
    def actualizarDescripcion(self): #Funcion para actualizar la descripcion
        codigo = self.entry.get() #Se toman los datos del campo de codigo
        nueva_desc = self.entry1.get() #Se toman los datos del campo de la descripción
        
        #Se evalua si el codigo existe en el inventario, de ser asi. Se actualiza con los nuevos datos
        if codigo in self.inventario: 
            self.inventario[codigo]["Descripción"] = nueva_desc
            messagebox.showinfo("Éxito",f"La nueva descripción del producto es: {nueva_desc}")
            self.cursor.execute("UPDATE inventario SET Descripción = ? WHERE Codigo = ?", (nueva_desc,codigo))
            self.conexion.commit()
            self.ventanaDescripcion.destroy()# Cierra la ventana
        else:
            messagebox.showinfo("Error", "El código no existe en el inventario")
            self.entry.delete(0, tk.END)
    
    def actualizarMarca(self):
        codigo = self.entry.get()
        nueva_marca = self.entry2.get()
        
        if codigo in self.inventario:
            self.inventario[codigo]["Marca"] = nueva_marca
            messagebox.showinfo("Éxito",f"La nueva marca del producto es: {nueva_marca}")
            self.cursor.execute("UPDATE inventario SET Marca = ? WHERE Codigo = ?", (nueva_marca,codigo))
            self.conexion.commit()
            self.ventanaMarca.destroy()  # Cierra la ventana
        else:
            messagebox.showinfo("Error", "El código no existe en el inventario")
            self.entry.delete(0, tk.END)

        
    def actualizarStock(self):
        codigo = self.entry.get()
        try:
            nuevo_stock = int(self.entry3.get())
        except ValueError:
            nuevo_stock = None
        
        if nuevo_stock == None:
            messagebox.showinfo("Error", "Ingrese el stock correcto")
            self.entry3.delete(0, tk.END)
        elif codigo in self.inventario:
            self.inventario[codigo]["Stock"] = nuevo_stock
            messagebox.showinfo("Éxito",f"El nuevo stock del producto es: {nuevo_stock}")
            self.cursor.execute("UPDATE inventario SET Stock = ? WHERE Codigo = ?", (nuevo_stock,codigo))
            self.conexion.commit()
            self.ventanaStock.destroy()  # Cierra la ventana
        else:
            messagebox.showinfo("Error", "El código no existe en el inventario")
            self.entry.delete(0, tk.END)
        
    
    def actualizarPrecio(self):
        codigo = self.entry.get()
        try:
            nuevo_precio = float(self.entry4.get())
        except ValueError:
            nuevo_precio = None
        
        if nuevo_precio == None:
            messagebox.showinfo("Error", "Ingrese el precio correcto")
            self.entry4.delete(0, tk.END)
        elif codigo in self.inventario:
            self.inventario[codigo]["Precio"] = nuevo_precio
            messagebox.showinfo("Éxito",f"El nuevo precio del producto es: {nuevo_precio}")
            self.cursor.execute("UPDATE inventario SET Precio = ? WHERE Codigo = ?", (nuevo_precio,codigo))
            self.conexion.commit()
            self.ventanaPrecio.destroy()  # Cierra la ventana
        else:
            messagebox.showinfo("Error", "El código no existe en el inventario")
            self.entry.delete(0, tk.END)
    
    def eliminarProducto(self):
        codigo = self.entry.get()
        if codigo in self.inventario: #Evaluamos que no se repitan los codigos de los productos y si el ingreso de stock y precio es correcto.
            del self.inventario[codigo]
            messagebox.showinfo("Éxito", "El producto se eliminó correctamente")
            self.cursor.execute("DELETE FROM inventario WHERE Codigo = ?", (codigo,))
            self.conexion.commit()  # Elimina el producto de la base de datos
            
            self.ventanaEliminar.destroy()  # Cierra la ventana de eliminación
        else:
            messagebox.showinfo("Error", "El código no existe en el inventario")
            self.entry.delete(0, tk.END)
    
    def mostrarInventario(self): #Mostramos el inventario
        self.ventanaInventario= Toplevel()
        self.ventanaInventario.title("Inventario")
        self.ventanaInventario.configure(bg="black")
        
        texto=tk.Text(self.ventanaInventario, bg="#AF7AC5", fg="white")
        texto.pack(padx=40, pady=20)
        
        self.cursor.execute("SELECT * FROM inventario")
        rows = self.cursor.fetchall()
        
        for row in rows:
            codigo, descripcion, marca, stock, precio = row
            texto.insert(tk.END, f"Código: {codigo}\n")
            texto.insert(tk.END, f"Descripción: {descripcion}\n")
            texto.insert(tk.END, f"Marca: {marca}\n")
            texto.insert(tk.END, f"Stock: {stock}\n")
            texto.insert(tk.END, f"Precio: {precio}\n\n")
            
        Cerrar_button = tk.Button(self.ventanaInventario, text="Cerrar", command=self.ventanaInventario.destroy,bg="#C00C0C", fg="white", width=10)
        Cerrar_button.pack(pady=15)
     #Se imprime por pantalla los datos del diccionario
     
     

#Se inicializa el programa     
ventana=tk.Tk()
app=Menu(ventana)
ventana.mainloop()
