from app import db

class Square(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    desc = db.Column(db.String(255))
    query = db.Column(db.String(255))

    def __repr__(self):
        return '<Square {}>'.format(self.id)    

class Card(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    s11 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s12 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s13 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s14 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s15 = db.Column(db.String(6), db.ForeignKey('square.id'))

    s21 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s22 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s23 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s24 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s25 = db.Column(db.String(6), db.ForeignKey('square.id'))

    s31 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s32 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s33 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s34 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s35 = db.Column(db.String(6), db.ForeignKey('square.id'))

    s41 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s42 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s43 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s44 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s45 = db.Column(db.String(6), db.ForeignKey('square.id'))

    s51 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s52 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s53 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s54 = db.Column(db.String(6), db.ForeignKey('square.id'))
    s55 = db.Column(db.String(6), db.ForeignKey('square.id'))
    #s11 = db.relationship(db.String(6), db.ForeignKey('square.id'))

    def __repr__(self):
        return '<Card {}>'.format(self.id)      


class Room(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(50))
    cardid = db.Column(db.String(6), db.ForeignKey('card.id'))

    def __repr__(self):
        return '<Room {}>'.format(self.id)    

class User(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(50))
    roomid = db.Column(db.String(6), db.ForeignKey('room.id'))
    color = db.Column(db.String(7))
    result = db.Column(db.String(25))
    def __repr__(self):
        return '<User {}>'.format(self.id)    