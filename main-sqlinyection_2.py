import os
import mysql.connector
from datetime import date
from functools import wraps
from flask import Flask, jsonify, request


app = Flask(__name__)

def products_select_sp(category = ""):
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    args = (category,)
    cursor = mydb.cursor()
    cursor.callproc('sp_products_by_category', args)
    for result in cursor.stored_results():
        product = result.fetchall()
    json_products = json.dumps(product)
    return json_products

@app.route('/')
def index():
    return jsonify({"hello": "SQL inyection test"}) 

@app.route('/products', methods=['GET'])
#ejemplo https://insecure-website.com/products?category=Gifts

#Cambio en la sentencia sql con or http://127.0.0.1:5000/products?category=gifts
# agraga la comentacion (#) despues del category+ ' en la libnea 22 http://127.0.0.1:5000/products?category=gifts%22+or+1=1%23

def products_get():
    args = request.args
    s_category = args.get("category")
    respuesta = products_select_sp(s_category)
    return jsonify({"msg":"success","products":respuesta})


"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 