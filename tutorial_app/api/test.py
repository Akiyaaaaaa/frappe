import frappe

@frappe.whitelist( allow_guest=True,methods=['GET'] )
def hello():
    frappe.response['message'] = "Hello World"
    return
