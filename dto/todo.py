from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema


def todo_schema(Todo, db):
    class TodoSchema(SQLAlchemySchema):
        class Meta(SQLAlchemySchema.Meta):
            model = Todo
            sqla_session = db.session

        id = fields.Integer(dump_only=True)
        title = fields.String(required=True)
        description = fields.String(required=True)
    return TodoSchema
