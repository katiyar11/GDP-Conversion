"""Use this to run script.

./manage.py shell < usd_inr/scripts/populate.py
"""

import pandas as pd
from datetime import datetime
from usd_inr.models import GdpData

df = pd.read_excel('usd_inr/scripts/BankWise.xlsx')
for index, rows in df.iterrows():
    
    date = rows.get("Date")
    date = datetime.strptime(date, '%d/%m/%Y').strftime("%Y-%d-%m")
    date = datetime.strptime(date, "%Y-%d-%m")    
    usd = rows.get("USD")
    
    gdp_data, created = GdpData.objects.update_or_create(
    date=date,
    defaults={
        'date': date,
        'usd_data': usd,
    }
)

print("Created")
