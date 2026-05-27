$(document).ready(async function () {
    let company = frappe.defaults.get_default("company");

    let color_list = [
        { background: "#5f9ea05e", color: "#487274" },
        { background: "#5fa06d5e", color: "#487452" },
        { background: "#895fa05e", color: "#644874" },
        { background: "#a0745f5e", color: "#745548" }
    ]

    let company_doc = await frappe.get_list("Company")
    let company_list = []
    for (c in company_doc) {
        company_list.push(company_doc[c]["name"])
    }

    let company_index = company_list.indexOf(company)

    if (company_list.length < color_list.length) {
        background = color_list[company_index].background;
        color = color_list[company_index].color;
    } else {
        background = color_list[company_index % color_list.length].background;
        color = color_list[company_index % color_list.length].color;
    }

    $(".sticky-top").append(`
        <div style="text-align: center; font-size: 16px; padding: 8px; background: ${background}; color: ${color};">
            Current Session Company is ${company}
        </div>
    `);
});