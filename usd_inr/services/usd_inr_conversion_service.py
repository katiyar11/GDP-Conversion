
from gdp_conversion.settings import BASE_DIR
from usd_inr.models import GdpData
import matplotlib.pyplot as plt
import requests


class GdpConversionService:
    @classmethod
    def create_usd_data(cls):
        all_usd_data = GdpData.objects.all()
        xx = []
        yy = []
        static_path =  '/static/images/usd_plot.png'
        save_image_path = BASE_DIR + static_path
        
        for val in all_usd_data:
            xx.append(val.date)
            yy.append(val.usd_data)


        plt.scatter(xx, yy)
        plt.title("USD Data")
        plt.xlabel("Year")
        plt.ylabel("GDP in Billion USD")
        plt.xticks(rotation=20, ha='right')
        plt.savefig(save_image_path)
        return static_path
    

    @classmethod
    def usd_to_inr_conversion(cls):
        all_usd_data = GdpData.objects.all()
        xml = []
        yml = []
        
        to_data = "INR"
        from_data = "USD"
        static_path = f"/static/images/inr_plot.png"
        save_image_path = BASE_DIR + static_path
        try:
            for val in all_usd_data:
                xml.append(val.date)

                amount = val.usd_data

                url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_data}&from={from_data}&amount={amount}"

                payload = {} 
                headers = {
                    "apikey": "2Zzp9FKDVv4qeuRupbtfOcChJDCi06YG"
                }

                response = requests.request("GET", url, headers=headers, data=payload)

                status_code = response.status_code
                result = response.json()
                yml.append(result["result"])

            plt.scatter(xml, yml)   
            plt.title("INR Data")
            plt.xlabel("Year")
            plt.ylabel("GDP in Billion INR")
            plt.xticks(rotation=20, ha='right')
            plt.savefig(save_image_path)

        except:
            message = "Response is not found"
            return message
        return static_path

