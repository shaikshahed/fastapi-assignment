import psycopg2
 
def get_connection(host,database,user,password):
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)
    return conn