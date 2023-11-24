from fastapi import FastAPI,HTTPException
import psycopg2
from pydantic import BaseModel
import db_conn
 
 
 
app =FastAPI()
def get_connection(host,database,user,password):
    conn = psycopg2.connect(
        host='localhost',
        database='shahed',
        user='shahed',
        password='shahed')
    return conn
 
 
@app.get("/get_user/{id}")
def get_user(id):
    if id is not None:
    
        conn = get_connection("localhost","shahed","shahed","shahed")
        cur = conn.cursor()
        cur.execute("select * from employees where id=%s;",(id,))
        rows = cur.fetchone()
        cur.close()
        conn.close()
        if rows is None:
            raise HTTPException(status_code=404, detail="details not found")
        return rows
        
    
class items(BaseModel):
    id:int
    name:str
    age:int
    email:str
    position:str

@app.post('/items')
 
def create_items(request : items):
    try:
        conn = db_conn.get_connection('localhost','shahed','shahed','shahed')
    except Exception as e:
        print(e);    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (id, name, age,email,position) VALUES ('%s', '%s','%s','%s','%s')"%(request.id,request.name, request.age,request.email,request.position))
    conn.commit()
    conn.close()
    if request.id and request.email:
        raise HTTPException(status_code=500, detail=f"Entered data already exists")
    return {'data':f"items is Created {request} response"}

@app.put('/items/{id}')
def modify_items(id: int, modify: items):
    conn = db_conn.get_connection('localhost', 'shahed', 'shahed', 'shahed')  
    cursor = conn.cursor()
    query = "UPDATE employees SET id=%s, name=%s, age=%s, email=%s, position=%s WHERE id=%s"
    values = (modify.id, modify.name, modify.age, modify.email, modify.position, id)
    row = cursor.execute(query, values)
    updated_rows = cursor.rowcount
    if updated_rows > 0:
        conn.commit()
        conn.close()
        return {'data': 'Item is Updated'}
    else:
        conn.close()
        raise HTTPException(status_code=404, detail="details not found")

@app.delete('/items/{id}')
def delete_item(id:int):
    try:
        conn = db_conn.get_connection('localhost','shahed','shahed','shahed')
    except Exception as e:
        print(e)
    cursor = conn.cursor()
    query= "DELETE FROM employees WHERE id=%s"
    row=cursor.execute(query,(id,))
    updated_rows = cursor.rowcount 
    if updated_rows > 0:
        conn.commit()
        conn.close()
        return {'data': 'Item is Deleted'}
    else:
        conn.close()
        raise HTTPException(status_code=404, detail="details not found")
    



