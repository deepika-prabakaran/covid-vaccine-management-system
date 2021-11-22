import requests
contact_no = 963025741
url = "https://www.fast2sms.com/dev/bulk"
payload = f"sender_id=FSTSMS&message=Congrats! You are sucessfully vaccinated with both the doses=english&route=p&numbers={contact_no}"
headers = {
'authorization': "Mefbs6CNUnpioIKrcLdDSxW8Q0OlEtaRuGzT4B3vYPyXmwFh2ZgDm8XkhvxCOjLV6edIcaP5tRTJnM07",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)

