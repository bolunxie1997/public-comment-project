from ext import db
from datetime import datetime

class User(db.Model):
    __tablename__:'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    age = db.Column(db.String(10))
    type = db.Column(db.Integer)# 0 - user 1 - boss 2 - admin
    desc = db.Column(db.Text)
    avatar = db.Column(db.Text) 
    state = db.Column(db.Integer,default = 1) # # 1 - regular 0 - deleted
    ctime = db.Column(db.DateTime,default = datetime.now)

class ShopType(db.Model):
    __tablename__:'shoptype'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    ctime = db.Column(db.DateTime,default = datetime.now)

class Shop(db.Model):
    __tablename__:'shop'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    address = db.Column(db.Text)
    desc = db.Column(db.Text)
    imgs = db.Column(db.Text)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    owner = db.relationship('User',backref = db.backref('shops'))
    type_id = db.Column(db.Integer,db.ForeignKey('shop_type.id'))
    shopType = db.relationship('ShopType',backref = db.backref('shops'))
    state = db.Column(db.Integer,default = 1) # # 1 - regular 0 - deleted
    ctime = db.Column(db.DateTime,default = datetime.now)



class Goods(db.Model):
    __tablename__:'goods'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Text)
    desc = db.Column(db.Text)
    imgs = db.Column(db.Text)
    shop_id = db.Column(db.Integer,db.ForeignKey('shop.id'))
    shop = db.relationship('Shop',backref = db.backref('goods'))
    state = db.Column(db.Integer,default = 1) # # 1 - regular 0 - deleted
    ctime = db.Column(db.DateTime,default = datetime.now)

class Comment(db.Model):
    __tablename__ : "comment"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text)
    rating = db.Column(db.Integer)
    imgs = db.Column(db.Text)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref = db.backref('comments'))

    shop_id = db.Column(db.Integer,db.ForeignKey('shop.id'))
    shop = db.relationship('Shop',backref = db.backref('comments'))
    state = db.Column(db.Integer,default = 1) # # 1 - regular 0 - deleted

    ctime = db.Column(db.DateTime,default = datetime.now)


class Reply(db.Model):
    __tablename__ : "reply"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref = db.backref('replies'))
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))
    comment = db.relationship('Comment',backref = db.backref('replies'))
    state = db.Column(db.Integer,default = 1) # # 1 - regular 0 - deleted

    ctime = db.Column(db.DateTime,default = datetime.now)


# class Support(db.Model):
#     __tablename__ = 'support'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     supporter_id = db.Column(db.Integer)
#     author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
#     author = db.relationship('User',backref = db.backref('suppoters'))
#     ctime = db.Column(db.DateTime,default = datetime.now)

# class Images(db.Model):
#     __tablename__ : 'images'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     img_name = db.Column(db.Text,nullable=False)
#     params = db.Column(db.Text)
#     author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
#     author = db.relationship('User',backref = db.backref('images'))
#     ctime = db.Column(db.DateTime,default = datetime.now)

# class Warn(db.Model):
#     __tablename__ : 'warn'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     phone = db.Column(db.String(20))
#     ctime = db.Column(db.DateTime,default = datetime.now)
#     studentno = db.Column(db.String(12))
#     statuecode = db.Column(db.Integer)

# class Tempcode(db.Model):
#     __tablename__:'tempcode'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     phone = db.Column(db.String(20))
#     code = db.Column(db.String(6))
#     ctime = db.Column(db.DateTime,default = datetime.now)
    


    







