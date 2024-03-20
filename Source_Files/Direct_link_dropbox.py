# install pyperclip module using pip install pyperclip
# V1.1 2020-05-20
# Ahmed Al fahdi

# This program will replace the www.dropbox.com with dl.dropboxusercontent.com

#How to use the program:
# 1- install pyperclip module using pip install pyperclip
# 2- copy the link from dropbox and run the program
# 3- the program will copy the new link to the clipboard
# 4- paste the new link in the browser and hit enter


print("Dropbox direct link generator")
print("By Ahmed Al fahdi, V1.1 2020-05-20")
print("Install pyperclip module using (pip install pyperclip) if it fails to start")
input("Press enter to continue...")
import pyperclip

def replace_dropbox_url(url):
    # Replace www.dropbox.com with dl.dropboxusercontent.com
    new_url = url.replace("www.dropbox.com", "dl.dropboxusercontent.com")
    
    # Remove ?dl=0 from the end of the URL
    if new_url.endswith("?dl=0"):
        new_url = new_url[:-5]  # Remove the last 5 characters (?dl=0)
    
    return new_url

# Loop until the user enters "exit"
while True:
    # User input and output
    original_url = input("Enter the URL (or 'exit' to quit): ")
    
    if original_url == "exit":
        break  # Exit the loop
    
    modified_url = replace_dropbox_url(original_url)
    pyperclip.copy(modified_url)  # Copy the modified URL to clipboard
    print("<#####################Modified URL############################>")
    print(modified_url)
    print("The modified URL has been copied to clipboard.")