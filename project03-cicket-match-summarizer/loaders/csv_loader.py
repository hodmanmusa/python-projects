import pandas as pd
from pathlib import Path

REQUIRED_PLAYER_COLUMNS = {
    "player_id",
    "name",
    "nationality",
    "age",
    "primary_role",
}

REQUIRED_BATTING_COLUMNS = {
    "player_id",
    "innings",
    "runs",
    "highest_score",
}

REQUIRED_BOWLING_COLUMNS = {
    "player_id",
    "innings",
    "balls_bowled",
    "runs_conceded",
    "wickets",
}


def validate_required_columns(df, required_columns, file_name):
    missing = required_columns - set(df.columns)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(
            f"{file_name} is missing required column(s): {missing_list}"
        )


def load_players(csv_path: str, countries: list[str]):
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"Players file not found: {path}")

    df = pd.read_csv(path)
    
    # Filter by countries
    df = df[df["nationality"].isin(countries)]
    if df.empty:
        raise ValueError(f"No players found for countries: {countries}")
    
    validate_required_columns(df, REQUIRED_PLAYER_COLUMNS, "players.csv")

    if df["name"].isnull().any():
        raise ValueError(
            "Invalid data in players.csv: column 'name' contains missing values."
        )

    if (df["age"] <= 0).any():
        raise ValueError(
            "Invalid data in players.csv: column 'age' must contain positive values."
        )

    return df


def batting_career(csv_batting_path: str):
    path = Path(csv_batting_path)

    if not path.exists():
        raise FileNotFoundError(f"Batting career file not found: {path}")

    df = pd.read_csv(path)
    
    validate_required_columns(df, REQUIRED_BATTING_COLUMNS, "batting_career.csv")

    for column in ["innings", "runs", "highest_score"]:
        if (df[column] < 0).any():
            raise ValueError(
                f"Invalid data in batting_career.csv: column '{column}' "
                f"cannot contain negative values."
            )

    return df


def bowling_career(csv_bowling_path: str):
    path = Path(csv_bowling_path)

    if not path.exists():
        raise FileNotFoundError(f"Bowling career file not found: {path}")

    df = pd.read_csv(path)

    
    validate_required_columns(df, REQUIRED_BOWLING_COLUMNS, "bowling_career.csv")

    for column in ["innings", "balls_bowled", "runs_conceded", "wickets"]:
        if (df[column] < 0).any():
            raise ValueError(
                f"Invalid data in bowling_career.csv: column '{column}' "
                f"cannot contain negative values."
            )

    return df
