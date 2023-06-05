import requests
import os
import shutil
from os.path import splitext, basename
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import logging as log

def downloadImage(imageUrl: str, outputFolder: str = 'images') -> str:
    imageData = requests.get(imageUrl).content
    disassembled = urlparse(imageUrl)
    filename, file_ext = splitext(basename(disassembled.path))
    filename = 'i%s%s' % (str(hash(imageUrl)), file_ext)
    with open('%s/%s' % (outputFolder, filename), 'wb') as handler:
        handler.write(imageData)
    return 

def createDirectory(dirname: str, delete: bool = False) -> None:
    if os.path.exists(dirname):
        if delete:
            shutil.rmtree(dirname)
            log.debug('Recreated new dirctory %s' % dirname)
        else:
            log.debug('Directory %s already exists. Skipping creation.' % dirname)
            return
    
    os.makedirs(dirname)
    log.debug('Created new dirctory %s' % dirname)

def main() -> None:
    createDirectory('images', True)
    image_url = 'https://vulcan.condenastdigital.com/demo/photos/6430305a43557ca5c77bec32/master/pass/WIR_LIFT_Sale_Growler_Paywall_Bar_400x400-update-white-bg_1x%20(1).png?format=original'
    downloadImage(image_url)

if __name__ == "__main__":
    log.basicConfig(level=log.INFO)
    main()
