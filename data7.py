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
                    "dateOfBirth": "1971-01-01",
                    "socialSecurityNumber": "01017118654",
                    "hNumber": "",
                    "dNumber": "",
                    "firstName": "kate",
                    "lastName": "Middleton",
                    "address1": "902 North Avenue",
                    "address2": "",
                    "postalCode": "5086",
                    "city": "Yern",
                    "mobileNumber": "011556698412",
                    "email": "katei@yahoo.com"
                },
                "company": "",
                "referenceNumber": ""
            },
            "merchantInfo": {
                "herId": "",
                "hprNumber": "12204691",
                "name": "Shaun Micheal",
                "socialSecurityNumber": "",
                "bankAccountNumber": "93860115555",
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
                "firstName": "Ariq ",
                "lastName": "Islam",
                "dateOfBirth": "1971-01-01",
                "socialSecurityNumber": "01017119366",
                "hNumber": "",
                "dNumber": "",
                "mobileNumber": "6546546458656",
                "email": "ariq@gmail.com"
            },
            "invoiceDate": str(datetime.now().date()),
            "createTime": datetime.now(timezone('CET')).strftime("%H:%M:%S"),
            "dueDate": "2022-12-29",
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
