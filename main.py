import qrcode

# Specify the link you want to encode
link = "pasteYourLinkHereToGenerate"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=1,
)

# Add the link data to the QR code
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
