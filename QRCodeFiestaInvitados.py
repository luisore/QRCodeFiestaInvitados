import qrcode
from PIL import Image, ImageDraw, ImageFont
import qrcode.constants

def create_qr_code(text, output_filename):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)


    img = qr.make_image(fill_color="black", back_color= "white")

    img.save(output_filename)

    