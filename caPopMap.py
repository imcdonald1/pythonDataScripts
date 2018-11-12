import cx_Oracle
import plotly
import plotly.plotly as py
import plotly.figure_factory as ff

plotly.tools.set_credentials_file(username='imcdonald1', api_key='rKHp3ElEqqeIOLDKfhUZ')

def checkFips(x):
	if(x < 10):
		strX = str(x)
		strX = '0600' + strX
		return strX
	elif(x>100):
		strX = str(x)
		strX = '06' + strX
		return strX
	else:
		strX = str(x)
		strX = '060' + strX
		return strX

connect = cx_Oracle.connect('user101', 'pass101',cx_Oracle.makedsn('',1521,'XE'));

sql = """
		  select C.county, C.population, F.fipCode
  		  from countyPop C join fips F on UPPER(TRIM(C.county)) = UPPER(TRIM(F.county))
      """

fips = []
values = []

cursor = connect.cursor()
for result in cursor.execute(sql):
    fips.append(checkFips(result[2]))
    values.append(result[1])

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    round_legend_values=True,
    simplify_county=0, simplify_state=0,
    county_outline={'color': 'rgb(15, 15, 55)', 'width': 0.5},
    state_outline={'width': 1},
    legend_title='Pop. per county',
    title='California'
)

py.iplot(fig, filename='California Population')

