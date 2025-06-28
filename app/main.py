from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from app.services.data_access import get_accessible_documents, access_rules
from app.services.rag import process_query
import pandas as pd

app = FastAPI()

# Function to get user information based on employee ID
def get_user_info(employee_id: str):
    df = pd.read_csv("resources/data/hr/hr_data.csv")
    user_row = df[df["employee_id"] == employee_id]
    if user_row.empty:
        return None
    user = user_row.iloc[0]
    return {
        "employee_id": user["employee_id"],
        "full_name": user["full_name"],
        "role": user["role"],
        "department": user["department"],
        "email": user["email"]
    }

# Data models for request and response
class QueryRequest(BaseModel):
    query: str
    user_id: str

class QueryResponse(BaseModel):
    response: str
    sources: list

# Endpoint to get user information by employee ID
@app.get("/user_info")
async def user_info(full_name: str = Query(...)):
    df = pd.read_csv("resources/data/hr/hr_data.csv")
    user_row = df[df["full_name"].str.lower() == full_name.lower()]
    if user_row.empty:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_row.iloc[0]
    return {
        "employee_id": user["employee_id"],
        "full_name": user["full_name"],
        "role": user["role"],
        "department": user["department"],
        "email": user["email"]
    }

# Endpoint to handle queries
@app.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    user = get_user_info(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    role = user["role"].lower()
    department = user["department"].lower()
    print("User role:", role)
    print("User department:", department)

    # C-level: all docs
    if "c-level" in role:
        selected_role = "c-level"
    # Department-based: use department access rule if it exists
    elif department in access_rules:
        selected_role = department
    # Otherwise: employee/general
    else:
        selected_role = "employee"
    print("Docs being indexed for this user/role:", get_accessible_documents(selected_role))

    response, sources = process_query(request.query, selected_role)
    return QueryResponse(response=response, sources=sources)