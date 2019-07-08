import os, yaml
import pandas as pd
with open("IPL_data/335982.yaml") as f:
    dataMap = yaml.safe_load(f)
print(type(dataMap))
print(list(dataMap))
innings = dataMap['innings'][0]
print(type(innings["1st innings"]["deliveries"][0]))
