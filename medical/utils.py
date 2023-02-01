from datetime import timedelta, datetime
from eskiz_sms import EskizSMS
from config.settings import ESKIZ_EMAIL, ESKIZ_PASSWORD
from .models import Work


def send_verify_code(code, phone_number):
    eskiz = EskizSMS(ESKIZ_EMAIL, ESKIZ_PASSWORD)
    eskiz.send_sms(phone_number, message=f'Tasdiqlash kodi: {code}')


def get_works_jadval(staffs, date=False):
    works = []
    for s in staffs:
        w = Work.objects.filter(staff__user=s.user, date=date) if date else Work.objects.filter(staff__user=s.user)
        if w.exists():
            checked_count = 0
            addresses = []
            for ch in w:
                if ch.checked:
                    checked_count += 1
                    addresses.append(ch.address.addres_name)
            works.append([w, checked_count, addresses])
    return works


def get_now_month():
    months = {
        'January': 'Yanvar', 'February': 'Fevral',
        'March': 'Mart', 'April': 'Aprel',
        'May': 'May', 'June': 'Iyun',
        'July': 'Iyul', 'August': 'Avgust',
        'September': 'Sentabr', 'October': 'Oktabr',
        'November': 'Noyabr', 'December': 'Dekabr',
    }
    month = datetime.now().strftime("%B")
    return months[month]