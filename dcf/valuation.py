from dcf.discount_rate import calculate_wacc
from dcf.ufcf_calculator import project_ufcf, discount_ufcf
from dcf.terminal_value import calculate_terminal_value

def perform_valuation(assumptions, discount_inputs, historicals, terminal_inputs, net_debt_inputs):
    """
    Coordinates the DCF valuation process.

    Returns:
        - ufcf_df (DataFrame): Yearly projected UFCF and discounted UFCF
        - valuation_summary (dict): Summary including WACC, Terminal Value, Enterprise Value, Equity Value
    """
    # Step 1: Calculate WACC
    wacc = calculate_wacc(discount_inputs)

    # Step 2: Project UFCF
    ufcf_df = project_ufcf(assumptions, historicals)

    # Step 3: Discount UFCF
    ufcf_df = discount_ufcf(ufcf_df, wacc)

    # Step 4: Terminal Value Calculation
    terminal_growth_rate = terminal_inputs.loc[
        terminal_inputs['Parameter'] == 'Terminal Growth (%)', 'Value'
    ].values[0]
    last_ufcf = ufcf_df['UFCF'].iloc[-1]
    terminal_value = calculate_terminal_value(last_ufcf, terminal_growth_rate, wacc)

    # Step 5: Discount Terminal Value
    final_year = len(ufcf_df)
    discounted_terminal_value = terminal_value / ((1 + wacc) ** final_year)

    # Step 6: Enterprise Value
    enterprise_value = ufcf_df['Discounted UFCF'].sum() + discounted_terminal_value

    # Step 7: Equity Value
    net_debt = net_debt_inputs.loc[
        net_debt_inputs['Parameter'] == 'Net Debt', 'Value'
    ].values[0]
    equity_value = enterprise_value - net_debt

    # Step 8: Summary
    valuation_summary = {
        'WACC': wacc,
        'Terminal Value': terminal_value,
        'Discounted Terminal Value': discounted_terminal_value,
        'Enterprise Value': enterprise_value,
        'Equity Value': equity_value
    }

    return ufcf_df, valuation_summary
