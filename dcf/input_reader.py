import pandas as pd

def read_input_data(file_path):
    print("📥 Reading input template...")

    assumptions = pd.read_excel(file_path, sheet_name="Assumptions")
    discount = pd.read_excel(file_path, sheet_name="Discount Rate Inputs")
    historical = pd.read_excel(file_path, sheet_name="Historical Financials")
    terminal = pd.read_excel(file_path, sheet_name="Terminal Growth Rate")
    net_debt = pd.read_excel(file_path, sheet_name="Net Debt")

    return assumptions, discount, historical, terminal, net_debt
