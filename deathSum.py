import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import cx_Oracle


connect = cx_Oracle.connect('user101', 'pass101',cx_Oracle.makedsn('',1521,'XE'));

sql = """
        select year, sum(total_num) 
        from death
        group by year
        order by year asc
      """

queryYears = []
querySum = []

cursor = connect.cursor()
for result in cursor.execute(sql):
	queryYears.append(result[0])
	querySum.append(result[1])

yearsPredict = [2012, 2013,2014,2015,2016,2017,2018,2019,2020]

xs = np.array(queryYears, dtype=np.float64)
ys = np.array(querySum, dtype=np.float64)

def best_fit_slope(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))
    b = mean(ys) - m*mean(xs)
    
    return m, b
    
m,b = best_fit_slope(xs, ys)
regression_line = [(m*x)+b for x in yearsPredict]


plt.plot(queryYears, querySum, label='Total Deaths', color='blue')
plt.plot(yearsPredict, regression_line, 'o', color='red')
plt.plot(yearsPredict, regression_line, label='Predicted Deaths', color='red')
plt.ylabel('Deaths')
plt.xlabel('Year')
plt.axis([2012,2020,240000,280000])
plt.legend()
plt.title('California Deaths Per Year')
plt.show()
