#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_226012.html (Sum ends with 90)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context() #zero idea what it does
ctx.check_hostname = False         #same
ctx.verify_mode = ssl.CERT_NONE    #double same

#url = input('Enter - ') #i really dont want to re-enter url everytime during testing
url= 'http://py4e-data.dr-chuck.net/comments_226012.html' #hardcoded url
html= urlopen(url, context=ctx).read()
soup= BeautifulSoup(html,"html.parser")


tags= soup('span')

# zero out the variables
print(html)
sum=0
count=0

for tag in tags:
    num= float(tag.contents[0])
    sum= sum+num
    count= count + 1

print('Item count:', count)
print('Item sum:', sum)
