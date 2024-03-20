import frappe


@frappe.whitelist( allow_guest=True,methods=['GET'] )
def querryParam():
    request = frappe.form_dict
    data = request.get("data")
    frappe.response['message'] = data
    return


@frappe.whitelist( allow_guest=True,methods=['GET'] )
def toDoctype():
	request = frappe.form_dict
	namaDoctype = request.get("nama_doctype")
	data = frappe.get_all(namaDoctype)
	frappe.response['message'] = "OK!"
	frappe.response['data'] = data
	return

@frappe.whitelist( allow_guest=True,methods=['GET'] )
def getData():
    data = frappe.get_all("Tutorial API")
    frappe.response['data'] = data
    frappe.response['message'] = "OK!"
    return
