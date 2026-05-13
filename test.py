import xml.etree.ElementTree as ET
import re

# Path to your XML file
file_path = "modified_sms_v2.xml"

# Parse XML
tree = ET.parse(file_path)
root = tree.getroot()

total_received = 0
total_sent = 0

received_count = 0
sent_count = 0

# Loop through all SMS messages
for sms in root.findall("sms"):
    body = sms.get("body")

    # RECEIVED MONEY
    if "received" in body.lower():
        match = re.search(r"received\s([\d,]+)\sRWF", body)

        if match:
            amount = int(match.group(1).replace(",", ""))
            total_received += amount
            received_count += 1

    # MONEY SENT / PAYMENT
    elif "payment of" in body.lower() or "transferred to" in body.lower():

        # payment of 1,000 RWF
        payment_match = re.search(r"payment of\s([\d,]+)\sRWF", body)

        # 1500 RWF transferred to
        transfer_match = re.search(r"([\d,]+)\sRWF transferred to", body)

        if payment_match:
            amount = int(payment_match.group(1).replace(",", ""))
            total_sent += amount
            sent_count += 1

        elif transfer_match:
            amount = int(transfer_match.group(1).replace(",", ""))
            total_sent += amount
            sent_count += 1

# Results
print("===== TRANSACTION SUMMARY =====")
print(f"Total Received: {total_received} RWF")
print(f"Number of Received Transactions: {received_count}")

print()

print(f"Total Sent/Expenses: {total_sent} RWF")
print(f"Number of Sent Transactions: {sent_count}")