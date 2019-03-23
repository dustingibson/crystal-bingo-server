from app import app,db
from app.models import Square, Card, User, Room
from flask import request, jsonify, Response
import random,sys,json

@app.route('/')
@app.route('/index')
def index():
    # sq = Square(id="XYZ", desc="XYZ", query="XYZ")
    # db.session.add(sq)
    # db.session.commit()
    sq = db.session.query(Square).filter_by(id='XYZ').first()
    return "blah"

def GrabSquares():
    return db.session.query(Square).first().id

def GetRandID():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(6))

def CreateCard(roomid):
    #Get all Squares
    allSquares = db.session.query(Square).all()
    s = []
    for curSquare in allSquares:
        s.append(curSquare.id)
    random.shuffle(s)
    randID = GetRandID()
    cr = Card(id=randID,s11=s[0],s12=s[1],s13=s[2],s14=s[3],s15=s[4],s21=s[5],s22=s[6],s23=s[7],s24=s[8],s25=s[9],s31=s[10],s32=s[11],s33=s[12],s34=s[13],s35=s[14],s41=s[15],s42=s[16],s43=s[17],s44=s[18],s45=s[19],s51=s[20],s52=s[21],s53=s[22],s54=s[23],s55=s[24])
    db.session.add(cr)
    db.session.commit()
    return cr

def CreateUser(roomid,name,color):
    #Check if color or name is taken
    chkUsers = db.session.query(User).filter_by(roomid=roomid).all()
    if(len(chkUsers) > 8):
        return [False, "More than 8 users"]
    for curChkUser in chkUsers:
        if( curChkUser.color == color ):
            return [False, "Color is already taken"]
        if( curChkUser.name == name ):
            return [False, "Name is already taken"]
    userID = GetRandID()
    user = User(id=userID,roomid=roomid,name=name,color=color,result='0000000000000000000000000')
    db.session.add(user)
    db.session.commit()
    return [True,user]

def JoinUser(roomid,name):
    chkUsers = db.session.query(User).filter_by(roomid=roomid).all()
    for curChkUser in chkUsers:
        if( curChkUser.name == name ):
            return [True, curChkUser]
    return [False, "User does not exist"]

@app.route('/GetNews', methods = ['GET'])
def GetNews():
    if request.method == 'GET':
        try:
            news = open("news.html","r").read()
            return news
        except Exception as e:
            print(e)
            return ""

@app.route('/GetRoomInfo', methods = ['GET'])
def GetRoomInfo():
    if request.method == 'GET':
        try:
            roomID = request.args["roomid"]
            users = db.session.query(User).filter_by(roomid=roomID).all()
            room = db.session.query(Room).filter_by(id=roomID).first()
            card = db.session.query(Card).filter_by(id=room.cardid).first()

            s11 = db.session.query(Square).filter_by(id=card.s11).first()
            s12 = db.session.query(Square).filter_by(id=card.s12).first()
            s13 = db.session.query(Square).filter_by(id=card.s13).first()
            s14 = db.session.query(Square).filter_by(id=card.s14).first()
            s15 = db.session.query(Square).filter_by(id=card.s15).first()

            s21 = db.session.query(Square).filter_by(id=card.s21).first()
            s22 = db.session.query(Square).filter_by(id=card.s22).first()
            s23 = db.session.query(Square).filter_by(id=card.s23).first()
            s24 = db.session.query(Square).filter_by(id=card.s24).first()
            s25 = db.session.query(Square).filter_by(id=card.s25).first()

            s31 = db.session.query(Square).filter_by(id=card.s31).first()
            s32 = db.session.query(Square).filter_by(id=card.s32).first()
            s33 = db.session.query(Square).filter_by(id=card.s33).first()
            s34 = db.session.query(Square).filter_by(id=card.s34).first()
            s35 = db.session.query(Square).filter_by(id=card.s35).first()

            s41 = db.session.query(Square).filter_by(id=card.s41).first()
            s42 = db.session.query(Square).filter_by(id=card.s42).first()
            s43 = db.session.query(Square).filter_by(id=card.s43).first()
            s44 = db.session.query(Square).filter_by(id=card.s44).first()
            s45 = db.session.query(Square).filter_by(id=card.s45).first()

            s51 = db.session.query(Square).filter_by(id=card.s51).first()
            s52 = db.session.query(Square).filter_by(id=card.s52).first()
            s53 = db.session.query(Square).filter_by(id=card.s53).first()
            s54 = db.session.query(Square).filter_by(id=card.s54).first()
            s55 = db.session.query(Square).filter_by(id=card.s55).first()

            squareList = [s11,s12,s13,s14,s15,s21,s22,s23,s24,s25,s31,s32,s33,s34,s35,s41,s42,s43,s44,s45,s51,s52,s53,s54,s55]

            results = { "squares" : [], "roominto" : { "id" : room.id, "name" : room.name} , "userinfo": [] }

            results["userinfo"] = []

            for i in range(0, len(users)):
                curUser = users[i]
                userDict = { "id" : curUser.id,  "result": curUser.result, "color": curUser.color, "status": curUser.color, "name" : curUser.name }
                results["userinfo"].append(userDict)


            for curSquare in squareList:
                results["squares"].append( { "id": curSquare.id, "desc": curSquare.desc, "query": curSquare.query}  )

            resp = Response(json.dumps(results))
            resp.headers["Access-Control-Allow-Origin"] = "*"


            return resp  

        except Exception as e:
            print(e)
            return "error"

@app.route('/UpdateResults', methods = ['POST'])
def UpdateResults():
    if request.method == 'POST':
        try:
            userid = request.args['userid']
            results = request.args['results']
            db.session.query(User).filter_by(id=userid).update(dict(result=results))
            db.session.commit()
            return "success"
        except Exception as e:
            print(e)
            return "error"

def CreateResponse(respDict):
    return Response(json.dumps(respDict))

@app.route('/CreateRoom', methods = ['POST'])
def CreateRoom():
    if request.method == 'POST':
        try:
            roomID = GetRandID()
            roomName = request.args['roomname']
            userName = request.args['username']
            userColor = request.args['usercolor']
            cardID = CreateCard(roomID)
            user = CreateUser(roomID, userName, userColor)
            if(not user[0]):
                return CreateResponse({"success": False, "message": user[1]})
            room = Room(id=roomID, cardid=cardID.id, name=roomName)
            db.session.add(room)
            db.session.commit()
            return CreateResponse({"success": True, "message": "", "user": user[1].id, "room": roomID})
        except Exception as e:
            return CreateResponse({"success" : False, "message" : str(e)})

@app.route('/JoinRoom', methods = ['POST'])
def JoinRoom():
    if request.method == 'POST':
        try:
            roomID = request.args['roomid']
            userName = request.args['username']
            userColor = request.args['usercolor']
            user = CreateUser(roomID, userName, userColor)
            room = db.session.query(Room).filter_by(id=roomID).all()
            if(len(room) <= 0):
                return CreateResponse({"success": False, "message": "Room does not exist"})
            if(not user[0]):
                return CreateResponse({"success": False, "message": user[1]})
            return CreateResponse({"success": True, "message": "", "user": user[1].id, "room": roomID})
        except Exception as e:
            print(e)
            return CreateResponse({"success" : False, "message" : str(e)})

@app.route('/RejoinRoom', methods = ['POST'])
def RejoinRoom():
    if request.method == 'POST':
        try:
            roomID = request.args['roomid']
            userName = request.args['username']
            user = JoinUser(roomID, userName)
            room = db.session.query(Room).filter_by(id=roomID).all()
            if(len(room) <= 0):
                return CreateResponse({"success": False, "message": "Room does not exist"})
            if(not user[0]):
                return CreateResponse({"success": False, "message": user[1]})
            return CreateResponse({"success": True, "message": "", "user": user[1].id, "room": room[0].id})
        except Exception as e:
            print(e)
            return CreateResponse({"success" : False, "message" : str(e)})

def getObjectDict(roomInfo, userInfo):
    results = {}
    results["roominfo"] = { "roomcode" : roomInfo.id, "roomname" : roomInfo.name  }
    results["userinfo"] = []
    for i in range(0, len(userInfo)):
        curUser = userInfo[i]
        userDict = { "id" : curUser.id,  "result": curUser.result, "color": curUser.color, "status": curUser.color, "name" : curUser.name }
        results["userinfo"].append(userDict)
    return results

#0000000000000000000000000
@app.route('/GetInfo', methods = ['GET'])
def GetInfo():
    if request.method == 'GET':
        try:
            roomID = request.args['roomid']
            userID = request.args["userid"]
            #curSquare = db.session.query(Square).first().id
            room = db.session.query(Room).filter_by(id=roomID).first()
            users = db.session.query(User).filter_by(roomid=roomID).all()
            card = db.session.query(Card).filter_by(id=room.cardid).first()
            #squares = db.session.query(Square).filter( (Square.id==card.s11) | (Square.id==card.s12) | (Square.id==card.s13) | (Square.id==card.s14) | (Square.id==card.s15) | (Square.id==card.s21) | (Square.id==card.s22) | (Square.id==card.s23) | (Square.id==card.s24) | (Square.id==card.s25) | (Square.id==card.s31) | (Square.id==card.s32) | (Square.id==card.s33) | (Square.id==card.s34) | (Square.id==card.s35) | (Square.id==card.s41) | (Square.id==card.s42) | (Square.id==card.s43) | (Square.id==card.s44) | (Square.id==card.s45) | (Square.id==card.s51) | (Square.id==card.s52) | (Square.id==card.s53) | (Square.id==card.s54) | (Square.id==card.s55) ).all()
            result = getObjectDict( room , users )
            resp = Response(json.dumps(result))
            resp.headers["Access-Control-Allow-Origin"] = "*"
            return resp
        except Exception as e:
            print(e)
            return "error"

@app.route('/GetRAM', methods = ['POST'])
def GetRAM():
    if request.method == 'POST':
        binVal = request.get_data()
        return "blah"