from django.http import JsonResponse
from django.shortcuts import render
import matplotlib.pyplot as plt

from usd_inr.services.usd_inr_conversion_service import GdpConversionService
from usd_inr.models import GdpData
import os
import io
import base64


def usd_data_request(request):    
    """
    API for Display the USD data in scatter plot

    """
    save_image_path = GdpConversionService.create_usd_data()
    return render(
        request,
        "index.html",
        {"image_path": save_image_path}
    )


def usd_conversion_request(request):
    """
    API for Display the converted data from USD into INR in scatter plot

    """
    
    image_path = GdpConversionService.usd_to_inr_conversion()
    response = {"success": True, "image_path": image_path}

    json_response = JsonResponse(response)
    return json_response





