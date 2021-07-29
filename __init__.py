#Libreria para importar el framework FLASK de python 
from flask import Flask


#Iniciamos la aplicacion SERVIDOR
app = Flask(__name__)


#Se crea ruta principal
@app.route('/')
def index():
	return "Bienvenido a Mundi Mall :Bloques MundiMall, Empresas todas por categoria"



#Se crea ruta secundaria
@app.route('/login_cliente')
def login_cliente():
	return "Login clientes"





if __name__ == '__main__':
	app.run(port= 8989, debug = True)
