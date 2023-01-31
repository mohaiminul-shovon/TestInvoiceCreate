import json

import requests
import data3
import data1
import data2
import data4
import data5
import data6
import data7
import data8
import data9
import data10
import data11
import data12

url1 = "https://test1.tkhelse.com/dev-test/api/infodoc/create-invoices/"
url2 = "https://test2.tkhelse.com/dev-test/api/infodoc/create-invoices/"

try:
    while True:
        choice = input("1. same biller and patient info with only mobile number \n"
                    "2. different biller and patient info with only mobile number\n"
                    "3. company biller and know patient info with email\n"
                    "4. company biller and unknow patient info with email\n"
                    "5. same biller and patient info with only email\n"
                    "6. One biller and no patient info with only mobile number\n"
                    "7. Different biller and patient with phone number and email\n"
                    "8. Same biller and patient info with no phone number and email\n"
                    "9. Same biller and patient info with phone and email both\n"
                    "10. Different biller and patient with only email\n"
                    "11. Different biller and patient with no phone and email\n"
                    "choose your case: \n")
        # same biller and patient info(sms)
        if choice == "1":
            header = data1.headers
            body = data1.payload
        # one biller and another patient(sms)
        elif choice == "2":
            header = data2.headers
            body = data2.payload
        # One biller and no patient info(sms)
        elif choice == "6":
            header = data6.headers
            body = data6.payload
        # same biller and patient info (email)
        elif choice == "5":
            header =data5.headers
            body = data5.payload
        # Company biller and another patient
        elif choice == "3":
            header = data3.headers
            body = data3.payload

        # For creating new doctor
        elif choice == "7":
            header = data7.headers
            body = data7.payload
        # Same biller and patient info with no phone number and email
        elif choice == "8":
            header = data8.headers
            body = data8.payload
        # Same biller and patient info with phone and email both
        elif choice == "9":
            header = data9.headers
            body = data9.payload
        # Different biller and patient with only email
        elif choice == "10":
            header = data10.headers
            body = data10.payload
        # Different biller and patient with no phone and email
        elif choice == "11":
            header = data11.headers
            body = data11.payload
        # Company biller with no phone and email and no patient info
        elif choice == "12":
            header = data12.headers
            body = data12.payload
        # Company biller with only email
        else:
            header = data4.headers
            body = data4.payload
        response = requests.request("POST", url1, headers=header, data=body)
        print(response.text)
        pass
except KeyboardInterrupt:
    print("Exiting from the program. Thank you!")

