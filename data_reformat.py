import os, yaml
import pandas as pd
with open("IPL_data/335982.yaml") as f:
    dataMap = yaml.safe_load(f)
first_innings_deliveries = dataMap['innings'][0]["1st innings"]["deliveries"]
print(type(first_innings_deliveries))