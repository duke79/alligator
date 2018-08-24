from app import db
from sqlalchemy.dialects.mysql import INTEGER


class User(db.Model):
    __tablename__ = 'person'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(200), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)
    photo_url = db.Column(db.String(2013), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    firebase_uid = db.Column(db.String(100), nullable=True)
    # created_at = db.Column(db.DateTime, default=db.func.now())
    # updated_at = db.Column(db.DateTime, default=db.func.now())
    ## https://bitbucket.org/zzzeek/sqlalchemy/issues/3444/sqlalchemy-does-not-emit-server_onupdate
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           )

    # def __repr__(self):
    #     return '<User %r>' % self.username
