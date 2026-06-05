import frappe

def check_for_valid_rate_and_discount(doc, method):
    for row in doc.items:
        if row.price_list_rate < row.rate:
            frappe.throw("Standard Rate can not be less than Discounted Rate.")

def fetch_customer_po_and_set_in_user_remarks(doc, method):
    unique_so_list = []
    if len(doc.items) > 0:
        for row in doc.items:
            if row.sales_order and row.sales_order not in unique_so_list:
                unique_so_list.append(row.sales_order)
    
    po_no_list = []
    if len(unique_so_list)>0:
        for so in unique_so_list:
            customer_po_number = frappe.db.get_value("Sales Order", so, "po_no")
            if customer_po_number and customer_po_number not in po_no_list:
                po_no_list.append(customer_po_number)
    print(po_no_list,"===========================")
    if len(po_no_list)>0:
        po_no_str = ", ".join(po_no_list)
    else :
        po_no_str = ""

    doc.custom_user_remarks = po_no_str
