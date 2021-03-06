from django.shortcuts import render
import qrcode
from datetime import datetime
import time
from django.http import HttpResponse
# Create your views here.
def generateQRCode(requests):
    curr_date = datetime.today().strftime('%d-%m-%Y')
    curr_time = datetime.now().time().strftime('%H:%M:%S')
    subj_code = '10'  # TODO: Database Value
    staff_id = '12'  # TODO: Database Value

    data = (curr_date, curr_time, subj_code, staff_id)
    qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,border=1)
    # HACK: If needed save image first in svg and return it
    qr_code.add_data(data)
    qr_code.make(fit=True)
    qr_img = qr_code.make_image(fill_color='black', back_color='white')
    # TODO: Destroy image after 30 seconds in frontend
    qr_img.save("static/qrcode_images/test.png")
    # time.sleep(10)  # Shows 30 seconds delay
    if requests.user.is_authenticated:
        return render(requests,'qrcode.html')
    return HttpResponse("<h1>Sorry!! You can't generate the QR-CODE like this. Please click the | Generate QR-Code | Button.</h1>")