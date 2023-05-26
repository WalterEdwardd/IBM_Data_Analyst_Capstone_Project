#Requests is a python Library that allows you to send HTTP/1.1 requests easily. We can import the library as follows:
import requests
#We will also use the following libraries
import os 
from PIL import Image
from IPython.display import IFrame
#You can make a GET request via the method get to www.ibm.com:
url='https://www.ibm.com/'
r=requests.get(url)
#We have the response object r , this has information about the request, like the status of the request. We can view the status code using the attribute status_code 
r.status_code
#You can view the request headers:
print(r.request.headers)
#You can view the request body, in the following line, as there is no body for a get request we get a None :
print("request body:", r.request.body)
#You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.
header=r.headers
print(r.headers)
#We can obtain the date the request was sent using the key Data
header['date']
#Content-Type indicates the type of data:
header['Content-Type']
#You can also check the encoding:
r.encoding
#As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
r.text[0:100]

#You can load other types of data for non-text requests like images, consider the URL of the following image:
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png'
#We can make a get request:
r=requests.get(url)
#We can look at the response header:
print(r.headers)
#We can we can see the 'Content-Type'
r.headers['Content-Type']
#An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
print(path)
#We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r.content)
#We can view the image:
Image.open(path)

