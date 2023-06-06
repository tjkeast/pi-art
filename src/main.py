import requests
import os
import shutil
from os.path import splitext, basename
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import time
import logging as log

def download_image(image_url: str, output_folder: str = 'images') -> str:
    image_data = requests.get(image_url).content
    disassembled = urlparse(image_url)
    file_name, file_ext = splitext(basename(disassembled.path))
    file_name = '%s%s' % (time.time_ns(), file_ext)
    with open('%s/%s' % (output_folder, file_name), 'wb') as handler:
        handler.write(image_data)
    log.debug('Downloaded image %s and saved to file %s' % (image_url, file_name))

def create_directory(directory_name: str, delete: bool = False) -> None:
    if os.path.exists(directory_name):
        if delete:
            shutil.rmtree(directory_name)
            log.debug('Removed directory %s' % directory_name)
        else:
            log.debug('Skipped creating directory %s - already exists' % directory_name)
            return
    
    os.makedirs(directory_name)
    log.debug('Created new dirctory %s' % directory_name)

def main() -> None:
    create_directory('images', True)
    image_url = 'https://vulcan.condenastdigital.com/demo/photos/6430305a43557ca5c77bec32/master/pass/WIR_LIFT_Sale_Growler_Paywall_Bar_400x400-update-white-bg_1x%20(1).png?format=original'
    download_image(image_url)
    download_image(image_url)

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG)
    log.info('App started')
    main()
