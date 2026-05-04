#create qr code
import qrcode
qr=qrcode.QRCode()
text="TVK Is HEADING towards CHENNAI HEADQUERTERS"
qr.add_data(text)
qr.make(fit=True)
res=qr,make_image(fil_color="black",back_color="white")
res.save("NIHARIKA.png")
print("created niha")
