from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():    
    return render_template('index.html', dojos=Dojo.all_dojos())

@app.route('/dojo/create', methods= ['POST'])
def create_dojo():
    print(request.form)
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    return render_template('index.html', dojos=Dojo.all_dojos())

@app.route('/create/ninja', methods= ['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/ninja')

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html', dojos=Dojo.all_dojos())

@app.route('/ninjas/dojos/<int:id_dojo>')
def ninjas_dojos(id_dojo):
    data = {"id":id_dojo}
    return render_template('ninjas_dojos.html', dojo=Dojo.ninjas_con_dojos(data))