import unittest

import frappe
from frappe.tests import IntegrationTestCase

import accurix


@accurix.allow_regional
def test_method():
	return "original"


class TestInit(IntegrationTestCase):
	def test_regional_overrides(self):
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
