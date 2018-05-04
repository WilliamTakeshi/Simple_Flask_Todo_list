from db import db

class TaskModel(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    done = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    def json(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'done': self.done}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()