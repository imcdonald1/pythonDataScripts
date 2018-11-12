import matplotlib.pyplot as plt
import cx_Oracle
import numpy as np

connect = cx_Oracle.connect('user101', 'pass101',cx_Oracle.makedsn('',1521,'XE'));

sql = """
		select county, num_of_females, num_of_males from doctors
      """

county = []
females = []
males = []

cursor = connect.cursor()
for result in cursor.execute(sql):
	county.append(result[0])
	females.append(result[1])
	males.append(result[2])


N = len(county)
ind = np.arange(N)
width = 0.4

p1 = plt.bar(ind, females, width, color='#FF66C1')
p2 = plt.bar(ind, males, width, bottom=females, color='blue')
plt.xticks(ind, county, rotation=90)
plt.legend((p1[0], p2[0]), ('Women', 'Men'))
plt.ylabel('Num of Doctors')
plt.xlabel('County')
plt.title('Number of Male and Female Doctors Per County')
plt.show()