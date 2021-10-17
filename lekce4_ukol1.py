import os
import matplotlib.pyplot as plt
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

dreviny = pandas.read_sql("dreviny", con=engine)
#print(dreviny)

smrk = dreviny[dreviny["dd_txt"] == "Smrk, jedle, douglaska"]
#print(smrk)
smrk.sort_values(by="rok").plot.bar( x="rok", y="hodnota", title="tezba smrk, jedle, douglaska")


nahodila_tezba = dreviny[dreviny["druhtez_txt"] == "Nahodilá těžba dřeva"]
pivot_tezba = pandas.pivot_table(nahodila_tezba, values="hodnota", index="rok", columns="prictez_txt", aggfunc=numpy.sum)
#print(pivot_tezba)

pivot_tezba.plot()
plt.show()
