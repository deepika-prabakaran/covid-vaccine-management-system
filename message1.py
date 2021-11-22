import requests
contact_no = 7339274549
url = "https://www.fast2sms.com/dev/bulk"
payload = f"sender_id=FSTSMS&message=Congrats! You took your 1st dose of vaccination on 21/11/2021 and your 2nd dose date is 03/01/2022&language=english&route=p&numbers={contact_no}"
headers = {
'authorization': "Mefbs6CNUnpioIKrcLdDSxW8Q0OlEtaRuGzT4B3vYPyXmwFh2ZgDm8XkhvxCOjLV6edIcaP5tRTJnM07",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
