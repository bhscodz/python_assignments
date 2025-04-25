import pandas as pd
import random
import numpy as np
asking_price = pd.Series(random.randint(100,1000) for _ in range(10))
fair_price = pd.Series(random.randint(100,1000) for _ in range(10))
df=pd.DataFrame({"asking_price":asking_price,"fair_price":fair_price})
df["deal"]=(df["asking_price"]<df["fair_price"])
df["deal"]=df["deal"].apply(lambda x:"yes" if x else "no")
print(df)