import tkinter as tk
from tkinter import *
from tkinter import font



class Menu:
    def __init__(self,ventana): #En esta funcion se ve el programa principal
        self.inventario={} #inventario donde se van a guardar los productos
        
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
        
        self.button = tk.Button(self.frame, text="Guardar",command=self.guardarEnInventario,  bg="#9B59B6", fg="white", width=20, font=boton_font) #Se le da el comando al boton de que guarde en el inventario lo ingresado
        self.button.pack(pady=5)
       
       #Cuando se presione el boton de "Volver", se procederá a cerrar la ventana 
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaProducto.destroy,  bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.Volver.pack()
        
    
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
        
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarDescripcion, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5) 
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaDescripcion.destroy, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.Volver.pack() 
    
    
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
        
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarMarca, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5) 
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaMarca.destroy, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.Volver.pack()
    
    
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
        
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarStock, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5) 
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaStock.destroy, bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.Volver.pack() 
    
         
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
        
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarPrecio,bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.guardar.pack(pady=5)
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaPrecio.destroy,bg="#9B59B6", fg="white", width=20, font=boton_font)
        self.Volver.pack()      


    def guardarEnInventario(self): #Funcion para guardar en el inventario
        codigo = self.entry.get() #Obtiene el contenido del campo de entrada de texto
        descripcion = self.entry1.get()
        marca = self.entry2.get()
        stock = int(self.entry3.get())
        precio = float(self.entry4.get())
        
        self.entry.delete(0, tk.END) #.delete() sirve para eliminar la entrada de texto luego de guardar los datos
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        
        if codigo in self.inventario: #Evaluamos que no se repitan los codigos de los productos
            print("El codigo ya existe en el inventario")
        else:
            self.inventario[codigo] = {"Descripción": descripcion,"Marca": marca ,"Stock": stock, "Precio": precio}
            print("Producto cargado con éxito") #guardamos el codigo con sus respectivos datos

    def actualizarDescripcion(self): #Funcion para actualizar la descripcion
        codigo = self.entry.get() #Se toman los datos del campo de codigo
        nueva_desc = self.entry1.get() #Se toman los datos del campo de la descripción
        
        #Se evalua si el codigo existe en el inventario, de ser asi. Se actualiza con los nuevos datos
        if codigo in self.inventario: 
            self.inventario[codigo]["Descripción"] = nueva_desc
            print("La nueva descripcion del producto es:", nueva_desc)
        else:
            print("Código no encontrado en el inventario")
        
        self.entry.delete(0, tk.END)
        self.entry1.delete(0, tk.END)
    
    def actualizarMarca(self):
        codigo = self.entry.get()
        nueva_marca = self.entry2.get()
        
        if codigo in self.inventario:
            self.inventario[codigo]["Marca"] = nueva_marca
            print("La nueva marca del producto es:", nueva_marca)
        else:
            print("Código no encontrado en el inventario")

        self.entry.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        
    def actualizarStock(self):
        codigo = self.entry.get()
        nuevo_stock = self.entry3.get()
        
        if codigo in self.inventario:
            self.inventario[codigo]["Stock"] = nuevo_stock
            print("El nuevo stock del producto es:", nuevo_stock)
        else:
            print("Código no encontrado en el inventario")
    
        self.entry.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
    
    def actualizarPrecio(self):
        codigo = self.entry.get()
        nuevo_precio = self.entry4.get()
        
        if codigo in self.inventario:
            self.inventario[codigo]["Precio"] = nuevo_precio
            print("El nuevo precio del producto es:", nuevo_precio)
        else:
            print("Código no encontrado en el inventario")
    
        self.entry.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
    
    
    def mostrarInventario(self): #Mostramos el inventario
        for codigo, detalles in self.inventario.items():
            print(f"Código: {codigo}")
            print(f"Descripción: {detalles['Descripción']}")
            print(f"Marca: {detalles['Marca']}")
            print(f"Stock: {detalles['Stock']}")
            print(f"Precio: {detalles['Precio']}")
            print()
        
     #Se imprime por pantalla los datos del diccionario
     

#Se inicializa el programa     
ventana=tk.Tk()
app=Menu(ventana)
ventana.mainloop()
