# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RoutineExercise(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		exercise: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		reps: DF.Int
		sets: DF.Int
	# end: auto-generated types
	pass
