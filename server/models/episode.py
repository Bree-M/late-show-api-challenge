from . import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # ✅ Cascade delete appearances
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    def to_dict_basic(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number
        }
