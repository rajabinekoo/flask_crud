from flask import Flask
from model.init import Model
from dto.init import DTO
from database.init import init as database_init
from routers.todo import todo_routes

app = Flask(__name__)
db = database_init(app)
models = Model(db)
dto = DTO(models, db)
todo_routes(app, db, models, dto)

if __name__ == "__main__":
    app.run(debug=True)
