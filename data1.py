import json
import random
import uuid
from datetime import datetime

import pytz
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
                "person": {
                    "dateOfBirth": "1981-05-01",
                    "socialSecurityNumber": "010171162130",
                    "hNumber": "",
                    "dNumber": "",
                    "firstName": "low",
                    "lastName": "Biden",
                    "address1": "25464 North Avenue",
                    "address2": "",
                    "postalCode": "5086",
                    "city": "Oslo",
                    "mobileNumber": "0112121466874",
                    "email": ""
                },
                "company": "",
                "referenceNumber": ""
            },
            "merchantInfo": {
                "herId": "",
                "hprNumber": "654558469",
                "name": "Test11",
                "socialSecurityNumber": "",
                "bankAccountNumber": "938601112945",
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
            "participant": {
                "firstName": "low",
                "lastName": "Biden",
                "dateOfBirth": "1981-05-01",
                "socialSecurityNumber": "010171162130",
                "hNumber": "",
                "dNumber": "",
                "mobileNumber": "0112121466874",
                "email": ""
            },
            "invoiceDate": str(datetime.now().date()),
            "createTime": datetime.now(timezone('CET')).strftime("%H:%M:%S"),
            "dueDate": "2023-01-17",
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
            "kidNumber": "0000000006192019206546",
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
