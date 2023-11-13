import sqlite3
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Veritabanı bağlantısı oluşturma
conn = sqlite3.connect('data/db.sqlite3')
cursor = conn.cursor()

# Veritabanından verileri çekme
cursor.execute("SELECT employee_age, employee_salary FROM employees")
data = cursor.fetchall()

# Verileri bir DataFrame'e dönüştürme
df = pd.DataFrame(data, columns=['Yaş', 'Maaş'])

# Grafik oluşturma
sns.regplot(data=df, x='Yaş', y='Maaş', scatter_kws={'color': 'blue'}, line_kws={'color': 'red'}, ci=None)
plt.xlabel('Yaş')
plt.ylabel('Maaş')
plt.title('Yaşa Göre Maaş Durumu')
plt.show()

# Veritabanı bağlantısını kapatma
conn.close()