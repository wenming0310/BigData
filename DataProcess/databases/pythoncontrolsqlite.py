import sqlite3
conn = sqlite3.connect('D:\CC++C#Code\github\BigData\DataProcess\iris.sqlite')

c = conn.cursor()

#c.row_factory = sqlite3.Row

c.execute('SELECT * FROM  iris')
results = c.fetchone()

print(results)
#print(results['id'])
#print(results['PetalLengthCm'])