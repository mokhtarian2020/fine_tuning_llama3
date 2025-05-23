# convert_csv_to_alpaca.py
import pandas as pd
import json

df = pd.read_csv("emails.csv")
alpaca = [
    {
        "instruction": "Classify the following email",
        "input": row["text"],
        "output": row["label"]
    }
    for _, row in df.iterrows()
]

with open("emails_alpaca.json", "w", encoding="utf-8") as f:
    json.dump(alpaca, f, ensure_ascii=False, indent=2)

