# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Membership(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		branch: DF.Literal["Krishna Nagar", "Noida", "Gurugram"]
		packages: DF.Literal["Monthly", "Quarterly", "Yearly"]
		status: DF.Literal["Active", "Not Active"]
		user: DF.Link | None
	# end: auto-generated types
	pass
