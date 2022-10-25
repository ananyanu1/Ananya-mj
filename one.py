# importing library
import qrcode
# Data to qrcode
data = "https://google.co.in"
# creating an instance of QRcode class
qr = qrcode.QRCode(version = 1,box_size = 10,border = 5)
# Adding data to the instance 'qr'
qr.add_data(data)
qr.make(fit = True)
# img = qr.make_image(fill_color = 'Green', back_color = 'white')
img.save('rep.png')
