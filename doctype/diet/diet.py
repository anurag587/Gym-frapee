# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Diet(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.gym.doctype.meal_plan.meal_plan import MealPlan
		from frappe.types import DF

		date: DF.Date | None
		diet_type: DF.Literal["Cutting", "Bulking", "Maintain"]
		meal_type: DF.Table[MealPlan]
		user: DF.Link | None
	# end: auto-generated types
	pass
