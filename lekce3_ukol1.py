import requests
import pandas
import numpy


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pandas.read_csv("lexikon-zvirat.csv", sep=";")
lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.dropna(how="all", axis="rows")
lexikon = lexikon.set_index("id")
lexikon = lexikon["image_src"].astype(str)

def check_url(radek):
        check_str = isinstance(radek.image_src, str)
        check_start = radek.image_src.startswith("https://zoopraha.cz/images/")
        check_end = radek.image_src.endswith("jpg") or radek.image_src.endswith("JPG")
        check_all = check_str and check_start and check_end
        for radek in lexikon.itertuples():
            check_url(radek)
            print(radek.title)
        else:
            print(radek.title)