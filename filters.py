import pandas as pd

def filter_stat(csv_file):
  df = pd.read_csv(csv_file)
  
  threshold = 0.265
  above_threshold = []
  for index, row in df.iterrows():
    if row['BA▼'] > threshold:
      above_threshold.append(row['Player'])

  for player in above_threshold:
    print(player)
      
      

