# Reusable DCF Model Tool

This project is my bsaic implementation of a reusable, Excel-based Discounted Cash Flow (DCF) valuation tool written in Python.
It reads financial inputs from an Excel spreadsheet, calculates projected Free Cash Flows, WACC, Terminal Value, and derives the Enterprise & Equity Value.

## 📦 Features

- Projects UFCF (Unlevered Free Cash Flow) from assumptions
- Calculates WACC from inputs
- Computes terminal value (Gordon Growth Model) and enterprise value
- Outputs to Excel
- Fully modular and reusable code

## 📂 Structure
dcf/
├── input_reader.py # Reads input Excel
├── ufcf_calculator.py # Projects UFCF
├── discount_rate.py # Calculates WACC
├── terminal_value.py # Calculates terminal value
├── valuation.py # Orchestrates full valuation
├── utils.py # Excel export and helpers

## 📊 How to Use

1. Install dependencies: (```bash
pip install -r requirements.txt)
2. Add your inputs to input_template.xlsx
3. Run the tool: (python main.py)
4. Output will be saved as dcf_valuation_output.xlsx
