from app.graph.user.alchemy import User
from app.graph.channel.alchemy import Channel
from app import db

if __name__ == "__main__":
    db.create_all()
