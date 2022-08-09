# SharePoint REST API Custom Package
- Small python package to provide easy REST uploads to a SharePoint site.
- Authentication via Service Principal Client ID & Secret

## How to develop
- xxx

## How to use in your own app
- Add SharePointREST.py into your file structure (preferably into a src folder but python is not fussy)
- Add config.py and populate relevant details (See below sections for further explanation)
- Copy requirements into your existing requirements file
- Import SharePointREST.py e.g.

    ```python
    from src.SharePointREST import *
    ```

## Required configuration in config.py
- This is the minimum configuration required to allow the REST API to communicate with the SharePoint Site
- Example:

    ```python
    credentials = {
        'ClientSecret' : 'xxx', # Azure Service Principal Client Secret
        'ClientID' : 'xxx' # Azure Service Principal ClientID
    }

    configuration = {
        'SharePointDomain' : 'thevirtualforge0.sharepoint.com', # Office 365 Tenant Domain
        'SiteURL' : 'thevirtualforge0.sharepoint.com/sites/JLRSprintReport77/' # SharePoint Site Root URL
    }
    ```

## Optional Values
- If you are writing to the same folder and file every time then enter these into config.py 
- The functions will automatically use these values and you don't need to pass anything into the functions
- If you need to change folder and file every time you run the function see "Usage (Default Values specified in config.py)" section below
- Example:

    ```python
    configuration = {
        'FolderLocation' : 'Shared%20Documents/ReportData', # Default Foldername to Get\Upload File
        'FileName' : 'TestData.csv', # Default Filename that will appear on SharePoint site
        'UploadFileName': 'SampleSmall.csv' # Default Filename to get for upload
    }
    ```

## Usage (Default Values specified in config.py)
- Examples:

    ```python
    # Get all files from FolderLocation
    GetAllFiles()

    # Get a single file called FileName located in FolderLocation
    GetFile()

    # Upload a file called FileName to FolderLocation
    UploadFile()
    ```

## Usage (Custom Values input into function)
- Examples:

    ```python
    # Get all files from FolderLocation
    GetAllFiles('Shared%20Documents/ReportData/NewFolder')

    # Get a single file from FolderLocation called FileName
    GetFile('Shared%20Documents/ReportData/NewFolder', 'TestData.csv',)

    # Upload into FolderLocation into FileName from UploadFileName
    UploadFile('Shared%20Documents/ReportData/NewFolder', 'TestData.csv', 'SampleSmall.csv')
    ```

## SimpleUploadFile Payload Methods
- There are three demonstrated ways to specify a payload to upload to SharePoint
- These are ready to go in SharePointREST.py in the UploadFile function but commented out so you can easily select your preffered method

    ```python
    # UPLOAD FROM INLINE CSV
    payload="hello,world,this,is,a,test,demonstrating,uploading,inline,csv"

    # UPLOAD FROM CSV IN MEMORY
    csv = "hello,world,this,is,a,test,demonstrating,uploading,csv,from,memory"
    payload = csv

    # UPLOAD FROM CSV FILE
    payload = open(uploadFile) # Defaults to UploadFileName from config.py
    ```