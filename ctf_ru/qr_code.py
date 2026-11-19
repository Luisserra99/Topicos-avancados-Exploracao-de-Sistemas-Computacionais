import qrcode
payload = '123456789; id'
img = qrcode.make(payload)
img = img.convert('RGB')
img.save('test_inj.jpg')