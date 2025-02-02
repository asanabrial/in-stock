import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.email import Email
from src.constants import NVIDIA_API_STORE, NVIDIA_HEADERS, EMAIL_TO, EMAIL_FROM, EMAIL_SUBJECT, EMAIL_BODY, EMAIL_PASSWORD


class NvidiaStoreChecker:
    def run():
        # Make the HTTP request
        response = requests.get(NVIDIA_API_STORE, headers=NVIDIA_HEADERS)
        data = response.json()

        # Check if any product_url is not empty
        product_urls = [item.get("product_url", "")
                        for item in data.get("listMap", [])]
        has_available_product = any(product_urls)

        # If any URL is available, send an email
        if has_available_product:
            body = EMAIL_BODY
            # Create the email message
            for item in data.get("listMap", []):
                if item.get("product_url"):
                    body += f"SKU: {item.get('fe_sku')
                                    }, URL: {item.get('product_url')}\n"
            email = Email(email=EMAIL_FROM, password=EMAIL_PASSWORD)
            email.send(EMAIL_SUBJECT, body, EMAIL_TO)

        else:
            print("No products available with non-empty URLs.")
