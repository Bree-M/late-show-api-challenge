from . import db
from sqlalchemy.orm import validates

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # ✅ Backrefs
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    def to_dict_basic(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'episode_id': self.episode_id,
            'guest_id': self.guest_id,
            'episode': self.episode.to_dict_basic(),
            'guest': self.guest.to_dict_basic()
        }

    # ✅ Rating validation
    @validates('rating')
    def validate_rating(self, key, rating):
        if rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5.')
        return rating
