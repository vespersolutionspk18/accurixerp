// Copyright (c) 2019, Integra Strategy Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Newsletter", {
	refresh() {
		accurix.toggle_naming_series();
	},
});
