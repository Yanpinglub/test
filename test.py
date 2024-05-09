import pandas as pd

# Specify the path to your Excel file
excel_file = '/path/to/your/excel/file.xlsx'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Print the contents of the DataFrame
print(df)