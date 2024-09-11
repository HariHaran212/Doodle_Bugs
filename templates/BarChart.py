#import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

df = pd.read_csv("C:/Users/user/OneDrive/Desktop/SIH-GIT/data-2.csv")

df = df[(df['SUBDIVISION']=='KERALA')]

df = df[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']]

x_values = list()
y_values = list()

for month in df:
    print(month);
    x_values.append(month);
    y_values.append(df[month].sum()/len(df[month]));
    
#print(x_values)
#print(y_values)

#plt.bar(x_values, y_values, color='#87CEEB')

#plt.title('Bar Graph')
#plt.ylabel('Rainfall')

#plt.show()


# Create a simple bar chart
# fig = go.Figure([go.Bar(x=x_values, y=y_values)])

fig = go.Figure([go.Scatter(x=x_values, y=y_values, mode='lines')])

# Export as an HTML file
pio.write_html(fig, file='Graph.html', auto_open=False)

