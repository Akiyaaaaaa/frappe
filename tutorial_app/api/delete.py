import frappe


@frappe.whitelist( allow_guest=True, methods=['DELETE'] )
def delete(id):
	try:
		frappe.db.delete("Tutorial API", {"name": id})
		frappe.response['message'] = "OK!"
		return
	except:
		frappe.response['message'] = "Failed to delete data"
		return
