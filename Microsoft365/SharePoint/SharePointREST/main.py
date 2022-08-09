from src.SharePointREST import *

## Usage (Default Values specified in config.py)

# Get all files from FolderLocation
#print(GetAllFiles())

# Get a single file called FileName located in FolderLocation
#print(GetFile())

# Upload a file called FileName to FolderLocation
#print(UploadFile())


## Usage (Custom Values input into function)

# Get all files from FolderLocation
#print(GetAllFiles('Shared%20Documents/ReportData/NewFolder'))

# Get a single file from FolderLocation called FileName
#print(GetFile('Shared%20Documents/ReportData/NewFolder', 'TestData.csv',))

# Upload into FolderLocation into FileName from UploadFileName
#print(UploadFile('Shared%20Documents/ReportData/NewFolder', 'TestData.csv', 'SampleSmall.csv'))