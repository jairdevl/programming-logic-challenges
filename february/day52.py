# QR code generatos

import qrcode
import qrcode.constants

def generate_qr_code(text, file_name = "qrcode.png"):
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

text = input("Enter the text for the QR code: ")
generate_qr_code(text)
