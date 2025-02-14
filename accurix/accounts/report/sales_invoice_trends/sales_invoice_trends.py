# Copyright (c) 2015, Integra Strategy Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from accurix.controllers.trends import get_columns, get_data


def execute(filters=None):
	if not filters:
		filters = {}
	data = []
	conditions = get_columns(filters, "Sales Invoice")
	data = get_data(filters, conditions)

	return conditions["columns"], data
