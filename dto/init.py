from dto.todo import todo_schema


class DTO:
    def __init__(self, Todo, db) -> None:
        self.TodoSchema = todo_schema(Todo, db)
