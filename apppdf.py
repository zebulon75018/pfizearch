#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import json
import collections


with open('json_datapdf.json', 'r') as f:
    data = json.load(f)

files = []
for f in data["files"]:
    result =  f.split("/")
    files.append(result[1])

data["files"] = files

DEVELOPMENT_ENV  = False

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    global data
    terms =  request.args.get('term')
    type =  request.args.get('type')
    if type is None :
       type = "sites"
    terms = terms.lower()
    print(terms)
    result=[]
    resultindex = range(0,data["nbdocument"])
    for term in terms.split():
        if term in data["word"]:
            result = data["word"][term]
            resultkeyint = []
            for k in result.keys():
                resultkeyint.append(int(k))
            resultindex = set(resultkeyint).intersection(resultindex)
            resulttmp = {}
            for ri in resultindex:
                 resulttmp[str(ri)]=result[str(ri)]
            result = resulttmp

    sorted_result= []
    if len(result)> 0:
       sorted_result = sorted(result.items(), key =lambda  x: x[1], reverse = True)
    #print(sorted_result)
    """
    for r in result:
        filename= data["files"][int(r)]
        print(filename)
        with open(filename,"r") as f :
            text = f.read()
            idx = text.lower().find(str(" "+term+" "))
            print(idx)
            print(text[idx-20:idx+20])
    """

    return render_template('search.html', term=term,type=type,result=sorted_result,files= data["files"])


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

