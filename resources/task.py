from flask_restful import Resource, reqparse, marshal
from models.task import TaskModel

class TaskListAPI(Resource):
    def get(self):
        return {'task': list(map(lambda x: x.json(), TaskModel.query.all()))}

    def post(self):
        args = TaskAPI.parser.parse_args()
        task = TaskModel(**args)
        try:
            task.save_to_db()
        except:
            return {"message": "An error occurred creating the task."}, 500
        return task.json(), 201

class TaskAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=False)
    parser.add_argument('description', type=str, required=False)
    parser.add_argument('done', type=bool, required=False)

    def get(self, _id):
        task = TaskModel.find_by_id(_id)
        if task:
            return task.json()
        return {'message': 'Task not found'}, 404

    def put(self, _id):
        data = self.parser.parse_args()
        task = TaskModel.find_by_id(_id)

        if task:
            task.title = data['title']
            task.description = data['description']
            task.done = data['done']
        else:
            task = TaskModel(**data)
        task.save_to_db()

        return task.json()

    def delete(self, _id):
        task = TaskModel.find_by_id(_id)
        if task:
            task.delete_from_db()
            return {'message': 'Task deleted'}

        return {'message': "There is no task with id '{}'".format(_id)}, 400
