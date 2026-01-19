from loaders.csv_loader import load_players, batting_career, bowling_career

print("Select countires for the Match: ")
print("List of countries: ")

country_a = input("Country A: ")
country_b = input("Country B: ")

countires = [country_a, country_b]
players_df = load_players('data/raw/players.csv', countires)
batting_df = batting_career('data/raw/batting_career.csv')
bowling_df = bowling_career('data/raw/bowling_career.csv')

players_batting_df = players_df.merge(
    batting_df,
    on="player_id",
    how="left"
)

players_bowling_df = players_df.merge(
    bowling_df,
    on="player_id",
    how="left"
)

print(players_batting_df.columns)
print(players_bowling_df.columns)
print()

print(players_batting_df)
print(players_bowling_df.head())