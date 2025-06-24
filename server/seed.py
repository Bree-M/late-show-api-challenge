from server import app, db
from server.models import User, Guest, Episode, Appearance

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create test user
        admin = User(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        # Create sample guests
        guests = [
            Guest(name='John Mulaney', occupation='Comedian'),
            Guest(name='Emma Stone', occupation='Actor')
        ]
        db.session.add_all(guests)

        # Create episodes
        episodes = [
            Episode(date='2023-01-01', number=101),
            Episode(date='2023-01-08', number=102)
        ]
        db.session.add_all(episodes)

        db.session.commit()

if __name__ == '__main__':
    seed_data()