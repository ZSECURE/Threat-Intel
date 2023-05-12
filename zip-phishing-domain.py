#!/usr/bin/python3
import requests
from termcolor import colored

# List of possible phishing terms
phishing_terms = ["account-deactivation", "account-suspension", "account-verification", "accounts", "annual-report", "apple-update", "apple-updates", "bank-statement", "bonus-details", "booking-confirmation", "business-plan", "census-form", "charity-donation-receipt", "charity-request", "cisco-update", "cisco-updates", "company-update", "company-updates", "contract-agreement", "corporate-policy", "court-summons", "covid-test-result", "credit-approval", "critical-update", "cv", "data-breach", "debt-collection", "discount-coupon", "dll", "email-verification", "employee-survey", "employment-contract", "end-of-year-accounts", "event-invitation", "fedex-notification", "finance", "financial-planning", "flight-itinerary", "fortinet-update", "fortinet-updates", "holiday-gift", "hr", "insurance-claim", "insurance-policy", "invoice", "job-offer", "legal-notice", "lost-package", "lottery-winner", "macos-update", "macos-updates", "medical-report", "meeting-agenda", "meeting-minutes", "membership-confirmation", "microsoft-update", "microsoft-updates", "network-outage", "office-update", "office-updates", "order-confirmation", "password-change", "password-reset", "payment-info", "payment-receipt", "payroll", "performance-review", "prize-redemption", "project-proposal", "project-update", "promotional-offer", "property-deed", "purchase-order", "receipt", "refund-status", "resume", "salary-adjustment", "school-report", "security-breach", "security-protocol", "service-interruption", "shipping-label", "software-update", "software-updates", "software-upgrade", "sonicwall-update", "sonicwall-updates", "subscription-cancellation", "survey-response", "system-alert", "system-notification", "tax-audit", "tax-return", "team-schedule", "ticket-confirmation", "transaction-report", "travel-voucher", "unpaid-invoice", "update", "updates", "urgent-message", "urgent-update", "urgent-updates", "usps-tracking", "vpn-update", "vpn-updates", "warranty-extension", "windows-update", "year-end-accounts"]

# Iterate through each term
for term in phishing_terms:
    url = f"http://{term}.zip"
    try:
        response = requests.get(url)
        # If the status code is 200, print in green, if the code is 403, print yellow, otherwise print in red 
        if response.status_code == 200:
            print(colored(f"{url} - {response.status_code}", "green"))
        elif response.status_code == 403:
            print(colored(f"{url} - {response.status_code}", "yellow"))
        else:
            print(colored(f"{url} - {response.status_code}", "red"))
    except requests.exceptions.RequestException as err:
        print(colored(f"{url} - Connection Error", "red"))
