# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Exercise(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Literal["BodyWeight", "Cardio", "Strength", "Mobility"]
		name1: DF.Data
		target_muscle_group: DF.Literal["Chest", "Back", "Legs", "Arms", "Shoulders", "Core", "Full Body"]
	# end: auto-generated types
	pass
