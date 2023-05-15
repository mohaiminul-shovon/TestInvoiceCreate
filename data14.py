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
                "person": {
                    "dateOfBirth": "",
                    "socialSecurityNumber": "19091397067",
                    "hNumber": "",
                    "dNumber": "",
                    "firstName": "Rihana",
                    "lastName": "Mariam",
                    "address1": "322665 Gary, Bargen, Norway",
                    "address2": "",
                    "postalCode": "5085",
                    "city": "BARGEN",
                    "mobileNumber": "98655652",
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
            "participant": {
                "firstName": "Laila",
                "lastName": "Mariam",
                "dateOfBirth": "2002-09-01",
                "socialSecurityNumber": "01090295920",
                "hNumber": "",
                "dNumber": "",
                "mobileNumber": "98655970",
                "email": ""
            },
            "invoiceDate": str(datetime.now().date()),
            "createTime": datetime.now(timezone('CET')).strftime("%H:%M:%S"),
            "dueDate": "2022-12-15",
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
