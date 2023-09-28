import qrcode
text = "Roger Droidman"
qr = qrcode.make(text)
qr.save('roger.jpg')
