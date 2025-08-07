from dcf.utils import parse_percentage

def calculate_terminal_value(last_ufcf, terminal_growth_rate, discount_rate):
    """
    Calculate the terminal value using the Gordon Growth Model.

    Parameters:
    - last_ufcf (float): UFCF in the final forecast year.
    - terminal_growth_rate (float or str): Terminal growth rate as percentage (e.g. 2.5 or '2.5%').
    - discount_rate (float or str): Discount rate as percentage (e.g. 8.0 or '8.0%').

    Returns:
    - terminal_value (float): Present value of future UFCFs beyond forecast horizon.
    """
    g = parse_percentage(terminal_growth_rate)
    r = parse_percentage(discount_rate)

    if r <= g:
        raise ValueError("Discount rate must be greater than terminal growth rate.")

    terminal_value = last_ufcf * (1 + g) / (r - g)
    return terminal_value
