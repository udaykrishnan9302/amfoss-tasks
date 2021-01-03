import json #javascript object notion
import os
import requests
username = input()
loop=1
page=1
identity=[]
while loop!=0:
    req = requests.get('https://api.github.com/users/'+username+'/repos?page='+str(page))
    page+=1
    json = req.json()
    if (len(json)==0):
        loop=0
        continue
    for i in range(0,len(json)):
        identity.append(json[i]['svn_url'])     #subversion using URL to identify repo resources   
  
for i in range(0,len(identity)):
    print(identity[i])
