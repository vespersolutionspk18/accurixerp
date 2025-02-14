import unittest

import frappe
from frappe.tests import IntegrationTestCase

from accurix import encode_company_abbr

EXTRA_TEST_RECORD_DEPENDENCIES = ["Company"]


class TestInit(IntegrationTestCase):
	def test_encode_company_abbr(self):
		abbr = "NFECT"

		names = [
			"Warehouse Name",
			"accurix Foundation India",
			f"Gold - Member - {abbr}",
			f" - {abbr}",
			"accurix - Foundation - India",
			f"accurix Foundation India - {abbr}",
			f"No-Space-{abbr}",
			"- Warehouse",
		]

		expected_names = [
			f"Warehouse Name - {abbr}",
			f"accurix Foundation India - {abbr}",
			f"Gold - Member - {abbr}",
			f" - {abbr}",
			f"accurix - Foundation - India - {abbr}",
			f"accurix Foundation India - {abbr}",
			f"No-Space-{abbr} - {abbr}",
			f"- Warehouse - {abbr}",
		]

		for i in range(len(names)):
			enc_name = encode_company_abbr(names[i], abbr=abbr)
			self.assertTrue(
				enc_name == expected_names[i],
				f"{enc_name} is not same as {expected_names[i]}",
			)

	def test_translation_files(self):
		from frappe.tests.test_translate import verify_translation_files

		verify_translation_files("accurix")

	def test_patches(self):
		from frappe.tests.test_patches import check_patch_files

		check_patch_files("accurix")
