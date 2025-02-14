# Copyright (c) 2013, Integra Strategy Pvt. Ltd. and contributors
# For license information, please see license.txt


from accurix.selling.report.sales_analytics.sales_analytics import Analytics


def execute(filters=None):
	return Analytics(filters).run()
