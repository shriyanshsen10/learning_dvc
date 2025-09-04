import pandas as pd # type: ignore
import os

data  = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
         'Age': [24, 27, 22, 32, 29],
         'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
        }

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'people.csv')
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")

print(df)