import os
import smplib
import requests
from linode_api4 from import LinodeClient

EMAIL_ADDRESS = os.envron.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMIAL_TOKEN = os.environ.get('LINODE_TOKEN')

client = LinodeClient(LINODE_TOKEN)

for linode in client.linode.instances():
    print(f'{linode.label}: {linode.id}')


r = requests.get('https://www.srilankan.com/en_uk/lk',timeout = 10) 

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com' , 587 ) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Site is down'
        body = 'Check whether server restarted and it is backup'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS,'https://www.srilankan.com/en_uk/lk', msg)