

"""Use this to run script.

./manage.py shell < usd_inr/scripts/try.py
"""
from gdp_conversion.settings import BASE_DIR
from usd_inr.models import GdpData
from usd_inr.services.usd_inr_conversion_service import GdpConversionService
import matplotlib.pyplot as plt


all_data = GdpData.objects.all()
static_path = f"/static/images/latesssst_test_plot.png"
save_image_path = BASE_DIR + static_path
xx = []
yy = []
for i in all_data:
    xx.append(i.date)
    yy.append(i.usd_data)

plt.scatter(xx, yy)   
plt.title("USD data")
plt.xlabel("Year")
plt.ylabel("GDP in Billion USD")
plt.xticks(rotation=20, ha='right')
plt.savefig(save_image_path)
