// Copyright (c) 2016, Integra Strategy Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["BOM Explorer"] = {
	filters: [
		{
			fieldname: "bom",
			label: __("BOM"),
			fieldtype: "Link",
			options: "BOM",
			reqd: 1,
		},
	],
};
