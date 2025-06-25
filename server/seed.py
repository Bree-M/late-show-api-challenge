from app import app
from models import db
from models.episode import Episode
from models.guest import Guest
from models.appearance import Appearance
from models.user import User

def seed_database():
    with app.app_context():
        # Delete in correct order due to foreign key constraints
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        User.query.delete()
        db.session.commit()

        # Seed episodes
        e1 = Episode(date="2023-01-01", number=101)
        e2 = Episode(date="2023-01-08", number=102)
        db.session.add_all([e1, e2])
        db.session.commit()

        # Seed guests
        g1 = Guest(name="James Okitu", occupation="Comedian")
        g2 = Guest(name="Kenneth Keya", occupation="Actor")
        db.session.add_all([g1, g2])
        db.session.commit()

        # Seed appearances (safe FK usage)
        a1 = Appearance(rating=4, episode_id=e1.id, guest_id=g1.id)
        a2 = Appearance(rating=5, episode_id=e1.id, guest_id=g2.id)
        db.session.add_all([a1, a2])
        db.session.commit()

        # Seed users with hashed passwords
        users = [
            User(username="carren caro"),
            User(username="ann anne"),
            User(username="beth"),
            User(username="brenda")
        ]
        for user in users:
            user.set_password("password123")
        db.session.add_all(users)
        db.session.commit()

        print("Database seeded!")

if __name__ == "__main__":
    seed_database()
