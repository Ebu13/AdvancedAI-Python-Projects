import sqlite3
import matplotlib.pyplot as plt

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('data/db.sqlite3')
cursor = conn.cursor()

# Verileri sorgula
cursor.execute("SELECT employee_age, employee_salary FROM employees")
rows = cursor.fetchall()

# Verileri diziye aktar
ages = []
salaries = []
for row in rows:
    ages.append(row[0])
    salaries.append(row[1])

# Veritabanı bağlantısını kapat
conn.close()

# Grafik oluştur
plt.plot(ages, salaries)
plt.xlabel('Yaş')
plt.ylabel('Maaş')
plt.title('Yaşa Göre Maaş Artışı')
plt.show()
