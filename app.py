from flask import Flask, render_template
from flask_restful import Api

from resources.task import TaskAPI, TaskListAPI
from models.task import TaskModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'todolistsecret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    form = {}
    return render_template('public/home.html', form=form)

@app.route('/task', methods=['GET'])
def task():
    tasks_done = TaskModel.query.filter_by(done=True)
    tasks_not_done = TaskModel.query.filter_by(done=False)
    form = {"taskdone": tasks_done,
            "tasknotdone": tasks_not_done}
    print(form)
    return render_template('public/task.html', form=form)


api.add_resource(TaskListAPI, '/v0/task', endpoint="api.task")
api.add_resource(TaskAPI, '/v0/task/<_id>', endpoint="api.tasks")

if __name__ == '__main__':
    from db import db
    db.init_app(app)
app.run(port=5000, debug=True)