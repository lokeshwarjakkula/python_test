import pandas as pd
import io

# Ask the user for the file path (or set it directly)
filename = 'C:/Users/LokeshwarJakkula/downloads/F05_ScheduledShifts-05nov.txt'  # Replace with your actual file path

# Read the text file into a list of lines
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Convert the list of lines into a DataFrame
df = pd.DataFrame([line.strip().split(';') for line in lines[1:]], columns=lines[0].strip().split(';'))

# Display the first few rows to verify the import
print(df.head())

# Save the DataFrame to an Excel file
output_filename = 'C:/Users/LokeshwarJakkula/downloads/F05_ScheduledShifts-05nov.xlsx'
df.to_excel(output_filename, index=False)
print(f"Data has been saved to {output_filename}")
