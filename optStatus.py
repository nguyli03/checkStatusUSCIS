# importing the requests library
import requests

# api-endpoint
URL = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=';
PREFIX = "XXX" #your prefix in the receipt number
START_NUMBER = "your number - range (so 100 for example)"
MINE = "your number"
END_NUMBER = "your number + range"

f =open('before.txt','w')
# sending get request and saving the response as response object
for i in range(START_NUMBER,MINE+1):
    r = requests.get(URL+PREFIX+str(i))
    f.write(r.text)
f.close()

f =open('after.txt','w')
for i in range(MINE,END_NUMBER+1):
    r = requests.get(URL+PREFIX+str(i))
    f.write(r.text)
f.close()
print('done')
