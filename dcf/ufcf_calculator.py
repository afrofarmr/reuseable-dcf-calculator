import pandas as pd

def project_ufcf(historicals, assumptions):
    # Extract historical revenue
    last_revenue = historicals['Revenue'].iloc[-1]

    # Assumptions
    growth_rate = assumptions.loc[assumptions['Parameter'] == 'Revenue Growth (%)', 'Value'].values[0] / 100
    ebit_margin = assumptions.loc[assumptions['Parameter'] == 'EBIT Margin (%)', 'Value'].values[0] / 100
    tax_rate = assumptions.loc[assumptions['Parameter'] == 'Tax Rate (%)', 'Value'].values[0] / 100
    capex_pct = assumptions.loc[assumptions['Parameter'] == 'CapEx (%)', 'Value'].values[0] / 100
    d_and_a_pct = assumptions.loc[assumptions['Parameter'] == 'D&A (%)', 'Value'].values[0] / 100
    nwc_pct = assumptions.loc[assumptions['Parameter'] == 'NWC (%)', 'Value'].values[0] / 100

    projections = []
    revenue = last_revenue

    for year in range(1, 6):
        revenue *= (1 + growth_rate)
        ebit = revenue * ebit_margin
        tax = ebit * tax_rate
        d_and_a = revenue * d_and_a_pct
        capex = revenue * capex_pct
        change_in_nwc = revenue * nwc_pct

        ufcf = ebit - tax + d_and_a - capex - change_in_nwc

        projections.append({
            'Year': f'Year {year}',
            'Revenue': revenue,
            'UFCF': ufcf
        })

    return pd.DataFrame(projections)
