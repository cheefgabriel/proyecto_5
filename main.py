from repository.task_repository import TaskRepository
from service.task_service import TaskService
from ui.app_window import AppWindow

def main() -> None:
    repository: TaskRepository = TaskRepository()
    service: TaskService = TaskService(repository)
    app: AppWindow = AppWindow(service)

    app.mainloop()

if __name__ == "__main__":
    main()
