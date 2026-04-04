import random
import requests
from django.core.cache import cache
from django.conf import settings

def send_sms_otp(phone_number):
    otp = str(random.randint(100000, 999999))
    cache.set(f'otp_{phone_number}', otp, timeout=300)

    response = requests.post(
        'https://www.fast2sms.com/dev/bulkV2',
        headers={
            'authorization': settings.FAST2SMS_API_KEY,
        },
        params={
            'route': 'q',
            'message': f'Your OTP is {otp}. Valid for 5 minutes.',
            'language': 'english',
            'flash': 0,
            'numbers': phone_number,
        }
    )

    print("Fast2SMS status:", response.status_code)
    print("Fast2SMS response:", response.text)

    data = response.json()
    if not data.get('return'):
        raise Exception(data.get('message', 'Failed to send OTP'))

    return otp


def verify_sms_otp(phone_number, otp):
    cached_otp = cache.get(f'otp_{phone_number}')
    if cached_otp and cached_otp == otp:
        cache.delete(f'otp_{phone_number}')
        return True
    return False