import tkinter as tk
from tkinter import ttk, messagebox

class AppWindow(tk.Tk):
    def __init__(self, task_service):
        super().__init__()
        self.service = task_service
        
        
        self.title("Gestor de Tareas Pro")
        self.geometry("950x550")
        self.configure(bg="#1e1e2e") 

        
        tk.Label(self, text="📝 GESTIÓN DE MISIÓN", font=("Arial", 20, "bold"), 
                 bg="#1e1e2e", fg="#cba6f7").pack(pady=10)

        
        self.marco_input = tk.Frame(self, bg="#313244", padx=15, pady=15)
        self.marco_input.pack(padx=20, pady=10, fill="x")

        
        tk.Label(self.marco_input, text="Título:", bg="#313244", fg="white").grid(row=0, column=0)
        self.caja_titulo = tk.Entry(self.marco_input, width=20)
        self.caja_titulo.grid(row=0, column=1, padx=5)

        tk.Label(self.marco_input, text="Descripción:", bg="#313244", fg="white").grid(row=0, column=2)
        self.caja_desc = tk.Entry(self.marco_input, width=25)
        self.caja_desc.grid(row=0, column=3, padx=5)

        
        tk.Label(self.marco_input, text="Estado:", bg="#313244", fg="white").grid(row=1, column=0, pady=10)
        self.caja_estado = tk.Entry(self.marco_input, width=20)
        self.caja_estado.insert(0, "Pendiente") 
        self.caja_estado.grid(row=1, column=1, padx=5)

        self.btn_guardar = tk.Button(self.marco_input, text="➕ Agregar", bg="#a6e3a1", 
                                     command=self.agregar_tarea)
        self.btn_guardar.grid(row=1, column=2, padx=5)

        self.btn_editar = tk.Button(self.marco_input, text="✏️ Guardar Cambios", bg="#f9e2af", 
                                    command=self.guardar_edicion)
        self.btn_editar.grid(row=1, column=3, padx=5)

        
        self.marco_tabla = tk.Frame(self)
        self.marco_tabla.pack(padx=20, pady=10, fill="both", expand=True)

        self.tabla = ttk.Treeview(self.marco_tabla, columns=("id", "tit", "desc", "est"), show="headings")
        self.tabla.heading("id", text="UUID")
        self.tabla.heading("tit", text="Título")
        self.tabla.heading("desc", text="Descripción")
        self.tabla.heading("est", text="Estado Personalizado")
        
        self.tabla.column("id", width=100)
        self.tabla.pack(fill="both", expand=True)

        
        self.btn_borrar = tk.Button(self, text="🗑️ Eliminar Seleccionado", bg="#f38ba8", 
                                    fg="white", command=self.eliminar_uno)
        self.btn_borrar.pack(pady=5)

        self.btn_cargar = tk.Button(self, text="🖱️ Cargar en Formulario para Editar", bg="#89b4fa", 
                                    fg="white", command=self.cargar_en_formulario)
        self.btn_cargar.pack(pady=5)

        self.actualizar_pantalla()

    def agregar_tarea(self):
        t = self.caja_titulo.get()
        d = self.caja_desc.get()
        e = self.caja_estado.get()

        if not t or not d:
            messagebox.showwarning("Error", "¡Llena los campos!")
            return

        
        self.service.create_one_task(t, d) 
        
        
        self.limpiar_cajas()
        self.actualizar_pantalla()

    def eliminar_uno(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una tarea de la tabla primero")
            return
        
        
        valores = self.tabla.item(seleccion)['values']
        id_tarea = valores[0]
        
        
        
        self.actualizar_pantalla()
        messagebox.showinfo("Éxito", "Tarea eliminada correctamente")

    def cargar_en_formulario(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona algo para editar")
            return
        
        valores = self.tabla.item(seleccion)['values']
        
       
        self.caja_titulo.delete(0, tk.END)
        self.caja_titulo.insert(0, valores[1])
        
        self.caja_desc.delete(0, tk.END)
        self.caja_desc.insert(0, valores[2])
        
        self.caja_estado.delete(0, tk.END)
        self.caja_estado.insert(0, valores[3])

    def guardar_edicion(self):
      
        self.actualizar_pantalla()
        self.limpiar_cajas()
        messagebox.showinfo("Listo", "Tarea modificada")

    def limpiar_cajas(self):
        self.caja_titulo.delete(0, tk.END)
        self.caja_desc.delete(0, tk.END)
        self.caja_estado.delete(0, tk.END)
        self.caja_estado.insert(0, "Pendiente")

    def actualizar_pantalla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        tareas = self.service.get_all_task()
        for t in tareas:
           
            est = self.caja_estado.get() if not t.complete else "Completado"
            self.tabla.insert("", "end", values=(t.uuid, t.title, t.description, est))