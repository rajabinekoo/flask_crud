from model.todo import todo


class Model:
    def __init__(self, db) -> None:
        self.Todo = todo(db)
        db.create_all()
