import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


plt.style.use('ggplot')
df = pd.read_excel(r"C:\Users\dalty\Documents\Custom Office Templates\listings.xltx")
df_index = df.index
df_cols = df.columns
x_values = []
y_values = []
x1_values = []
y1_values = []
hotel_x = []
hotel_y = []
shared_x = []
shared_y = []
for i in range(len(df['room_type'])):
    if df['room_type'][i] == "Entire home/apt":
        y_values.append(int(df['price'][i]))
        x_values.append(df['room_type'][i])
    elif df['room_type'][i] == "Private room":
        y1_values.append(int(df['price'][i]))
        x1_values.append(df['room_type'][i])
    elif df['room_type'][i] == "Hotel room":
        hotel_y.append(int(df['price'][i]))
        hotel_x.append(df['room_type'][i])
    elif df['room_type'][i] == "Shared room":
        shared_y.append(int(df['price'][i]))
        shared_x.append(df['room_type'][i])
    else:
        pass
plt.bar(x_values, sorted(y_values), label='Entire Home')
plt.bar(x1_values, sorted(y1_values), label='Private Room')
plt.bar(hotel_x, sorted(hotel_y), color='#444444', label='Hotel Room')
plt.bar(shared_x, sorted(shared_y), label='Shared Room')
plt.xlabel('Room Types')
plt.ylabel('Price Range')
plt.title('Price Range per Room Type')
plt.legend()
plt.show()
