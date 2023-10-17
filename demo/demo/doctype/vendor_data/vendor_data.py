# Copyright (c) 2023, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import json

class VendorData(Document):
	pass

@frappe.whitelist()
def get_vendor_data():
	url="http://localhost:8030/api/method/vendormanagement.vendor_management.doctype.vendor_details.vendor_details.get_vendor_list"
	response = requests.request("GET", url,headers = {
			'Content-Type': 'application/json',
				})
	response_data=response.json()
	print("respons",response_data)
	
	
	for d in response_data["message"]:
		
		name = d["name"]
		if name:
			existing_doc = frappe.db.exists("Vendor Data",{"name1":name})
			if existing_doc:
				print("no")
			else:
				new_doc=frappe.new_doc("Vendor Data")
				new_doc.name1=name
				new_doc.address1=d['address1']
				new_doc.address_2=d['address_2']
				new_doc.attachements=d['attachements']
				new_doc.bank_branch=d['bank_branch']
				new_doc.bank_name=d['bank_name']
				new_doc.city=d['city']
				new_doc.contact_person_1=d['contact_person_1']
				new_doc.contact_person_2=d['contact_person_2']
				new_doc.din=d['din']
				new_doc.gst_provisional_id=d['gst_provisional_id']
				new_doc.ifsc_code=d['ifsc_code']
				new_doc.mobile_number=d['mobile_number']
				new_doc.msme_category=d['msme_category']
				new_doc.pan_number=d['pan_number']
				new_doc.pin_code=d['pin_code']
				new_doc.state=d['state']
				new_doc.status=d['status']
				new_doc.street=d['street']
				new_doc.telephone_number=d['telephone_number']
				new_doc.vendor_name=d['vendor_name']
				new_doc.banking_account_number=d['banking_account_number']
				new_doc.insert(ignore_permissions=True)

			
               

	
	return response_data

		
