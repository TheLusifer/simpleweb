from bottle import get, run, template, static_file, debug, route, request, post, redirect
import dataset
import os

#definimos la conexion a la base de datos
db = dataset.connect('sqlite:///labs.db')
table = db['links']


#creamos la funcion para la pagina de index
@get('/')
def index():    
    result = db.query('SELECT name, link, desc, COUNT(*) FROM links GROUP BY id')
    #for row in result:
    #    print(row['name'], row['desc'], row['link'])    
    # le decimos el nombre del template    
    return template('index.html', result=result)
    
# definimos en donde se encuentran los archivos estaticos de css
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")
# definimos en donde se encuentran los archivos estaticos de fuentes
@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/font")
# definimos en donde se encuentran los archivos estaticos de imagenes
@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")
# definimos en donde se encuentran los archivos estaticos de java script
@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")



@get('/agregar')
def index():
    
    # le decimos el nombre del template
    return template('agregar.html', name="index")

@post('/agregar2')
def link_submit():
    name = request.forms.get("name")
    desc = request.forms.get("desc")
    link = request.forms.get("link")
    table.insert(dict(name=name, desc=desc, link=link))
    print(name, desc, link)
    return redirect('/agregar')




run(host='localhost', port=8080, reloader=True)