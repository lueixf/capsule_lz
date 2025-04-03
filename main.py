import pandas as pd
import matplotlib.pyplot as plt

avocado = pd.read_csv('avocado.csv')
x = avocado['date'].tolist()
y = avocado['price'].tolist()
plt.plot(x, y, label='Avocado')
plt.xlabel('Date')
plt.ylabel('Prise')
plt.title('СТОИМОСТЬ АВОКАДО')
plt.colormaps
plt.show()





