// Copyright (c) 2016, Integra Strategy Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("GL Entry", {
	refresh: function (frm) {
		frm.page.btn_secondary.hide();
	},
});
