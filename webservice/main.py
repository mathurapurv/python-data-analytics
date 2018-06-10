from flask import Flask, redirect, url_for, request ,  send_from_directory , send_file
from flask_restful import Resource, Api
import datetime
import population_analytics_webservice as pop
import os


app = Flask(__name__  )


@app.route('/')
def hello_world():
    return 'Hello World at [ '+  str(datetime.datetime.now())+' ] !'

@app.route('/hello')
def hello_world_greeting():
   return 'Hello , how are you ?'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/hello/<echo>')
def echo(echo):
   return echo

@app.route('/user/postinfo' ,methods=["POST"])
def postUserInfo():
    print(request.form)
    jsonData = request.get_json()
    print(jsonData)
    return 'Posted !!'


@app.route('/user/postinfoasJSON' ,methods=["POST"])
def postinfoasJSON():
    jsonData = request.get_json()
    print(jsonData['name'])
    return 'Posted JSON !!'

@app.route('/math/half/<int:postID>')
def halp(postID):
   return str(postID /2)

@app.route('/math/double/<float:revNo>')
def revision(revNo):
   return str(revNo*2)

@app.route('/<path:path>')
def send_js(path):
    print(path)
    root_dir = os.path.dirname(os.getcwd())
    finalPath = os.path.join(root_dir, 'worldbankdataanalyticsUI' , 'worldbankdataanalyticsUI' , 'dist');
    print(finalPath)
    return send_from_directory(finalPath ,path)



@app.route('/analysePopulationGrowth/<country_list>')
def analysePopulationGrowth(country_list):
    return pop.createPopulationStatsForSelectedCountries(country_list)

@app.route('/analysePopulationGrowthGraph/<country_list>')
def analysePopulationGrowthGraph(country_list):
    fileName =  pop.createPopulationStatsForSelectedCountries(country_list , responseFormat='GRAPH')
    return send_file(fileName, mimetype='image/png')



if __name__ == '__main__':
    app.run(port=8081,debug=True)