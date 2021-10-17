import pandas
import psycopg2
from sqlalchemy import create_engine, inspect
import numpy

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "z.drbalova"
USERNAME = f"z.drbalova@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "d5vDcvL?NnfhwwTk"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

inspector = inspect(engine)
#print(inspector.get_table_names())

crime = pandas.read_sql("crime", con=engine)
crime_table = crime[["PRIMARY_DESCRIPTION","SECONDARY_DESCRIPTION","DATE_OF_OCCURRENCE"]]
crime_table = crime_table[crime_table["PRIMARY_DESCRIPTION"] == "MOTOR VEHICLE THEFT"]
crime_table = crime_table[crime_table["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"]
crime_table["MONTH"] = pandas.to_datetime(crime_table["DATE_OF_OCCURRENCE"]).dt.month
print(crime_table.groupby("MONTH").count().sort_values(by="PRIMARY_DESCRIPTION", ascending=False))
