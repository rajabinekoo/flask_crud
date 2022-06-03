def todo(db):
    class Todo(db.Model):
        __tablename__ = "todos"
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(20))
        description = db.Column(db.String(100))

        def create(self):
            db.session.add(self)
            db.session.commit()
            return self

        def __init__(self, title, description):
            self.title = title
            self.description = description

        def __repr__(self):
            return f"{self.id}"
    return Todo
