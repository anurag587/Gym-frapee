# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Goal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		deadline: DF.Date | None
		goal_type: DF.Literal["Lift", "Weight"]
		target_lift: DF.Float
		target_weight: DF.Float
		user: DF.Link | None
	# end: auto-generated types
	pass
