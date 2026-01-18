import sys
import os

#this script should:
#Replace the name in template
#Add description where required
#sets version to 0.0.0

#Do delete  this after use! So it's not accidentally used and does not exist in your result repo!
#Don't use after new repo was already under development.

name = "YOUR_REPO_NAME_HERE"

description = "This repo does xxx..."

#NOTE LICENCE NEEDS TO BE CHANGED MANUALLY (otherwise it belongs to LuTze under MIT licence forever! xD)

import os



to_rename = ["README.md","pyproject.toml","docs/source/conf.py","docs/source/index.rst","docs/source/Using_repTemp.rst"]
for FILE in to_rename:
    
    with open("example.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    text = text.replace("repTemp",name)  # edit however you want
    
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
for_description = ["README.md","pyproject.toml","docs/source/Introduction.rst"]

for FILE in for_description:
    
    with open("example.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    text = text.replace("YOUR_REPO_DESCRIPTION_HERE",description)  # edit however you want
    
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
for_versions = [".bumpversion.cfg","pyproject.toml","README.md","docs/source/conf.py"]

for FILE in for_versions:
    
    with open("example.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    text = text.replace("1.0.0","0.0.0")  # edit however you want
    
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write(text)   

#Rename the folder in src, will need to also change parent dir manually
os.rename("src/repTemp", "src/"+name) 
    
os.rename("docs/source/Using_repTemp.rst", "docs/source/Using_"+name +".rst") 
    
    
    
    
    
    

