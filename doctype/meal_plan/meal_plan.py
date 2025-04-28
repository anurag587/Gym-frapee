# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MealPlan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		calories: DF.Data | None
		food_items: DF.Data | None
		meal_type: DF.Literal["Breakfast", "Lunch", "Snacks", "Dinner"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		quantity: DF.Data | None
	# end: auto-generated types
	pass
