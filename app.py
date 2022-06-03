from flask import Flask
from model.init import Model
from dto.init import DTO
from database.init import init as database_init
from routers.todo import todo_routes

app = Flask(__name__)
db = database_init(app=app)
models = Model(db)
dto = DTO(models.Todo, db)
todo_routes(app=app, db=db, models=models, dto=dto)

if __name__ == "__main__":
    app.run(debug=True)
