import frappe

def check_for_valid_rate_and_discount(doc, method):
    for row in doc.items:
        if row.price_list_rate < row.rate:
            frappe.throw("Standard Rate can not be less than Discounted Rate.")
