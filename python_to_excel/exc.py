import pandas as pd
import os
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data.csv")
output = "output.xlsx"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df.to_excel(output, index=False)
    print(f"Data written in {output}")
else:
    print("File not found")
