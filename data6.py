import json
import random
import uuid
from datetime import datetime
from pytz import timezone

payload = json.dumps({
    "referenceId": "8415e15f-7d95-4601-8bd3-29baedd40388",
    "invoices": [
        {
            "id": str(uuid.uuid4()),
            "organisationNumber": "338731772",
            "invoiceNumber": random.randint(0, 5000),
            "billingInfo": {
                "person": {
                    "dateOfBirth": "1995-08-23",
                    "socialSecurityNumber": "23089597555",
                    "hNumber": "",
                    "dNumber": "",
                    "firstName": "Mohaiminul",
                    "lastName": "Shovon",
                    "address1": "291 North Avenue, Bargen, Norway",
                    "address2": "",
                    "postalCode": "5085",
                    "city": "BARGEN",
                    "mobileNumber": "4769565653",
                    "email": ""
                },
                "company": "",
                "referenceNumber": ""
            },
            "merchantInfo": {
                "herId": "",
                "hprNumber": "12204693",
                "name": "Shovon",
                "socialSecurityNumber": "",
                "bankAccountNumber": "938601111794",
                "personalOrganisationNumber": None,
                "company": {
                    "organisationNumber": "338731772",
                    "name": "Test Ent Medisinsk",
                    "address1": "Solheimsgaten 5, 5058 Bergen, Norway",
                    "address2": None,
                    "postalCode": "5058",
                    "city": "BARGEN",
                    "telephoneNumber": None,
                    "email": None
                },
                "signature": None
            },
            "participant": {},
            "invoiceDate": str(datetime.now().date()),
            "createTime": datetime.now(timezone('CET')).strftime("%H:%M:%S"),
            "dueDate": "2022-12-17",
            "invoiceItems": [
                {
                    "articleNumber": "          ",
                    "articleTitle": "A72",
                    "quantity": 1,
                    "rate": 125.50,
                    "totalAmount": 125.50,
                    "vatPercentage": 0,
                    "totalVatFee": 0,
                    "category": 0
                }
            ],
            "description": None,
            "kidNumber": "000000000619201920193",
            "paymentState": 1,
            "totalAmount": 125.50,
            "totalVatFee": 0,
            "amountPaid": 0
        }
    ]
})
headers = {
    'token': '2022TKHELSE11TEST',
    'Content-Type': 'application/json'
}
