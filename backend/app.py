from flask import Flask, json, render_template, request
from flask_cors import CORS
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "my_password"))
session = driver.session()


# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r"/*":{'origins':"*"}})


@app.route("/catalog", methods=["GET"])
def get_catalog():
    query = """
    MATCH (p:Product) WHERE p.amount > 0 RETURN p;
    """
    results=session.run(query)
    data=results.data() 
    return(json.dumps(data, default=str, ensure_ascii=False).encode('utf8'))


@app.route("/addProduct", methods=["GET", "POST"])
def addProduct():
    response = {'status':'success'}
    data = request.get_json()
    add_query = """
    MATCH (n:User {id: $user_id, role: 'Продавец'})
    CREATE (n)-[:IS_SELLER_OF]->(product:Product {id: toInteger($product_id), name: $name, image: $image,\
        price: toFloat($price), shelf_life: Date($shelf_life), description: $description, amount: toInteger($amount)});
    """
    map={"user_id": data.get('user_id'), "product_id": data.get('product_id'), "name": data.get('name'), "image": data.get('image'),\
        "price": data.get('price'), "shelf_life": data.get('shelf_life'), "description": data.get('dedscription'), "amount": data.get('amount')}
    try:
        session.run(add_query, map)
    except Exception as e:
        response['status'] = 'failed'
        response['message'] = str(e)
    return(json.dumps(response))

@app.route("/warehouse", methods=["GET", "POST"])     
def get_warehouse():
    data = request.get_json()   
    query="""MATCH (n:User {id: $user_id})-[:IS_SELLER_OF]->(m) RETURN m"""
    map={"user_id": data.user_id}
    results=session.run(query, map)
    response=results.data() 
    return(json.dumps(response, default=str, ensure_ascii=False).encode('utf8'))



if __name__ == '__main__':
    app.run(debug=True, port=5050)