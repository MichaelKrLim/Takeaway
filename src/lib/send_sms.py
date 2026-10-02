from vonage import Auth, Vonage
from vonage_messages import Sms
from lib.secret import *

# i don't really want to add a dictionary of truth codes, so i'll just leave 44
def to_international(number: str, default_country_code: str = "44") -> str:
    digits = "".join(ch for ch in number if ch.isdigit())
    if digits.startswith("00"):
        digits = digits[2:]
    elif digits.startswith("0"):
        digits = default_country_code + digits[1:]
    return digits

def send_to(number: str, message: str):
    client = Vonage(
        Auth(
            api_key=vonage_api_key,
            api_secret=vonage_secret,
        )
    )

    return client.messages.send(
        Sms(
            to=to_international(number),
            from_="Takeaway",
            text=message
        )
    )
