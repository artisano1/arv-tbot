from hubspot import HubSpot
from config import Config

def create_contact(firstname, lastname, email, phone):
    client = HubSpot(access_token=Config.HUBSPOT_ACCESS_TOKEN)
    properties = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "phone": phone
    }
    client.crm.contacts.basic_api.create(properties=properties)