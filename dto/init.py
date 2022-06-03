from dto.todo import todo_schema


class DTO:
    def __init__(self, models, db) -> None:
        self.TodoSchema = todo_schema(models.Todo, db)
