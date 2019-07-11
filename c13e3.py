#Extracting Data from XML
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_226014.xml (Sum ends with 85)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# main url : http://py4e-data.dr-chuck.net/comments_226014.xml
# test url : http://py4e-data.dr-chuck.net/comments_42.xml

url= 'http://py4e-data.dr-chuck.net/comments_226014.xml' #hardcoded url
xcontent= urlopen(url).read()
tree= ET.fromstring(xcontent)

values = tree.findall('.//count')
sum = 0
count = 0

for item in values:
    x= int(item.text)
    sum= sum + x
    count= count + 1

print('Retrieving..', url)
print(('Retrieved:'), len(xcontent), 'characters')
print('Count: ', count)
print('Sum: ', sum)
