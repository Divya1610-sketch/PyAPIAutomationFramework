def payload_create_booking():
    payload = {
       "firstname": "Divya",
       "lastname": "Bhagwat",
       "totalprice": 111,
       "depositpaid": True,
       "bookingdates": {
           "checkin": "2018-01-01",
           "checkout": "2019-01-01"
       },
       "additionalneeds": "Lunch"
    }
    return payload
