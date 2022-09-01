import pandas as pd
from matplotlib import pyplot as plt


stock_df = pd.read_excel(r"C:\Users\dalty\PycharmProjects\pythonProject10\stock_prices.xltx")
plt.style.use("ggplot")
stock_df_index = stock_df.index
stock_df_cols = stock_df.columns
price_y = []
year_x = []
for year in range(50):
    year_x.append(stock_df["year"][year])
num = 49
for price in stock_df["avg_price"][49:103]:
    price_y.append(stock_df["avg_price"][num])
    num += 1
plt.style.use('ggplot')
df = pd.read_excel(r"C:\Users\dalty\Documents\Custom Office Templates\listings.xltx")
df_index = df.index
df_cols = df.columns
room_x = []
room_price_y = []

sorted_listings = df.sort_values(by="room_type")

for i in range(len(sorted_listings)):
    room_x.append(sorted_listings['room_type'][i])
    room_price_y.append(sorted_listings['price'][i])

plt.bar(x, y)
plt.xlabel('Room Types')
plt.ylabel('Price Range')
plt.title('Price Range per Room Type')
plt.show()
price_y.remove(price_y[0])
plt.plot(year_x, price_y, marker=".")
plt.xlabel("Years")
plt.ylabel("Average Stock Prices")
plt.title("Average Walmart Stock Price Per Year")
plt.grid(True)
plt.show()
