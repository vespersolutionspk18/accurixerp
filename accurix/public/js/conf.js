// Copyright (c) 2015, Integra Strategy Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide("accurix");

// preferred modules for breadcrumbs
$.extend(frappe.breadcrumbs.preferred, {
	"Item Group": "Stock",
	"Customer Group": "Selling",
	"Supplier Group": "Buying",
	Territory: "Selling",
	"Sales Person": "Selling",
	"Sales Partner": "Selling",
	Brand: "Stock",
	"Maintenance Schedule": "Support",
	"Maintenance Visit": "Support",
});

$.extend(frappe.breadcrumbs.module_map, {
	"accurix Integrations": "Integrations",
	Geo: "Settings",
	Portal: "Website",
	Utilities: "Settings",
	"E-commerce": "Website",
	Contacts: "CRM",
});
