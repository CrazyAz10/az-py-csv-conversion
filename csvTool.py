import pandas as pd

pd.__version__

import time

columns = ["Exness", "Symbol", "Timestamp", "Bid", "Ask"]
#
s = time.time()

df = pd.read_csv("./Exness_BTCUSDm_2021.csv", low_memory=False)

df['dateTime'] = pd.to_datetime(df['Timestamp'], format="%Y-%m-%d %H:%M:%S")

stock_df = pd.DataFrame(df).set_index('dateTime')

df.drop(['Timestamp'], axis=1, inplace=True)

df15 = df.resample('15min', on="dateTime").agg({'Exness': 'last',
    'Symbol': 'last',
    'Bid': 'last',
    'Ask': 'last'
})

t = time.time()
t_ = str(t).split('.', 1)[0]

df15.to_csv('C:/Users/CrazyAz/Desktop/'+t_+'.csv')

e = time.time()
print("Pandas Loading Time = {}".format(e-s))
