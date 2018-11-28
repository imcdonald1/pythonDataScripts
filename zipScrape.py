import requests
from bs4 import BeautifulSoup


url = 'https://www.zip-codes.com/state/ca.asp'
response = requests.get(url)
htmlResponse = BeautifulSoup(response.text, 'html.parser')
zipList = htmlResponse.find_all('table', class_='statTable')

zipRows = zipList[0].find_all('tr')

finalList = list()

for i in range(len(zipRows)):
	zipTD = zipRows[i].find_all('td')
	zipCode = zipTD[0].a.text[9:]
	city = zipTD[1].a.text
	county = zipTD[2].a.text
	infoTuple = (zipCode, city, county)
	finalList.append(infoTuple)

print(finalList[i][0]+ ',' + finalList[i][1] + ',' + finalList[i][2])
