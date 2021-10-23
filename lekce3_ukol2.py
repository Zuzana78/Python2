import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pandas.read_csv("lexikon-zvirat.csv", sep=";")
lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.dropna(how="all", axis="rows")
lexikon = lexikon.set_index("id")


def popisek(radek):
    lexikon_popisek = f" {radek.title} preferuje následující typ stravy: {radek.food}." +\
                      f" Konkrétně ocení když mu do misky přistanou {radek.food_note}." +\
                      f" Jak toto zvíře poznáme:{radek.description}."
    return lexikon_popisek


lexikon["popisek_zvirete"] = lexikon.apply(popisek, axis=1)
print(lexikon)


