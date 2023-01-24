from datetime import timedelta, datetime


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