import pandas as pd

def calculate_delay_metrics(dataframe: pd.DataFrame):
    grouped = dataframe.groupby("event_type").size().reset_index(name="count")
    return grouped.to_dict(orient="records")