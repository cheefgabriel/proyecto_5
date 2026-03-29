"""
Esta clase se encarga de la lógica de mi aplicación.
Se conecta con los datos a través del Repositorio de datos.
"""
from repository.task_repository import TaskRepository
from model.task import Task
from uuid import UUID

class TaskService:
    def __init__(self, task_repository: TaskRepository) -> None:
        self._task_repository = task_repository

    def get_all_task(self) -> list[Task]:
        """Retorna todas las tareas"""
        return self._task_repository.get_all()

    def delete_one_task(self, uuid: UUID) -> None:
        pass

    def create_one_task(self, title: str, description: str) -> Task:
        """Crea y retorna la tarea y insertada """
        return self._task_repository.create_one(title, description)

    def update_one_task(self, uuid: UUID, tle: str, description: str, complete: bool):
        pass
