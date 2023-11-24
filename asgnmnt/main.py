from fastapi import FastAPI,HTTPException,Depends
import psycopg2
from pydantic import BaseModel
import db_conn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pandas as pd

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
async def get_current_user(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
 
    if username != "shahed" or password != "shahed":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return username


app =FastAPI()
def get_connection(host,database,user,password):
    conn = psycopg2.connect(
        host='localhost',
        database='shahed',
        user='shahed',
        password='shahed')
    return conn
 
class items(BaseModel):
    user_id:int
    start_date:str
    end_date:str
    reason:str

 
@app.post('/apply_leave/{user_id}',dependencies=[Depends(get_current_user)])
def apply_leave(request:items):
    try:
        conn = db_conn.get_connection('localhost','shahed','shahed','shahed')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaves (user_id, start_date, end_date, reason) VALUES ('%s', '%s','%s','%s')"%(request.user_id,request.start_date, request.end_date,request.reason))
    conn.commit()
    conn.close()
    if not request.start_date or not request.end_date or not request.reason:
        raise HTTPException(status_code=400, detail='missing required parameters')
    return {'message':'leave application submitted successfully'}
 

# @app.post('/send_notification/{manager_email}')
# def send_notification(manager_id:int, manager_email:str, user_id:int):
#     try:
#         conn = db_conn.get_connection('localhost','shahed','shahed','shahed')
#         if not manager_id:
#             raise HTTPException(status_code=400, detail='user missing required parameter')
#         if not user_id:
#             raise HTTPException(status_code=401, detail='user not authenticated')
#         return {'messege':'Notification sent successfully to {manager_email}'}
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# Assuming data is a DataFrame containing your dataset
data = pd.DataFrame({
    "user_id": [1, 2, 3, 1, 2],
    "start_date": ["2023-11-01", "2023-11-02", "2023-11-03", "2023-11-04", "2023-11-05"],
    "end_date": ["2023-11-03", "2023-11-04", "2023-11-05", "2023-11-06", "2023-11-07"],
    "reason": ["Vacation", "Sick", "Personal", "Vacation", "Sick"]
})

# User input for filtering
user_id_filter = 1
date_filter_start = "2023-11-01"
date_filter_end = "2023-11-05"

# Apply filters
filtered_data = data[(data['user_id'] == user_id_filter) & (data['start_date'] >= date_filter_start) & (data['end_date'] <= date_filter_end)]

# Save the filtered data to a CSV file
filtered_data.to_csv("filtered_report.csv", index=False)
