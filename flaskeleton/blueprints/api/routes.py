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


@ns.route('/tasks/<string:status>')
class TaskListByStatus(Resource):
    @ns.marshal_list_with(task)
    def get(self, status):
        return [
            task.__dict__.copy()
            for task in db.session.query(ToDoList).filter_by(
                to_do_status_id=int(status)
            )
        ], 200


# @api.route('/task/<int:id>')
# def task_get(id):
#     ...


# @api.route('/task/<string:status>')
# def task_get_by_status(status):
#     ...


# @api.route('/task/<int:id>', methods=['POST'])
# def task_post(id):
#     ...


# @api.route('/task/<int:id>', methods=['PATCH'])
# def task_patch(id):
#     ...


@ns.route('/status')
class StatusList(Resource):
    @ns.marshal_list_with(status)
    def get(self):
        return [
            task.__dict__.copy() for task in db.session.query(DoDoStatus).all()
        ], 200
