from neo4j import GraphDatabase

def db_auth(url, name, password):
    driver = GraphDatabase.driver(url, auth=(name, password))
    return driver