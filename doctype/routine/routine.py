# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Routine(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.gym.doctype.routine_exercise.routine_exercise import RoutineExercise
		from frappe.types import DF

		accuracy: DF.Float
		day: DF.Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		end_time: DF.Time | None
		exercise_list: DF.Table[RoutineExercise]
		level: DF.Literal["Beginner", "Intermediate", "Expert"]
		start_time: DF.Time | None
		title: DF.Data | None
	# end: auto-generated types
	pass
