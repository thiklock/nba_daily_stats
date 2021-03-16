"""
This file shall load df inputs to postgres database all functions of the project
"""
import os
from library import SqlConnection, Extraction
import pandas as pd
from decouple import config
from sqlalchemy import create_engine


URL = config('db_url')



df = pd.read_csv("nba_stats_21.csv")

connection = URL

df_replace = SqlConnection.to_sql_replace(df, connection, "nba_stats_21_snapshot")

df_append = SqlConnection.to_sql_file_append(df, connection, "nba_stats_21_incremental")