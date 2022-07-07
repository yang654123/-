from __future__ import print_function
import sys,json
from flask import Blueprint, jsonify
from flask import render_template, flash, redirect, url_for, request,session
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.Model.models import User

# Configure Blueprint.
authentication_blueprint = Blueprint(
    'authentication', __name__, url_prefix='/')
authentication_blueprint.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'




@authentication_blueprint.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            u = User(username=data.get("account"), 
                    password=data.get("password"), 
                    realName = data.get("realName"), 
                    )
            db.session.add(u)
            db.session.commit()
            context = {
                "code":201,
                "message":"注册成功"
            }
            return jsonify(context)
        except:
            context = {
                "code":203,
                "message":"注册失败"
            }
            return jsonify(context)



@authentication_blueprint.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = json.loads(request.data)
        user = User.query.filter_by(username=data.get("username")).first()
        if not user or (not (user.password==data.get("password"))): 
            context = {
                "message":"fail"
            }
            return jsonify(context)
        session.clear()
        session['user_name'] = user.username
        rsp={
                "code":0,
                "result":{
                    "roles":[{"roleName":"Super Admin","value":"super"}],
                    "userId":user.userId,
                    "username":user.username,
                    "token":"fakeToken1",
                    "realName":user.realName,
                    "desc":"manager"},
                "message":"ok",
                "type":"success"}
        
        return jsonify(rsp) 


@authentication_blueprint.route('/getUserInfo', methods=['GET','POST'])
def getUserInfo():
    if request.method == 'GET':
        sess_username = session['user_name'] 
        user = User.query.filter_by(username=sess_username).first()

        test =   {
            "code":0,
            "result":{
                "userId":user.userId,
                "username":user.username,
                "realName":user.realName,
                "avatar":"https://q1.qlogo.cn/g?b=qq&nk=190848757&s=640",
                "desc":"manager",
                "password":user.password,
                "token":"fakeToken1",
                "homePath":"/dashboard/targetextraction",
                "roles":[{"roleName":"Super Admin","value":"super"}]
                },
                "message":"ok",
                "type":"success"
                }
        return jsonify(test) 

from functools import wraps
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_name' not in session :
            return redirect(url_for('authentication.login'))
        return view(**kwargs)
    return wrapped_view