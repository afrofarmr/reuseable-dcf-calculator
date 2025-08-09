from setuptools import setup, find_packages

setup(
    name="reusabl_dcf_model_tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "xlsxwriter",
    ],
    author="Adegoke Oluwafewa",
    description="A reusable DCF (Discounted Cash Flow) valuation model tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'dcf-model = main:main',
        ],
    },
    python_requires='>=3.8',
    license="MIT",
)
    
