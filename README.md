# Tkinter project

```python
# Ejemplo de Treeview
import tkinter as tk
from tkinter import ttk
from service.task_service import TaskService

class AppWindow(tk.Tk):

    def __init__(self, task_service: TaskService) -> None:
        super().__init__()
        self._task_service = task_service

        self.title("Tkinter desde POO")
        self.geometry("500x500")
        self.resizable(False, False)
        # Esto viene de una base de datos

        self.users: list[dict[str, str]] = [
            {"fname": "Juan", "lname": "Santana", "age": "18"},
            {"fname": "Carlos", "lname": "Rodríguez", "age": "37"},
            {"fname": "María", "lname": "Rosario", "age": "28"},
        ]
        # Widgets
        self.create_widgets()

    def create_widgets(self) -> None:
        # print(self._task_service.get_all_task())

        label = tk.Label(self, text="Bienvenido a mi App")
        label.pack()

        label_fname = tk.Label(self, text="Nombre: ")
        label_fname.pack()
        self.fname = tk.Entry(self)
        self.fname.pack()

        label_lname = tk.Label(self, text="Apellido: ")
        label_lname.pack()
        self.lname = tk.Entry(self)
        self.lname.pack()

        label_age = tk.Label(self, text="Edad: ")
        label_age.pack()
        self.age = tk.Entry(self)
        self.age.pack()

        # Arbol jerárquico
        # tree = ttk.Treeview(self)
        # parent = tree.insert("", "end", text="Padre")
        # tree.insert(parent, "end", text="Hijo 1")
        # tree.insert(parent, "end", text="Hijo 2")

        # tree.pack()

        # Tabulado de los datos
        self.tree = ttk.Treeview(self, columns=("Column1", "Column2"))
        self.tree.column("#0", width=150)
        self.tree.column("Column1", width=150, anchor="center")
        self.tree.column("Column2", width=150, anchor="center")

        self.tree.heading("#0", text="Nombre")
        self.tree.heading("Column1", text="Apellido")
        self.tree.heading("Column2", text="Edad")

        button = tk.Button(self, text="Insertar usuarios",
                           command=self.get_user)
        button.pack()

    def get_user(self):
        fname = self.fname.get()
        lname = self.lname.get()
        age = self.age.get()

        self.users.append({"fname": fname, "lname": lname, "age": age})

        self.show_table()
        self.clear_inputs()

    def show_table(self):
        self.clear_table()

        for user in self.users:
            self.tree.insert(
                "", "end", text=f"{user["fname"]}", values=(f"{user["lname"]}", f"{user["age"]}"))

        self.tree.pack()

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def clear_inputs(self):
        self.fname.delete(0, "end")
        self.lname.delete(0, "end")
        self.age.delete(0, "end")

```
