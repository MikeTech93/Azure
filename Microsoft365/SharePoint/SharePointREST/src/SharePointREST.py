from config import *
import requests
import re
import ast
import json

def GetTenantID():
    
    url = "https://" + configuration["SharePointDomain"] + "/_vti_bin/client.svc/"

    payload={}
    headers = {
    'Authorization': 'Bearer'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    regex = r"[:,\{\}\[\]]|(\".*?\")|('.*?')|[-\w.]+g"
    matches = ["".join(x) for x in re.findall(regex, response.headers["WWW-Authenticate"], re.MULTILINE)]

    return matches[0].replace('"','').replace(')',''), matches[2].replace('"','').replace(')','')

def GetToken():
    url = "https://accounts.accesscontrol.windows.net/" + GetTenantID()[0] + "/tokens/OAuth/2"

    payload= 'grant_type=client_credentials&client_id=' + credentials["ClientID"] + '%40' + GetTenantID()[0] + '&client_secret=' + credentials["ClientSecret"] + '%3D&resource= ' + GetTenantID()[1] + '%2F' + configuration["SharePointDomain"] + '%40' + GetTenantID()[0]
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'esctx=AQABAAAAAAD--DLA3VO7QrddgJg7WevrsmQSgVc05SuzZdzmlZVIqp9NyrDU-yuaW3DglzheMlyP89ywBM2iYT6s5qcdmPXrL_BhSWSwWkp5vLQknwUSKgzLg1zEI5ayqSU4x_a_vbgNnQzgvA1_Y52t9E9gZP1OsnXo074TYsDp0DhyIxm-px3RH91LX2g0mveyP8lIBOogAA; fpc=Akr0uTJS3LRFuAxKVvy9glnxz3U-AQAAAJbKXNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
    }

    response = ast.literal_eval(requests.request("POST", url, headers=headers, data=payload).text)
    return response['access_token']

def GetAllFiles(folder = configuration['FolderLocation']):
    token = GetToken()

    url = "https://" + configuration['SiteURL'] + "_api/web/GetFolderByServerRelativeUrl('" + folder + "')/Files"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + token + '',
    'Accept': 'application/json;odata=verbose'
    }

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
    return(response['d']['results'])

def GetFile(folder = configuration['FolderLocation'], file = configuration['FileName']):
    token = GetToken()

    url = "https://" + configuration['SiteURL'] + "_api/web/GetFolderByServerRelativeUrl('" + folder + "')/Files('" + file + "')"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + token + '',
    'Accept': 'application/json;odata=verbose'
    }

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

    return(response['d']['__metadata'])

def UploadFile(folder = configuration['FolderLocation'], file = configuration['FileName'], uploadFile = configuration['UploadFileName']):
    token = GetToken()

    url = "https://" + configuration['SiteURL'] + "_api/web/GetFolderByServerRelativeUrl('" + folder + "')/Files/add(url='" + file + "',overwrite=true)"

    # UPLOAD FROM INLINE CSV
    # payload="hello,world,this,is,a,test,demonstrating,uploading,inline,csv"

    # UPLOAD FROM CSV IN MEMORY
    # csv = "hello,world,this,is,a,test,demonstrating,uploading,csv,from,memory"
    # payload = csv

    # UPLOAD FROM CSV FILE
    payload = open(uploadFile)

    headers = {
    'Authorization': 'Bearer ' + token + '',
    'Accept': 'application/json;odata=verbose',
    'Content-Type': 'text/csv'
    }

    response = json.loads(requests.request("POST", url, headers=headers, data=payload).text)

    return(response['d']['__metadata'])