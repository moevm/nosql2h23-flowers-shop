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


if __name__ == '__main__':
    app.run(debug=True, port=5050)