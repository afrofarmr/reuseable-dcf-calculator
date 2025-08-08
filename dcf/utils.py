def parse_percentage(value):
    """
    Convert a percentage-like value (e.g. 5 or '5%') to decimal (0.05).
    """
    if isinstance(value, str) and '%' in value:
        value = value.replace('%', '')
    return float(value) / 100
