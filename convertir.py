import pandas as pd

# Llegim el CSV
df = pd.read_csv("Esfestamajor.csv")

# Convertim a JSON
df.to_json("Esfestamajor.json", orient="records", force_ascii=False, indent=2)

print("Conversió completada! Fitxer guardat com Esfestamajor.json")
