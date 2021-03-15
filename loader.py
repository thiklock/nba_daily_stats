"""
This file shall load df inputs to postgres database all functions of the project
"""

from library import SqlConnection, Extraction
import pandas as pd
from sqlalchemy import create_engine



df = pd.read_csv("nba_stats_21.csv")

connection = connection

df_replace = SqlConnection.to_sql_replace(df, connection, "nba_stats_21_snapshot")

df_append = SqlConnection.to_sql_file_append(df, connection, "nba_stats_21_incremental")