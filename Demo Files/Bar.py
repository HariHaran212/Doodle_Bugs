import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/user/OneDrive/Desktop/SIH-GIT/data-2.csv")

df = df[df['SUBDIVISION']=='ANDAMAN & NICOBAR ISLANDS']

df = df[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']]

x_values = list()
y_values = list()

for month in df:
    print(month);
    x_values.append(month);
    y_values.append(df[month].sum()/len(df[month]));
    
print(x_values)
print(y_values)

plt.bar(x_values, y_values, color='#87CEEB')

plt.title('Bar Graph')
plt.ylabel('Rainfall')

plt.show()


