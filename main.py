import requests
import zipfile
from io import BytesIO

source_url = "https://github.com/tukui-org/ElvUI/archive/refs/heads/main.zip"

req = requests.get(source_url)
filename = f"{source_url.split('/')[4]}-{source_url.split('/')[-1]}"
with open(filename,'wb') as output_file:
    output_file.write(req.content)
    
zipfile= zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall()

