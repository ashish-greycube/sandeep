// $(document).ready(async function () {
//     let company = frappe.defaults.get_default("company");
//     frappe.db.get_value("Company", company, "custom_company_banner_color").then((res) => {
//         $(".sticky-top").append(`
//         <div style="text-align: center; font-size: 16px; padding: 8px; background: ${res.message.custom_company_banner_color || "#0f0f0f"}; color: #ffffff;">
//             Current Session Company is ${company}
//         </div>
//     `);
//     })
// });