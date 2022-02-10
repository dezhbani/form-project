
from ippanel import Client
from decouple import config


api_key = config('api-key')
sms = Client(api_key)

def send_message(phone,code):
    bulk_id = sms.send_pattern(
        "6x5e01fhw2",
        "+983000505",          # originator
        phone,    # recipients
        code # message
    )

    return bulk_id

