import pandas as pd
import pytest


dict = {"a": ["123","124"], "b" : ["456","457"]}
df = pd.DataFrame(dict)
print("Below is the dataframe")
print(df)

#raise Exception