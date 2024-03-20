import qrcode

def generate_qrcode(text):
    # Create a QR Code instance with specific configurations
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
    
    # Add data to the QR Code
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("sabuhi.png")

generate_qrcode("https://www.instagram.com/isazada/?hl=fr")
