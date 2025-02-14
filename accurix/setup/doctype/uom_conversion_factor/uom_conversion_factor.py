# Copyright (c) 2018, Integra Strategy Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class UOMConversionFactor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Link
		from_uom: DF.Link
		to_uom: DF.Link
		value: DF.Float
	# end: auto-generated types

	pass
