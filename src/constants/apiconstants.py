# Add your constants here

# Adding my url constants

def base_url():
    # Change based on the env.json - Stage, preprod, Prod
    # In future I will write a logic to change the base url based on the env
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id




