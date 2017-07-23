from app import db

class Poll(db.Model):
    __tablename__ = "poll"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<id {} : name {}>'.format(self.id, self.name)


class Opinion(db.Model):
    __tablename__ = "opinion"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String()) 
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))

    def __init__(self, desc, poll):
        self.description = desc
        self.poll_id = poll
    
    def __repr__(self):
        return '<id {} : poll_id {} : description {}'.format(self.id, self.poll_id, self.description)
    
        
