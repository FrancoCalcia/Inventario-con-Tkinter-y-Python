import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Inventario de productos") #nombre de productos
        
        self.main_frame = tk.Frame(self.ventana) #Frame sirve para contener a los widgets
        self.main_frame.pack(padx=20, pady=20)
        
        self.button = tk.Button(self.main_frame, text="Agregar Producto",command=self.AgregarProducto)
        self.button.pack()
        self.button2 = tk.Button(self.main_frame, text="Actualizar Precio",command=self.ActualizarPrecio)
        self.button2.pack()
        
        
    def AgregarProducto(self):
        self.ventana=ventana
        self.ventana.title("Inventario de productos") #nombre de productos
        #self.ventana.geometry("400x300") #ancho y alto de la ventana
        
        self.inventario={} #Definimos el inventario donde se almacenaran los productos
        
        self.main_frame = tk.Frame(self.ventana) #Frame sirve para contener a los widgets
        self.main_frame.pack(padx=20, pady=20) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.main_frame, text="Código del producto") #Crea una etiqueta
        self.entry = tk.Entry(self.main_frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        
        self.descripcion=tk.Label(self.main_frame, text="Descripción") 
        self.entry1 = tk.Entry(self.main_frame) 
        self.descripcion.pack()
        self.entry1.pack() 
        
        
        self.marca=tk.Label(self.main_frame, text="Marca") 
        self.entry2 = tk.Entry(self.main_frame) 
        self.marca.pack()
        self.entry2.pack() 
        
        
        
        self.stock=tk.Label(self.main_frame, text="Stock") 
        self.entry3 = tk.Entry(self.main_frame) 
        self.stock.pack()
        self.entry3.pack() 
        
        
        
        self.precio=tk.Label(self.main_frame, text="Precio") 
        self.entry4 = tk.Entry(self.main_frame) 
        self.button = tk.Button(self.main_frame, text="Guardar",command=self.guardarEnInventario) #Se le da el comando al boton de que guarde en el inventario lo ingresado
        self.precio.pack()
        self.entry4.pack() 
        self.button.pack()
       

        self.precio1=tk.Label(self.main_frame, text="Precio") 
        self.button1 = tk.Button(self.main_frame, text="Guardar",command=self.abrir)
        self.precio1.pack()
        #self.entry4.pack() 
        self.button1.pack()
    
    def ActualizarPrecio(self):
       
        self.precio1=tk.Label(self.main_frame1, text="Precio")
        self.precio1.pack()
        
         
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
        
        self.inventario[codigo] = {"Descripción": descripcion,"Marca": marca ,"Stock": stock, "Precio": precio}  #ds

        print(self.inventario)

    # def actualizarPrecio(self):
    #     if codigo in inventario:
    #         nuevo_precio = self.entry4.get()
    #         self.inventario[codigo]={"Precio": nuevo_precio}
    #     print(self.inventario)
    
#if __name__=="__main__":            
ventana=tk.Tk()
app=App(ventana)
ventana.mainloop()



