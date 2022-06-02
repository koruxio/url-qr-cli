#!/usr/bin/env python3

import qrcode 
from datetime import datetime
import os

url = input("URL : ")

currentTime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

qrCode = qrcode.QRCode(version = 12, box_size = 5, border = 5)

qrCode.add_data(url)

qrCode.make(fit=True)

qrImage = qrCode.make_image(fill='black', back_color='white')

qrImage.save(f"{currentTime}.png")
