from typing import Dict
import pandas as pd


def get_user_info(employee_id: str) -> Dict:
    """
    Looks up user info by employee_id from the HR CSV file.
    Returns a dictionary with employee_id, full_name, role, department, and email.
    """
    df = pd.read_csv("resources/data/hr/hr_data.csv")
    user_row = df[df["employee_id"] == employee_id]
    if not user_row.empty:
        user = user_row.iloc[0]
        return {
            "employee_id": user["employee_id"],
            "full_name": user["full_name"],
            "role": user["role"],
            "department": user["department"],
            "email": user["email"]
        }
    return None

authenticate_user = get_user_info