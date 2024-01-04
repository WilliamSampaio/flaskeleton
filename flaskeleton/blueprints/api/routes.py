from flask_restx import Namespace, Resource, fields

from flaskeleton.extensions.database import db
from flaskeleton.models import ToDoList

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


@ns.route('/')
class Hello(Resource):
    def get(self):
        return {'message': 'Hello!'}, 418


@ns.route('/tasks')
class TaskList(Resource):
    @ns.marshal_list_with(task)
    def get(self):
        data = []
        for task in db.session.query(ToDoList).all():
            task_data = task.__dict__.copy()
            if '_sa_instance_state' in task_data:
                del task_data['_sa_instance_state']
            data.append(task_data)
        return data, 200


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


# @api.route('/status')
# def status_list():
#     ...
