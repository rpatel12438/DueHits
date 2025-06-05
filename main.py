import pandas as pd

# Load the CSV file
df = pd.read_csv('topbatters.csv') 

# Show column names
##print(df.columns.tolist())

df.drop(columns = ['Age', 'Lg', 'WAR', 'G', 'R', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'SO', 'OPS+', 'rOBA',
                 'Rbat+', 'TB', 'GIDP', 'HBP', 'SH', 'SF', 'IBB', 'Pos', 'Awards', 'Player-additional'], inplace= True)
# Add "inplace = True" if you don't want to reassign the DataFrame
# No "inplace = True" you had to reassign the DataFrame to a new named dataframe
print(df.head())
df.to_csv('cleaned_batters.csv', index=False)
