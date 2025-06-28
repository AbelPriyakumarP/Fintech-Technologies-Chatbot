from typing import List

# This module defines access rules for different roles and provides a function to get accessible documents based on the user's role.
access_rules = {
    "c-level": [
        "engineering_master_doc.md",
        "employee_handbook.md",
    ],
    "finance": [
        "financial_summary.md",
        "quarterly_financial_report.md",
        "marketing_report_2024.md",
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "employee_handbook.md",
    ],
    "marketing": [
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "marketing_report_2024.md",
        "employee_handbook.md",
    ],
    "engineering": [
        "engineering_master_doc.md",
        "employee_handbook.md",
    ],

    "sales":[
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",  
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "marketing_report_2024.md",
        "employee_handbook.md",
    ],
    
    "risk": [
        "financial_summary.md",
        "quarterly_financial_report.md",
        "marketing_report_2024.md",
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "employee_handbook.md",
    ],
    "quality assurance": [
        "employee_handbook.md",
    ],

    "data":[
        "financial_summary.md",
        "quarterly_financial_report.md",
        "marketing_report_2024.md",
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "employee_handbook.md",
        "hr_data.csv"
    ],
    "product": [
        "financial_summary.md",
        "marketing_report_2024.md",
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "employee_handbook.md",
    ],
    "compliance": [
        "financial_summary.md",
        "quarterly_financial_report.md",
        "marketing_report_2024.md",
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "employee_handbook.md",
        "hr_data.csv"
    ],
    "business": [
        "financial_summary.md",
        "quarterly_financial_report.md",
        "marketing_report_2024.md",
        "market_report_q4_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q1_2024.md",
        "employee_handbook.md",
    ],
    "employee": [
        "hr_data.csv",
        "employee_handbook.md"
    ],
    "general": [
        "employee_handbook.md"
    ],
    "operations":[
        "employee_handbook.md",

    ],
}

# This function retrieves the list of documents accessible to a user based on their role.
def get_accessible_documents(role: str) -> List[str]:
    role_key = role.lower()
    if role_key in access_rules:
        return access_rules[role_key]
    for key in access_rules:
        if key in role_key:
            return access_rules[key]
    return access_rules.get("employee", ["hr_data.csv"])