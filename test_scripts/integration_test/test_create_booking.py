'''


Author: Divya
Objective: Create and Verify the POST request
TC#1: Verify the status code
TC#2: Verify the Body - Booking ID
TC#3: Verify the JSON schema is valid



'''
import pytest

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verfication import *


class TestIntegration(object):

    @pytest.fixture(scope="module")
    def setup(self):
        print("Before")


    def test_create_booking_tc1(self):

        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        verify_key_for_not_null_greater_than_zero(response.json()["bookingid"])

    @pytest.fixture(scope="module")
    def tear_down(self):
        print("End")







   # def test_create_booking_tc2(self):
   #     assert True == False

   # def test_create_booking_tc3(self):
   #    assert True == True
