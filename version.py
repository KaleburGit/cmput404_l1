import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/KaleburGit/cmput404_l1/main/version.py")

print(resp.text)