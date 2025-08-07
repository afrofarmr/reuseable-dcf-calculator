def calculate_wacc(discount_inputs):
    """
    Calculates the Weighted Average Cost of Capital (WACC).

    Parameters:
        discount_inputs (DataFrame): DataFrame containing discount rate assumptions.

    Returns:
        float: The WACC as a decimal (e.g., 0.0669 for 6.69%).
    """
    def get_value(label):
        value = discount_inputs.loc[discount_inputs['Parameter'] == label, 'Value']
        return float(value.values[0]) if not value.empty else 0.0

    beta = get_value('Beta')
    risk_free_rate = get_value('Risk-free Rate (%)') / 100
    market_risk_premium = get_value('Market Risk Premium (%)') / 100
    cost_of_debt = get_value('Cost of Debt (%)') / 100
    debt_ratio = get_value('Debt Ratio (%)') / 100
    equity_ratio = 1 - debt_ratio
    tax_rate = get_value('Tax Rate (%)') / 100  # Optional: could be passed from assumptions

    cost_of_equity = risk_free_rate + beta * market_risk_premium
    after_tax_cost_of_debt = cost_of_debt * (1 - tax_rate)

    wacc = (equity_ratio * cost_of_equity) + (debt_ratio * after_tax_cost_of_debt)
    return wacc
