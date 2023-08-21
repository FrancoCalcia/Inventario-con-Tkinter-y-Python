import tkinter as tk
from tkinter import *



class Menu:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Inventario de productos") #nombre de productos
    
        self.inventario={}
        self.main_frame1 = tk.Frame(self.ventana) #Frame sirve para contener a los widgets
        self.main_frame1.pack(padx=90, pady=60)
        
        self.AgrProd = tk.Button(self.main_frame1, text="Agregar Producto",command=self.AgregarProducto)
        self.AgrProd.pack()
        
        self.MostDesc=tk.Button(self.main_frame1, text="Actualizar la descripción", command=self.GUIDescripcion)
        self.MostDesc.pack()
        
        self.MostMarc=tk.Button(self.main_frame1, text="Actualizar la marca", command=self.GUIMarca)
        self.MostMarc.pack()
        
        self.ActStock = tk.Button(self.main_frame1, text="Actualizar el stock",command=self.GUIStock)
        self.ActStock.pack()
        
        self.ActPrecio = tk.Button(self.main_frame1, text="Actualizar el precio",command=self.GUIPrecio)
        self.ActPrecio.pack()
        
        self.MostInven=tk.Button(self.main_frame1, text="Mostrar Inventario", command=self.mostrarInventario)
        self.MostInven.pack()
     
    def AgregarProducto(self):
        self.ventanaProducto= Toplevel()
        self.ventanaProducto.title("Agregar productos")#nombre de productos
        
        self.frame = tk.Frame(self.ventanaProducto) #Frame sirve para contener a los widgets
        self.frame.pack(padx=90, pady=60) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.frame, text="Código del producto") #Crea una etiqueta
        self.entry = tk.Entry(self.frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        
        self.descripcion=tk.Label(self.frame, text="Descripción") 
        self.entry1 = tk.Entry(self.frame) 
        self.descripcion.pack()
        self.entry1.pack() 
        
        
        self.marca=tk.Label(self.frame, text="Marca") 
        self.entry2 = tk.Entry(self.frame) 
        self.marca.pack()
        self.entry2.pack() 
        
        
        
        self.stock=tk.Label(self.frame, text="Stock") 
        self.entry3 = tk.Entry(self.frame) 
        self.stock.pack()
        self.entry3.pack() 
        
        
        
        self.precio=tk.Label(self.frame, text="Precio") 
        self.entry4 = tk.Entry(self.frame) 
        self.button = tk.Button(self.frame, text="Guardar",command=self.guardarEnInventario) #Se le da el comando al boton de que guarde en el inventario lo ingresado
        self.precio.pack()
        self.entry4.pack() 
        self.button.pack()
       
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaProducto.destroy)
        self.Volver.pack()
        
    
    def guardarEnInventario(self): #Funcion para guardar en el inventario
        codigo = self.entry.get() #Obtiene el contenido del campo de entrada de texto
        descripcion = self.entry1.get()
        marca = self.entry2.get()
        stock = self.entry3.get()
        precio = self.entry4.get()
        
        self.entry.delete(0, tk.END)
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        
        if codigo in self.inventario:
            
            print("El codigo ya existe en el inventario")
        else:
            self.inventario[codigo] = {"Descripción": descripcion,"Marca": marca ,"Stock": stock, "Precio": precio}
            print("Producto cargado con éxito") 


    
    
        
    
    def GUIDescripcion(self):
        self.ventanaDescripcion= Toplevel()
        self.ventanaDescripcion.title("Actualizar la descripción")#nombre de productos
        
        self.frame = tk.Frame(self.ventanaDescripcion) #Frame sirve para contener a los widgets
        self.frame.pack(padx=90, pady=60) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.frame, text="Código del producto") #Crea una etiqueta
        self.entry = tk.Entry(self.frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        self.precio=tk.Label(self.frame, text="Descripción") 
        self.entry1 = tk.Entry(self.frame)
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarDescripcion)
        self.precio.pack() 
        self.entry1.pack()
        self.guardar.pack() 
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaDescripcion.destroy)
        self.Volver.pack() 
    
    def GUIMarca(self):
        self.ventanaMarca= Toplevel()
        self.ventanaMarca.title("Actualizar la marca")#nombre de productos
        
        self.frame = tk.Frame(self.ventanaMarca) #Frame sirve para contener a los widgets
        self.frame.pack(padx=90, pady=60) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.frame, text="Código del producto") #Crea una etiqueta
        self.entry = tk.Entry(self.frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        self.precio=tk.Label(self.frame, text="Marca") 
        self.entry2 = tk.Entry(self.frame)
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarMarca)
        self.precio.pack() 
        self.entry2.pack()
        self.guardar.pack() 
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaMarca.destroy)
        self.Volver.pack()
    
    def GUIStock(self):
        self.ventanaStock= Toplevel()
        self.ventanaStock.title("Actualizar Stock")#nombre de productos
        
        self.frame = tk.Frame(self.ventanaStock) #Frame sirve para contener a los widgets
        self.frame.pack(padx=90, pady=60) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.frame, text="Código del producto") #Crea una etiqueta
        self.entry = tk.Entry(self.frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        self.precio=tk.Label(self.frame, text="Stock") 
        self.entry3 = tk.Entry(self.frame)
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarStock)
        self.precio.pack() 
        self.entry3.pack()
        self.guardar.pack() 
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaStock.destroy)
        self.Volver.pack() 
         
    def GUIPrecio(self):
        self.ventanaPrecio= Toplevel()
        self.ventanaPrecio.title("Actualizar precio")#nombre de productos
        
        self.frame = tk.Frame(self.ventanaPrecio) #Frame sirve para contener a los widgets
        self.frame.pack(padx=90, pady=60) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.frame, text="Código del producto") #Crea una etiqueta
        self.entry = tk.Entry(self.frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        self.precio=tk.Label(self.frame, text="Precio") 
        self.entry4 = tk.Entry(self.frame)
        self.guardar = tk.Button(self.frame, text="Guardar",command=self.actualizarPrecio)
        self.precio.pack() 
        self.entry4.pack()
        self.guardar.pack()
        
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaPrecio.destroy)
        self.Volver.pack()      

    def actualizarDescripcion(self):
        codigo = self.entry.get()
        nueva_desc = self.entry1.get()
        
        if codigo in self.inventario:
            self.inventario[codigo]["Descripción"] = nueva_desc
            print("El nuevo precio del producto es:", nueva_desc)
        else:
            print("Código no encontrado en el inventario")
        
        self.entry.delete(0, tk.END)
        self.entry1.delete(0, tk.END)
    
    def actualizarMarca(self):
        codigo = self.entry.get()
        nueva_marca = self.entry2.get()
        
        if codigo in self.inventario:
            self.inventario[codigo]["Marca"] = nueva_marca
            print("El nuevo precio del producto es:", nueva_marca)
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
    
    
    
    
    def mostrarInventario(self):
        print(self.inventario)
     
ventana=tk.Tk()
app=Menu(ventana)
ventana.mainloop()
