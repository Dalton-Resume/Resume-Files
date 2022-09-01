import psycopg2
from matplotlib import pyplot as plt

plt.style.use("ggplot")

toyota_x = ["Toyota"]
toyota_y = []

cadillac_x = ["Cadillac"]
cadillac_y = []

conn = psycopg2.connect(
   database="mock_data", user='postgres', password='Dimn@dnftt23', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()
cursor2 = conn.cursor()

sql = '''SELECT car_price FROM mock_data WHERE car_make = \'Toyota\''''
sql2 = '''SELECT car_price FROM mock_data WHERE car_make = \'Cadillac\''''

cursor.execute(sql)
cursor2.execute(sql2)

for price in cursor.fetchall():
    toyota_y.append(float(price[0][1:]))

for price2 in cursor2.fetchall():
    cadillac_y.append(float(price2[0][1:]))


conn.commit()

conn.close()


plt.bar(toyota_x, toyota_y, width=.4)
plt.bar(cadillac_x, cadillac_y, width=.4)
plt.xlabel("Car Makes")
plt.ylabel("Price Ranges ($)")
plt.title("Price Ranges of Toyota and Cadillac Cars")
plt.show()
