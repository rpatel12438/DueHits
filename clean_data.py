import pandas as pd

def clean_data():
    # Load the CSV file
    df = pd.read_csv('topbatters.csv')

    # Drop unwanted columns
    df.drop(columns=[
        'Age', 'Lg', 'WAR', 'G', 'R', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'SO',
        'OPS+', 'rOBA', 'Rbat+', 'TB', 'GIDP', 'HBP', 'SH', 'SF', 'IBB', 'Pos',
        'Awards', 'Player-additional'
    ], inplace=True)

    # Print first few rows
    print(df.head())

    # Save cleaned dataframe to new CSV
    df.to_csv('cleaned_batters.csv', index=False)
