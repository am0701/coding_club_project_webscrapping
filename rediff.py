import urllib2
from bs4 import BeautifulSoup
import requests
print "Enter date in format DD/MM/YYYY";

s1=raw_input();
print "printing the headline of ",s1
#s1=s1.replace("/","")
#s1=s1.replace(s1[4:7],s1[6:7])
s4=s1[0:2]+s1[3:5]+s1[8:]
s2="http://www.rediff.com/issues/"
s3="hl.html"
s=s2+s4+s3;
url=urllib2.urlopen(s)
soup=BeautifulSoup(url,'html.parser')
list1=soup.find_all('div',id='hdtab1')
for  x in list1:
	y=x.find('br')
	unwanted=y.find_all('a')
	for z in unwanted:
		z.extract()
	#unwanted=y.find_all('b')
	#for z in unwanted:
	#	z.extract()


txt=y.text

date=[];
n=0;
index=0;
str1="";	
for  n in range(len(txt)):
	if((txt[n]=='T') and (txt[n-1]=='S')and (txt[n-2]=='I')):
		str1=str1+txt[n];date.append(str1);str1="";continue;
	else:
		str1=str1+txt[n];	
url=urllib2.urlopen(s)
soup=BeautifulSoup(url,'html.parser')
list1=soup.find_all('div',id='hdtab1')
l=0
j=0
k=1;
for i in list1:
	a=i.find_all('font',class_='f12')
	for b in a:
		b.extract()
	list2=i.find_all('a')
	for j in range(len(list2)):
			if(j<=1):
				print list2[j].text				
				continue			
			else:
					
				print k,">>",list2[j].text,date[l];
				l=l+1;k=k+1;




 
