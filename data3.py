import json
import random
import uuid
from datetime import datetime
from pytz import timezone

amount = random.randint(100, 1000)
payload = json.dumps({
    "referenceId": "8415e15f-7d95-4601-8bd3-29baedd40388",
    "invoices": [
        {
            "id": str(uuid.uuid4()),
            "organisationNumber": "338731772",
            "invoiceNumber": random.randint(0, 5000),
            "billingInfo": {
                "person": None,
                "company": {
                    "organisationNumber": "938469411",
                    "name": "Test Insurance 22",
                    "address1": "Cost East Fluffy 22",
                    "address2": None,
                    "postalCode": "9750",
                    "city": "Oslo",
                    "telephoneNumber": "011665449887",
                    "email": "andie@insure.no"
                },
                "referenceNumber": "ref test -49887"
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
                    "address1": "Solheimsgaten 5",
                    "address2": None,
                    "postalCode": "5058",
                    "city": "BARGEN",
                    "telephoneNumber": None,
                    "email": None
                },
                "signature": None
            },
            "participant": {
                "firstName": "Jim",
                "lastName": "Carrey",
                "dateOfBirth": "1955-01-31",
                "socialSecurityNumber": "310155196545",
                "hNumber": "",
                "dNumber": "",
                "mobileNumber": "0116654154878",
                "email": ""
            },
            "invoiceDate": str(datetime.now().date()),
            "createTime": datetime.now(timezone('CET')).strftime("%H:%M:%S"),
            "dueDate": "2023-01-12",
            "invoiceItems": [
                {
                    "articleNumber": "          ",
                    "articleTitle": "A72",
                    "quantity": 1,
                    "rate": amount,
                    "totalAmount": amount,
                    "vatPercentage": 0,
                    "totalVatFee": 0,
                    "category": 0
                }
            ],
            "description": None,
            "kidNumber": "000000000619201920193",
            "paymentState": 1,
            "totalAmount": amount,
            "totalVatFee": 0,
            "amountPaid": 0
        }
    ]
})
headers = {
    'token': '2022TKHELSE11TEST',
    'Content-Type': 'application/json'
}
