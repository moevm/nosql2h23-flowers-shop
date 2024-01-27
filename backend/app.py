from flask import Flask, json, render_template, request
from flask_cors import CORS
from neo4j import GraphDatabase
import datetime

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "my_password"))


# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r"/*":{'origins':"*"}})


#просмотр каталога
@app.route("/catalog", methods=["GET"])
def get_catalog():
    with driver.session() as session:
        
        query = """MATCH (p:Product) WHERE p.amount > 0 AND p.shelf_life > Date($date) RETURN p;"""

        map={"date": datetime.date.today().strftime("%Y-%m-%d")}

        results=session.run(query, map)
        response=[data['p'] for data in results.data()]
        return(json.dumps(response, default=str, ensure_ascii=False).encode('utf8'))
    

#просмотр склада продавца
@app.route("/<int:user_id>/warehouse", methods=["GET"])     
def get_warehouse(user_id):
    with driver.session() as session: 

        query="""MATCH (n:User {id: $user_id})-[:IS_SELLER_OF]->(m) WHERE m.shelf_life > Date($date) RETURN m"""

        map={"user_id": user_id, "date": datetime.date.today().strftime("%Y-%m-%d")}

        results=session.run(query, map)
        response=[data['m'] for data in results.data()] 
        return(json.dumps(response, default=str, ensure_ascii=False).encode('utf8'))


#добавление продукта на склад
@app.route("/<int:user_id>/warehouse/addProduct", methods=["GET", "POST"])
def addProduct(user_id):
    with driver.session() as session:
        data = request.get_json()

        query = """
        MATCH (n:User {id: $user_id, role: 'Продавец'})
        CREATE (n)-[:IS_SELLER_OF]->(product:Product {id: toInteger($product_id), name: $name, image: $image,\
            price: toFloat($price), shelf_life: Date($shelf_life), description: $description, amount: toInteger($amount)});
        """

        map={"user_id": user_id, "product_id": data.get('product_id'), "name": data.get('name'), "image": data.get('image'),\
            "price": data.get('price'), "shelf_life": data.get('shelf_life'), "description": data.get('dedscription'), "amount": data.get('amount')}

        response = {}
        try:
            session.run(query, map)
            response['status'] = 'success'
            response['message'] = 'The product was successfully added'
        except Exception as e:
            response['status'] = 'failed'
            response['message'] = str(e)
        return(json.dumps(response))


#просмотр корзины
@app.route('/<int:user_id>/cart', methods=["GET"])
def get_cart(user_id):
    with driver.session() as session: 

        query="""MATCH (m:Order {status: 'Оформляется'})-[:IS_CREATED_BY]->(n:User {id: $user_id}) RETURN m"""

        map={"user_id": user_id}

        results=session.run(query, map)
        response=[data['m'] for data in results.data()] 
        return(json.dumps(response, default=str, ensure_ascii=False).encode('utf8'))


#создание/изменение заказа
@app.route('/<int:user_id>/changeOrder', methods=["GET", "POST"])
def change_order(user_id):
    with driver.session() as session: 
        response = {'status':'success'}
        data = request.get_json()

        change_order_query = """
        MATCH (m:User {id: $user_id}), (p:Product {id: $product_id})
        MERGE (o:Order {status: 'Оформляется'})-[:IS_CREATED_BY]->(m)
        ON CREATE SET o.id = toInteger($order_id), o.cost = 0, o.date = Date($date)
        ON MATCH SET o.date = Date($date)
        MERGE (p)-[r:IS_CONTAINED_IN]->(o)
        ON CREATE SET r.amount = toInteger("1"), r.cost = p.price
        ON MATCH SET r.amount = r.amount + 1, r.cost = r.amount * p.price;
        """

        change_cost_query = """
        MATCH (o:Order {id: $order_id})-[:IS_CREATED_BY]->(m), (n)-[r:IS_CONTAINED_IN]->(o)
        WITH o, sum(r.cost) AS sum_cost
        SET o.cost = sum_cost;
        """

        map={"user_id": user_id, "product_id": data.get('product_id'), "order_id": data.get('order_id'), "date": datetime.date.today().strftime("%Y-%m-%d")}
        
        response = {}
        try:
            session.run(change_order_query, map)
            session.run(change_cost_query, map)
            response['status'] = 'success'
            response['message'] = 'The order was successfully changed'
        except Exception as e:
            response['status'] = 'failed'
            response['message'] = str(e)
        return(json.dumps(response))


#просмотр списка заказов пользователя
@app.route('/<int:user_id>/Orders', methods=["GET"])
def get_orders(user_id):
    with driver.session() as session:
        query = """ MATCH (o:Order)-[:IS_CREATED_BY]->(u:User {id: $user_id}) RETURN o;"""

        map={"user_id": user_id}
        
        results=session.run(query, map)
        data=[data['o'] for data in results.data()] 
        return(json.dumps(data, default=str, ensure_ascii=False).encode('utf8'))


#просмотр одного заказа
@app.route('/Orders/<int:order_id>', methods=["GET"])
def get_order(order_id):
    with driver.session() as session:
        query = """MATCH (o:Order {id: $order_id}) RETURN o;"""

        map={"order_id": order_id}

        results=session.run(query, map)
        data=[data['o'] for data in results.data()] 
        return(json.dumps(data, default=str, ensure_ascii=False).encode('utf8'))


#обновление заказа в корзине после ввода адреса и оплаты
@app.route('/<int:user_id>/cart/update', methods=["GET", "POST"])
def update_order(user_id):
    with driver.session() as session:
        data = request.get_json()

        query="""
        MATCH (o:Order {status: 'Оформляется'})-[:IS_CREATED_BY]->(n:User {id: $user_id})
        SET o.delivery_address = $delivery_address, o.delivery_apartment = $delivery_apartment, o.delivery_entrance = $delivery_entrance, \
            o.delivery_floor = $delivery_floor, o.status = 'Оплачен', o.date = Date($date)
        RETURN o;
        """
        map={"user_id": user_id, "delivery_address": data.get('delivery_address'), "delivery_apartment": data.get('delivery_apartment'), \
            "delivery_entrance": data.get('delivery_entrance'), "delivery_floor": data.get('delivery_floor'), \
                "date": datetime.date.today().strftime("%Y-%m-%d")}
        
        response = {}
        try:
            session.run(query, map)
            response['status'] = 'success'
            response['message'] = 'The order was successfully updated'
        except Exception as e:
            response['status'] = 'failed'
            response['message'] = str(e)
        return(json.dumps(response))


if __name__ == '__main__':
    app.run(debug=True, port=5050)