"""
Esta clase manipula los datos.
"""
from model.task import Task
from uuid import UUID

class TaskRepository:
    _task: list[Task] = [
        Task("Leer un libro", "Debo leer el libro 'El diario de Ana Frank'"),
        Task("Practica programación", "Debo practica mucho Python."),
        Task("Ver anime", "Debo dedicar solo media hora para Dragon Ball Z")
    ]

    def get_all(self) -> list[Task]:
        """Recupera todas las tareas"""
        return self._task

    def delete_one(self, uuid: UUID) -> None:
        """Elimina una tarea"""
        pass

    def create_one(self, title: str, description: str) -> Task:
        """Crea y retorna la tarea insertada"""
        task: Task = Task(title, description)
        self._task.append(task)
        return task

    def update_one(self, uuid: UUID, tle: str, description: str, complete: bool):
        """Actualiza una tarea"""
        pass
