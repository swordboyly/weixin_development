#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from xml.etree import ElementTree as ET
from flask import render_template

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        echostr = request.args.get('echostr')
        return  echostr
    else:
        data = request.get_data()
        xml = ET.fromstring(data)
        ToUserName = xml.findtext(".//ToUserName")
        FromUserName = xml.findtext(".//FromUserName")
        CreateTime = xml.findtext(".//CreateTime")
        MsgType = xml.findtext(".//MsgType")
        Content = xml.findtext(".//Content")
        if MsgType == 'text':
            if Content == 'hi':
                return render_template('index.html',toUser = FromUserName,fromUser = ToUserName,CreateTime = CreateTime,content = u'你好啊！！！')
            else:
                return render_template('index.html',toUser = FromUserName,fromUser = ToUserName,CreateTime = CreateTime,content = u'很高兴见到你！！！')
        else:
            return render_template('index.html', toUser = FromUserName, fromUser = ToUserName, CreateTime = CreateTime,content = 'nice to meet you!!!')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)