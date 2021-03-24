from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adminId = db.Column(db.String(20))
    passWd = db.Column(db.String(20))
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Admin {}>'.format(self.name)


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(20))
    goodsId = db.Column(db.String(20))
    orderTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    orderCount = db.Column(db.SmallInteger)
    salePrice = db.Column(db.Float)
    userChecked = db.Column(db.Boolean)
    orderNumber = db.Column(db.String(50))
    postTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    adminChecked = db.Column(db.Boolean)

    def __repr__(self):
        return '<Basket {}>'.format(self.orderNumber)


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeid = db.Column(db.Integer)
    name = db.Column(db.String(50))
    an_number = db.Column(db.String(50))
    producer = db.Column(db.String(20))
    package = db.Column(db.String(20))
    salePrice = db.Column(db.Float)
    storePrice = db.Column(db.Float)
    content = db.Column(db.String(1000))
    readCount = db.Column(db.Integer)
    buyCount = db.Column(db.Integer)

    def __repr__(self):
        return '<Goods {}>'.format(self.name)


class GoodsType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))

    def __repr__(self):
        return '<GoodsType {}>'.format(self.type)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(20))
    pwd_hash = db.Column(db.String(128))
    username = db.Column(db.String(50))
    sex = db.Column(db.Boolean)
    address = db.Column(db.String(1000))
    email = db.Column(db.String(50))
    telephone = db.Column(db.String(100))
    mobile = db.Column(db.String(50))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

