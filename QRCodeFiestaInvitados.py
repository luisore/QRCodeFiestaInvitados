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



def generate_qr_codes_for_guests(guest_list):
    for index, guest in enumerate(guest_list, start = 1):
        guest_name = guest["name"]
        qr_data = f"Guest Name : {guest_name}\nID: {index}"
        output_filename = f"qr_codes/qr_{index}_{guest_name}.png"

        create_qr_code(qr_data, output_filename)
        print(f"Codigo QR generado para {guest_name}: {output_filename}")  


guest_list = [
    {"name":"Juan Perez"},
    {"name": "Maria Lopez"},
    {"name": "Carlos Gomez"}
]


generate_qr_codes_for_guests(guest_list)