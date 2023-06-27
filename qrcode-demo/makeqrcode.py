import qrcode

data = 'https://www.youtube.com/'

img = qrcode.make(data)

img.save('myqrcode.png')
