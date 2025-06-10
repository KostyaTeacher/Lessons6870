import pandas as pd
import matplotlib.pyplot as plt


week = pd.Series({"Понеділок": 90, "Вівторок": 76, "Середа": 51, "Четвер": 39, "П'ятниця": 23, "Субота": 66, "Неділя": 100})
plt.plot(week)
plt.show()

trend = pd.Series({"BMW": 23468, "Mazda": 34567, "Toyota": 45000, "Nisan": 10000})
plt.pie(trend, labels=trend.index, autopct='%1.1f%%')
plt.show()

trend = pd.Series({"BMW": 23468, "Mazda": 34567, "Toyota": 45000, "Nisan": 10000})
plt.bar(trend.index, height=trend)
plt.show()
