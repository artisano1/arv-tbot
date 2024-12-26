import requests
    import json
    from typing import Dict, List
    from datetime import datetime

    class HubSpotSync:
        def __init__(self, api_key: str):
            self.api_key = api_key
            self.base_url = "https://api.hubapi.com"
        
        def create_distributor(self, data: Dict):
            """Create a new distributor contact in HubSpot CRM."""
            url = f"{self.base_url}/crm/v3/objects/contacts?hapikey={self.api_key}"
            
            properties = {
                "email": data['email'],
                "firstname": data['first_name'],
                "lastname": data['last_name'],
                "phone": data['phone'],
                "country": data['country'],
                "arvea_id": data['arvea_id'],
                "opportunity_link": data['opportunity_link'],
                "shop_link": data['shop_link'],
                "upline_id": str(data.get('upline_id', '')),
                "level": str(data.get('level', ''))
            }
            
            payload = {
                "properties": properties
            }
            
            response = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload)
            )
            
            if response.status_code in [200, 201]:
                return response.json()['id']
            else:
                raise Exception(f"HubSpot distributor creation failed: {response.text}")
        
        def create_lead(self, data: Dict):
            """Create a new lead contact in HubSpot CRM."""
            url = f"{self.base_url}/crm/v3/objects/contacts?hapikey={self.api_key}"
            
            properties = {
                "email": data['email'],
                "firstname": data['first_name'],
                "lastname": data['last_name'],
                "phone": data['phone'],
                "country": data['country'],
                "lead_status": data.get('status', 'new'),
                "assigned_distributor": str(data.get('distributor_id', ''))
            }
            
            payload = {
                "properties": properties
            }
            
            response = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload)
            )
            
            if response.status_code in [200, 201]:
                return response.json()['id']
            else:
                raise Exception(f"HubSpot lead creation failed: {response.text}")
        
        def get_contact(self, contact_id: str):
            """Retrieve a contact from HubSpot by ID."""
            url = f"{self.base_url}/crm/v3/objects/contacts/{contact_id}?hapikey={self.api_key}"
            
            response = requests.get(
                url,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"HubSpot contact retrieval failed: {response.text}")
        
        def update_contact(self, contact_id: str, properties: Dict):
            """Update a contact in HubSpot by ID."""
            url = f"{self.base_url}/crm/v3/objects/contacts/{contact_id}?hapikey={self.api_key}"
            
            payload = {
                "properties": properties
            }
            
            response = requests.patch(
                url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload)
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"HubSpot contact update failed: {response.text}")
        
        def add_to_hubspot_list(self, list_id: str, emails: List[str]):
            """Add contacts to a HubSpot list."""
            url = f"{self.base_url}/contacts/v1/lists/{list_id}/add?hapikey={self.api_key}"
            
            payload = {
                "emails": emails
            }
            
            response = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload)
            )
            
            return response.status_code in [200, 204]
        
        def start_workflow(self, contact_email: str, workflow_id: str):
            """Start a HubSpot workflow for a contact."""
            url = f"{self.base_url}/automation/v2/workflows/{workflow_id}/enrollments/contacts/{contact_email}?hapikey={self.api_key}"
            response = requests.post(url)
            return response.status_code in [200, 204]
