from loaders.csv_loader import load_players, batting_career, bowling_career


players_df = bowling_career("data/raw/bowling_career.csv")

print(players_df)