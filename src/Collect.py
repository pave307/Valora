import requests
from pathlib import Path

LIGUES = {"E0": "premier_league", "SP1": "liga", "D1": "bundesliga",
          "I1": "serie_a", "F1": "ligue_1"}
SAISONS = ["2122", "2223", "2324", "2425", "2526", "2627"]
OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)

for saison in SAISONS:
    for code, nom in LIGUES.items():
        url = f"https://www.football-data.co.uk/mmz4281/{saison}/{code}.csv"
        r = requests.get(url, timeout=30)
        if r.ok:
            (OUT / f"{nom}_{saison}.csv").write_bytes(r.content)
            print("OK", nom, saison)
        else:
            print("Échec", nom, saison)
