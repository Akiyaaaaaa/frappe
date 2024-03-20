import frappe


@frappe.whitelist( allow_guest=True, methods=['PUT'] )
def update(id):
    request = frappe.form_dict
    nama = request.get("nama")
    id = request.get("id")
    try:
        if nama != "":
            frappe.db.set_value("Tutorial API", id, "nama", nama)
            new_data = frappe.get_doc("Tutorial API", id)
            frappe.response['message'] = "OK!"
            frappe.response['data'] = new_data
            return
        else:
            frappe.response['message'] = "Failure"
            frappe.response['data'] = "Name is empty"
            return
    except:
           frappe.response['message'] = "Failed to update data"
           return
