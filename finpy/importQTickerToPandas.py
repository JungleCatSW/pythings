import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from capm import *

start_date = '2009-01-01'
end_date = '2018-01-01'

dates = pd.date_range(start_date,end_date)
df = pd.DataFrame(index=dates)

AAPL = pd.read_csv('tickerData/AAPL.txt',
                    index_col="DATE",
                    parse_dates=True,
                    usecols=['DATE', ' CLOSE'],
                    na_values=['nan'])

SPY = pd.read_csv("data/SPY.csv",
                    index_col="Date",
                    parse_dates=True,
                    usecols=['Date','Close'],
                    na_values=['nan'])

df = df.join(SPY, how='inner')
df = df.join(AAPL)

#print(df['Close'])

df.plot.scatter('Close', ' CLOSE')
#plt.show()

#m = df.as_matrix()
#print(df.as_matrix())
m = df.values
#print(m[:, 1])

plt.figure(2)
x = m[:, np.newaxis, 1]
y = m[:, np.newaxis,  0]
plt.scatter(x,y)
plt.scatter(x,capm1(x,y))
#print(m[:,1])
#print(m[:, np.newaxis, 1])
y_pred = multi_capm(m[:,1], m[:,0], 30)
plt.figure(3)
plt.plot(y_pred)
plt.show()
#plt.show()



