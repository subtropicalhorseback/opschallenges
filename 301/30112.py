import sys
import requests

######################
## define functions ##
######################
def getAddr():
    destUrl=str(input("Enter a website to check connection, in format https://www.example.com: "))
    print("Okay, got it -",destUrl,"confirmed.")
    return destUrl

############################################
def request1():
    print("Option 1: GET \nOption 2: POST \nOption 3: PUT \nOption 4: DELETE \nOption 5: HEAD \nOption 6: PATCH \nOption 7: OPTIONS \nOption 8: quit")
    while True:
        choice = int(input("Enter your choice (number only, 1-8): "))
        match choice:
            case 1:
                print("You selected option 1: GET")
                httpReq = "GET"
                return httpReq
            case 2:
                print("You selected option 2: POST")
                httpReq = "POST"
                return httpReq
            case 3:
                print("You selected option 3: PUT")
                httpReq = "PUT"
                return httpReq
            case 4:
                print("You selected option 4: DELETE")
                httpReq = "DELETE"
                return httpReq
            case 5:
                print("You selected option 5: HEAD")
                httpReq = "HEAD"
                return httpReq
            case 6:
                print("You selected option 6: PATCH")
                httpReq = "PATCH"
                return httpReq
            case 7:
                print("You selected option 7: OPTIONS")
                httpReq = "OPTIONS"
                return httpReq
            case 8:
                print("Quitting the program.")
                sys.exit()
            case _:
                print("Invalid choice")
############################################
### automation: https://chat.openai.com/share/37a8209e-8880-498d-8d18-ee8851ba0ecf
def codeChk(response_code):
    if response_code == 200:
        print("Response code:", response_code, "OK - The request was successful.")
    elif response_code == 201:
        print("Response code:", response_code, "Created - The request was successful, and a new resource was created.")
    elif response_code == 204:
        print("Response code:", response_code, "No Content - The request was successful, but there is no additional information to send back.")
    elif response_code == 400:
        print("Response code:", response_code, "Bad Request - The request could not be understood or was missing required parameters.")
    elif response_code == 401:
        print("Response code:", response_code, "Unauthorized - Authentication failed or user does not have permissions.")
    elif response_code == 403:
        print("Response code:", response_code, "Forbidden - The server refuses to authorize the request.")
    elif response_code == 404:
        print("Response code:", response_code, "Not Found - The requested resource could not be found.")
    elif response_code == 405:
        print("Response code:", response_code, "Method Not Allowed - The specified method is not allowed for the resource.")
    elif response_code == 500:
        print("Response code:", response_code, "Internal Server Error - An unexpected condition was encountered on the server.")
    elif response_code == 502:
        print("Response code:", response_code, "Bad Gateway - The server received an invalid response from the upstream server.")
    elif response_code == 503:
        print("Response code:", response_code, "Service Unavailable - The server is not ready to handle the request.")
    elif response_code == 504:
        print("Response code:", response_code, "Gateway Timeout - The server did not receive a timely response from the upstream server.")
    elif response_code == 301:
        print("Response code:", response_code, "Moved Permanently - The requested resource has been permanently moved.")
    elif response_code == 302 or response_code == 303:
        print("Response code:", response_code, "Found/See Other - The requested resource resides temporarily under a different URL.")
    elif response_code == 304:
        print("Response code:", response_code, "Not Modified - The resource has not been modified since the specified version.")
    else:
        print("Your response code is", response_code, "which is not defined in this Python script.")
############################################
def getConf():

    print("You are going to send",destUrl,"an http",httpReq,"type request.")
    while True:
        choice = int(input("Do you want to continue? 1 for yes // 2 for no or quit: ").lower())
        match choice:
            case 1:
                print("Continuing...")
                conf = 1
                return conf
            case 2:
                print("Stopping...")
                sys.exit()
            case _:
                print("Invalid choice")
############################################
############################################

# Prompt the user to type a string input as the variable for your destination URL.
destUrl = getAddr()

# Prompt the user to select a HTTP Method of the following options:
# GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS
httpReq = request1()

# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.
conf = getConf()
if conf == 1:
    print("sending request: http-" + httpReq, "to", destUrl,"as requested.")
    response = requests.request(httpReq, destUrl)
    output1 = response.status_code
    output2 = response.headers

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error 
# should print Site not found to the terminal instead of 404.

codeChk(output1)

# For the given URL, print response header information to the screen.
print(output2)
