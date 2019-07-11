#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.


from urllib.request import urlopen
import json

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_226015.json (Sum ends with 27)


url = 'http://py4e-data.dr-chuck.net/comments_226015.json' #hardcoded url
address = urlopen(url)
data = address.read()

total = 0

while True:

    print(("Retrieving: "), address)
    print(("Retrieved: "),len(data), " characters.")

    info = json.loads(data)
    info = info["comments"]

    for i in info:
        print("Count: ", i["count"])
        total = total + int(i["count"])
        print("Sum: ", total)
    print("Final sum: ", total)
    break
