import numpy as np
import pandas as pd
import tstables as tt


no = 5000000
co = 3
interval = 1. / (12 * 30 * 24 * 60)
vol = 0.2

rn = np.random.standard_normal((no, co))
rn[0] = 0.0
paths = 100 * np.exp(np.cumsum(-0.5 * vol ** 2 * interval + vol * np.sqrt(interval) * rn, axis=0))
paths[0] = 100
dr = pd.date_range('2019-1-1', periods=no, freq='1s')
#print(dr[-6:])
df = pd.DataFrame(paths, index=dr, columns=['ts1', 'ts2', 'ts3'])
print(df[-6:])
