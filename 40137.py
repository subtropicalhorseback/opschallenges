#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser
import os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')
    
    # Send a request back to the site with the cookie.
    with requests.Session() as session:
        session.cookies.update(cookie)
        response_with_cookie = session.get(targetsite)
        
        # Save the response content to an HTML file
        filename = "response.html"
        with open(filename, 'w') as file:
            file.write(response_with_cookie.text)
        
        # Open the saved HTML file with Firefox
        try:
            # The path to Firefox might need to be adjusted depending on your system
            firefox_path = 'firefox'
            webbrowser.get(firefox_path).open(filename)
        except webbrowser.Error:
            print("Error opening Firefox. Please ensure Firefox is installed and its path is correctly set.")
        
bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)
