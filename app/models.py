from app import db

class User(db.Model):
    '''
    Inherits db.Model
    Fields are instance of db.Column class

    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        '''
        Tells Python how to print objects of this class - For debugging
        '''
        return '<User {usr}>'.format(usr=username)

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)