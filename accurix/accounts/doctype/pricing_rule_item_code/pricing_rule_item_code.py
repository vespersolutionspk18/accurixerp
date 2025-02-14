# Copyright (c) 2019, Integra Strategy Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class PricingRuleItemCode(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		item_code: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		uom: DF.Link | None
	# end: auto-generated types

	pass
