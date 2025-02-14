# Copyright (c) 2015, Integra Strategy Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class BudgetAccount(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		account: DF.Link
		budget_amount: DF.Currency
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
