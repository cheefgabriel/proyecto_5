"""
Esta clase modela una Tarea (Task).
"""
from uuid import UUID, uuid4
from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    description: str
    complete: bool = False
    # Crear un uuid por cada objeto instanciado
    uuid: UUID = field(default_factory=uuid4)
