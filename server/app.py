from flask import Flask,jsonify,request,session,Response,make_response,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_
from decorators import login_required
from flask_cors import CORS
from ext import db
from models import User,Shop,Comment,Goods,Reply,ShopType
from datetime import datetime,timedelta
import json,config,random,sys,os

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CORS(app)

serverPath = os.path.dirname(__file__)+'/'


@app.route("/getuser/")
def getUser():
    user_id = request.cookies.get("user_id")
    if(user_id==""):
        response = make_response(jsonify({'result':-1,'msg':'User not login'}))
    else:
        user = User.query.filter(User.id==user_id).first()
        if(user):
             response = make_response(jsonify({'username':user.username,'result':0,'avatar':user.avatar,'type':user.type}))
        else:
            response = make_response(jsonify({'result':-1,'msg':'No this user'}))
            
    
    response.headers['Access-Control-Allow-Credentials']='true'
    return response

@app.route("/")
def index():
    return send_from_directory("../", "index.html")

@app.route("/getusers/")
@login_required
def getUsers():
    user_id = request.cookies.get("user_id")
    user = User.query.filter(User.id==int(user_id)).first()
    if(user.type == 2):
        allUsers = User.query.filter().all()
        result = []
        for u in allUsers:
            result.append({
                "id":u.id,
                "username":u.username,
                "age":int(u.age),
                "gender":u.gender,
                "type":u.type,
                "ctime":str(u.ctime)
            })
        response = make_response(jsonify({"result":0,"users":result}))
    else:
        response = make_response(jsonify({"result":-1,"msg":'You are not admin'}))
    response.headers['Access-Control-Allow-Credentials']='true'

    return response


@app.route('/shoptypes/')
def getShopTypes():
    try:
        shoptypes = ShopType.query.filter().all()
        result = []
        for shoptype in shoptypes:
            result.append({
                "id":shoptype.id,
                "name":shoptype.name,
                "ctime":str(shoptype.ctime)
            })
        response = make_response(jsonify(result))
    except:
        response = make_response(jsonify({'result':-1,'msg':'Internal Error'}))
    response.headers['Access-Control-Allow-Credentials']='true'
    return response

@app.route('/login/',methods=['GET','POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter(and_(User.username == username,User.password==password)).first()
    
    if(user):
        response = make_response(jsonify({'username':user.username,'result':0,'avatar':user.avatar,'type':user.type}))
        response.headers['Access-Control-Allow-Credentials']='true'
        response.set_cookie('user_id',str(user.id),max_age=3600)
        return response
    else:
        response = make_response(jsonify({'result':-1,'msg':'username or password is incorrect'}))
        response.headers['Access-Control-Allow-Credentials']='true'
        return response

@app.route('/signup/',methods=['GET','POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    gender = request.form.get("gender")
    age = request.form.get("age")
    user_type = request.form.get("user_type")
    desc = request.form.get("desc")
    try:
        new_user = User(username=username,password=password,gender=gender,age=age,type=int(user_type),desc=desc)
        db.session.add(new_user)
        db.session.commit()
        avatar = request.files.get('avatar')
        avatar_url = "static/user_avatar/"+str(new_user.id)+".jpg"
        img_file = open(serverPath + avatar_url,'wb')
        img_file.write(avatar.read())
        img_file.close()
        new_user.avatar = avatar_url
        db.session.commit()
        response = make_response(jsonify({'result':0}))
        response.headers['Access-Control-Allow-Credentials']='true'
        return response
    except:
        response = make_response(jsonify({'result':-1}))
        response.headers['Access-Control-Allow-Credentials']='true'
        return response



@app.route("/createshop/",methods=['POST'])
def createshop():
    name = request.form.get("name")
    address = request.form.get("address")
    type_id = request.form.get("type_id")
    desc = request.form.get("desc")
    owner_id = request.cookies.get("user_id")

    imgs_length = request.form.get("imgs_length")
    try:
        new_shop = Shop(name=name,address=address,type_id=type_id,desc=desc,owner_id = owner_id)
        db.session.add(new_shop)
        db.session.commit()
        imgURLs = []
        
        for i in range(int(imgs_length)):
            imgURL = "static/shop_imgs/"+str(new_shop.id)+"_"+str(i)+".jpg"
            img = open(serverPath + imgURL,"wb")
            image = request.files.get("img"+str(i))
            img.write(image.read())
            img.close()
            imgURLs.append(imgURL)
        new_shop.imgs = json.dumps(imgURLs)
        db.session.commit()
        response = make_response(jsonify({'result':0}))
    except Exception as e:
        response = make_response(jsonify({'result':-1,'msg':str(e)}))
    
    response.headers['Access-Control-Allow-Credentials']='true'
    return response
            


@app.route('/getshops/')
def getShops():
    shops = Shop.query.filter().all()
    result = []
    for shop in shops:
        sum_rateing = 0
        for comment in shop.comments:
            sum_rateing += comment.rating

        if len(shop.comments)==0:
            average_rating = 0
        else:
            average_rating = round(sum_rateing/len(shop.comments),1)

        temp={
            "id":shop.id,
            "name":shop.name,
            "address":shop.address,
            "desc":shop.desc,
            "imgs":json.loads(shop.imgs),
            "owner":{
                "username":shop.owner.username,
                "avatar":shop.owner.avatar
            },
            "type":shop.shopType.name,
            "ctime":str(shop.ctime),
            'comments_length':len(shop.comments),
            "average_rating":average_rating
        }
        result.append(temp)
    response = make_response(jsonify({'result':0,'shops':result}))
    response.headers['Access-Control-Allow-Credentials']='true'
    return response


@app.route("/getshop/<shop_id>")
def getShop(shop_id):
    shop = Shop.query.filter(Shop.id==int(shop_id)).first()
    if(shop):
        comments = []
        for comment in reversed(shop.comments):
            comments.append({
                'id':comment.id,
                "content":comment.content,
                "rating":comment.rating,
                "imgs":json.loads(comment.imgs),
                "author":{
                    "username":comment.author.username,
                    "avatar":comment.author.avatar,
                },
                'ctime':str(comment.ctime),
                "replies_length":len(comment.replies)
            })
        result = {
            "id":shop.id,
            "name":shop.name,
            "address":shop.address,
            "desc":shop.desc,
            "imgs":json.loads(shop.imgs),
            "owner":{
                "username":shop.owner.username,
                "avatar":shop.owner.avatar,
            },
            "comments":comments,
            "type":shop.shopType.name,
            "ctime":str(shop.ctime)
        }
        response = make_response(jsonify({'result':0,'shop':result}))
    else:
        response = make_response(jsonify({'result':-1,'msg':'No this shop'}))
    
    response.headers['Access-Control-Allow-Credentials']='true'
    return response


@app.route('/getreplies/<comment_id>')
def getReplies(comment_id):
    replies = Reply.query.filter(Reply.comment_id == int(comment_id)).order_by(Reply.ctime.desc()).all()
    result = []
    for reply in replies:
        result.append({
            "id":reply.id,
            "content":reply.content,
            "author":{
                "username":reply.author.username,
                "avatar":reply.author.avatar
            },
            "ctime":str(reply.ctime)
        })
    response = make_response(jsonify({'result':0,'replies':result}))
    response.headers['Access-Control-Allow-Credentials']='true'
    return response

@app.route("/addcomment/",methods=['POST'])
def addComment():
    shop_id = request.form.get("shop_id")
    user_id = request.cookies.get("user_id")
    content = request.form.get("content")
    rating = request.form.get("rating")
    imgs_length = request.form.get("imgs_length")
    try:
        new_comment = Comment(content=content,rating = int(rating),author_id=int(user_id),shop_id=int(shop_id))
        db.session.add(new_comment)
        db.session.commit()

        imgURLs = []
        for i in range(int(imgs_length)):
            imgURL = "static/comment_imgs/"+str(new_comment.id)+"_"+str(i)+".jpg"
            img = open(serverPath + imgURL,"wb")
            image = request.files.get("img"+str(i))
            img.write(image.read())
            img.close()
            imgURLs.append(imgURL)
        
        new_comment.imgs = json.dumps(imgURLs)
        db.session.commit()
        response = make_response(jsonify({'result':0}))
    except Exception as e:
        response = make_response(jsonify({'result':-1,'msg':str(e)}))

    response.headers['Access-Control-Allow-Credentials']='true'
    return response

@app.route("/addreply/",methods=['POST'])
def addReply():
    
    user_id = request.cookies.get("user_id")
    content = request.form.get("content")
    comment_id = request.form.get("comment_id")

    try:
        new_reply = Reply(content = content,author_id = int(user_id),comment_id = int(comment_id))
        db.session.add(new_reply)
        db.session.commit()
        response = make_response(jsonify({'result':0,"reply":{
            "id":new_reply.id,
            "content":new_reply.content,
            "author":{
                "username":new_reply.author.username,
                "avatar":new_reply.author.avatar
            },
            "ctime":str(new_reply.ctime)
        }}))
    except Exception as e:
        response = make_response(jsonify({'result':-1,'msg':str(e)}))

    response.headers['Access-Control-Allow-Credentials']='true'
    return response






if __name__ == "__main__":
    app.run()
