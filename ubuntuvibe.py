from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.ubuntuvibes.com/2017/10/android-pagf-201.html'
page_soup = soup(uReq(my_url).read(), "html.parser")
uReq(my_url).close()
app_name = page_soup.findAll("div",{"class":"pagflistinglink"})
app_price = page_soup.findAll("div",{"class":"pagfoldprice"})
app_game = page_soup.findAll("div",{"class":"pagflistingtype"})
app_discription = page_soup.findAll("div",{"class":"pagfshortdes"})
app_genre = page_soup.findAll("div",{"class":"pagfappcat"})
app_rating = page_soup.findAll("div",{"class":"pagficoncolor"})
temp1=[]
for i in app_rating:
	temp =[]
	for j in i:
		temp.append(j)
	temp1.append(temp)

for m in xrange(len(app_name)):
	temp =temp1[m-1]
	print app_name[m].text[1:]
	if "App" in app_game[m].text[1:]:
		app = "App "
	else:
		app = "Game"
	print app_price[m].text[1:] +" | "+ app +" | "+ app_genre[m].text[1:]
	print app_discription[m].text[1:]
	# print app_genre[m].text[1:]
	print "Rating: "+ temp[2] + "| Download: "+ temp[4]
	print "Last Update  :"+ temp[6]
	if "No" in temp[8]:
		temp[8] = "No   "
	print "Ads: "+ temp[8] +"   | Inapp Purch:  "+ temp[10]
	print app_name[m].a['href']
	print "\n"