app_name = "sandeep"
app_title = "Sandeep Customization"
app_publisher = "Greycube Technologies"
app_description = "Customization For Sandeep "
app_email = "admin@greycube.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sandeep",
# 		"logo": "/assets/sandeep/logo.png",
# 		"title": "Sandeep Customization",
# 		"route": "/sandeep",
# 		"has_permission": "sandeep.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sandeep/css/sandeep.css"
app_include_js = "/assets/sandeep/js/banner.js"

# include js, css files in header of web template
# web_include_css = "/assets/sandeep/css/sandeep.css"
# web_include_js = "/assets/sandeep/js/sandeep.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sandeep/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/sales_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sandeep/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sandeep.utils.jinja_methods",
# 	"filters": "sandeep.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sandeep.install.before_install"
# after_install = "sandeep.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sandeep.uninstall.before_uninstall"
# after_uninstall = "sandeep.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sandeep.utils.before_app_install"
# after_app_install = "sandeep.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sandeep.utils.before_app_uninstall"
# after_app_uninstall = "sandeep.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sandeep.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"validate": "sandeep.api.check_for_valid_rate_and_discount"
	},
    "Sales Invoice": {
		"validate": ["sandeep.api.check_for_valid_rate_and_discount",
               		 "sandeep.api.fetch_customer_po_and_set_in_user_remarks"],
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sandeep.tasks.all"
# 	],
# 	"daily": [
# 		"sandeep.tasks.daily"
# 	],
# 	"hourly": [
# 		"sandeep.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sandeep.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sandeep.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sandeep.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sandeep.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sandeep.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sandeep.utils.before_request"]
# after_request = ["sandeep.utils.after_request"]

# Job Events
# ----------
# before_job = ["sandeep.utils.before_job"]
# after_job = ["sandeep.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sandeep.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

