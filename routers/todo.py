from flask import Flask, request, jsonify, make_response


def todo_routes(app, db, models, dto):
    @app.route('/api/todo', methods=['GET'])
    def index():
        get_todos = models.Todo.query.all()
        todo_schema = dto.TodoSchema(many=True)
        todos = todo_schema.dump(get_todos)
        return make_response(jsonify({"todos": todos}))

    @app.route('/api/todo/<id>', methods=['GET'])
    def get_todo_by_id(id):
        get_todo = models.Todo.query.get(id)
        todo_schema = dto.TodoSchema()
        todo = todo_schema.dump(get_todo)
        return make_response(jsonify(todo))

    @app.route('/api/todo/<id>', methods=['PUT'])
    def update_todo_by_id(id):
        data = request.get_json()
        get_todo = models.Todo.query.get(id)
        if data.get('title'):
            get_todo.title = data['title']
        if data.get('description'):
            get_todo.description = data['description']
        db.session.add(get_todo)
        db.session.commit()
        todo_schema = dto.TodoSchema(only=['id', 'title', 'description'])
        todo = todo_schema.dump(get_todo)
        return make_response(jsonify(todo))

    @app.route('/api/todo/<id>', methods=['DELETE'])
    def delete_todo_by_id(id):
        get_todo = models.Todo.query.get(id)
        db.session.delete(get_todo)
        db.session.commit()
        return make_response("", 204)

    @app.route('/api/todo', methods=['POST'])
    def create_todo():
        data = request.get_json()
        todo_schema = dto.TodoSchema()
        todo = todo_schema.load(data)
        todo_instance = models.Todo(
            title=todo["title"], description=todo["description"])
        result = todo_schema.dump(todo_instance.create())
        return make_response(jsonify(result), 200)
