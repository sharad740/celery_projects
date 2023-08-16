import string
from django.utils.crypto import get_random_string
from django.utils import timezone

def otp_generator():
    return get_random_string(6,string.digits)

def timesince(timestamp):
    now = timezone.now()
    diff = now - timestamp
    if diff.days > 365:
        return f'{diff.days // 365} years ago'
    if diff.days > 30:
        return f'{diff.days // 30} months ago'
    if diff.days > 7:
        return f'{diff.days // 7} weeks ago'
    if diff.days > 0:
        return f'{diff.days} days ago'
    if diff.seconds > 3600:
        return f'{diff.seconds // 3600} hours ago'
    if diff.seconds > 60:
        return f'{diff.seconds // 60} minutes ago'
    return f'{diff.seconds} seconds ago'
