"""
This file shall load df inputs to postgres database all functions of the project
"""
import os
import pandas as pd
from decouple import config
from sqlalchemy import create_engine

from library import SqlConnection, Extraction, scrape_NBA_team_data

URL = config('db_url')

# df = pd.read_csv("nba_stats_21.csv")

connection = URL

df = scrape_NBA_team_data()

print(df)

df_replace = SqlConnection.to_sql_replace(df, connection, "nba_team_stats_21_snapshot")

df_append = SqlConnection.to_sql_file_append(df, connection, "nba_team_stats_21_incremental")
