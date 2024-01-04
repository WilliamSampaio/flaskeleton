from datetime import datetime

from flask_restx import Namespace, Resource, fields

from flaskeleton.extensions.database import db
from flaskeleton.models import DoDoStatus, ToDoList

ns = Namespace('api', description='API operations')

# Models
task = ns.model(
    'Task',
    {
        'id': fields.Integer(required=True),
        'description': fields.String(required=True),
        'to_do_status_id': fields.Integer(required=True),
        'created_at': fields.DateTime(required=True),
        'updated_at': fields.DateTime(),
    },
)

new_task = ns.model(
    'NewTask',
    {
        'description': fields.String(required=True),
        'to_do_status_id': fields.Integer(required=True),
    },
)

status = ns.model(
    'Status',
    {
        'id': fields.Integer(required=True),
        'description': fields.String(required=True),
    },
)


@ns.route('/')
class Hello(Resource):
    def get(self):
        return {'message': 'Hello!'}, 418


@ns.route('/tasks')
class TaskList(Resource):
    @ns.marshal_list_with(task)
    def get(self):
        return [
            task.__dict__.copy() for task in db.session.query(ToDoList).all()
        ], 200


@ns.route('/tasks/<string:status_id>')
class TaskListByStatus(Resource):
    @ns.marshal_list_with(task)
    def get(self, status_id):
        return [
            task.__dict__.copy()
            for task in db.session.query(ToDoList).filter_by(
                to_do_status_id=int(status_id)
            )
        ], 200


@ns.route('/task')
class TaskPost(Resource):
    @ns.expect(new_task)
    @ns.marshal_with(task, code=201)
    def post(self):
        data = ns.payload
        task = ToDoList()
        task.description = data['description']
        task.to_do_status_id = data['to_do_status_id']
        if data['to_do_status_id'] != 1:
            task.updated_at = datetime.now()
        db.session.add(task)
        db.session.commit()
        return task, 201


@ns.route('/task/<int:id>')
class Task(Resource):
    @ns.marshal_with(task)
    def get(self, id):
        task = db.session.query(ToDoList).get(int(id))
        if not task:
            ns.abort(404, f"Todo {id} doesn't exist")
        return task, 200

    @ns.expect(new_task)
    @ns.marshal_with(task, code=201)
    def put(self, id):
        data = ns.payload
        task = db.session.query(ToDoList).get(int(id))
        if not task:
            ns.abort(404, f"Todo {id} doesn't exist")
        task.description = data['description']
        task.to_do_status_id = data['to_do_status_id']
        task.updated_at = datetime.now()
        db.session.commit()
        return task, 200


@ns.route('/status')
class StatusList(Resource):
    @ns.marshal_list_with(status)
    def get(self):
        return [
            task.__dict__.copy() for task in db.session.query(DoDoStatus).all()
        ], 200
