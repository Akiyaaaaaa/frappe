import frappe


@frappe.whitelist( allow_guest=True, methods=['POST'] )
def create(nama):
    new_data = frappe.new_doc("Tutorial API")
    new_data.nama = nama
    try:
            new_data.insert()
            frappe.response['message'] = "OK!"
            frappe.response['data'] = new_data
            return
    except:
           frappe.response['message'] = "Failed to insert data"
           return
