#!/usr/bin/env python3
"""Tests for expense-total.py using Python's built-in unittest."""

import importlib.util
import io
import os
import sys
import tempfile
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
_SOURCE = os.path.join(_HERE, "expense-total.py")
_SPEC = importlib.util.spec_from_file_location("expense_total", _SOURCE)
_expense_total = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_expense_total)
total_expenses = _expense_total.total_expenses
main = _expense_total.main


class TestParseAmount(unittest.TestCase):
    """The parse_amount logic is exercised through total_expenses."""

    def test_valid_amount(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("12.50\n")
            name = f.name
        try:
            total, warnings = total_expenses(name)
            self.assertEqual(total, 12.50)
            self.assertEqual(warnings, [])
        finally:
            os.unlink(name)

    def test_blank_line_ignored(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("\n\n12.50\n")
            name = f.name
        try:
            total, warnings = total_expenses(name)
            self.assertEqual(total, 12.50)
            self.assertEqual(warnings, [])
        finally:
            os.unlink(name)

    def test_comment_line_ignored(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("# this is a comment\n12.50\n")
            name = f.name
        try:
            total, warnings = total_expenses(name)
            self.assertEqual(total, 12.50)
            self.assertEqual(warnings, [])
        finally:
            os.unlink(name)

    def test_invalid_line_skipped_with_warning(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("10.00\nnot-a-number\n20.00\n")
            name = f.name
        try:
            total, warnings = total_expenses(name)
            self.assertEqual(total, 30.00)
            self.assertEqual(len(warnings), 1)
            self.assertIn("not-a-number", warnings[0])
        finally:
            os.unlink(name)

    def test_multiple_amounts_summed(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("12.50\n3.75\n8.00\n22.10\n")
            name = f.name
        try:
            total, warnings = total_expenses(name)
            self.assertAlmostEqual(total, 46.35)
            self.assertEqual(warnings, [])
        finally:
            os.unlink(name)


class TestMain(unittest.TestCase):
    """Tests for the command-line entry point."""

    def run_main(self, args, stdin=None):
        old_stdout = sys.stdout
        old_argv = sys.argv
        sys.stdout = io.StringIO()
        sys.argv = ["expense-total.py"] + args
        try:
            code = main(["expense-total.py"] + args)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        return code, output

    def test_missing_file(self):
        code, output = self.run_main(["nonexistent_file_12345.txt"])
        self.assertNotEqual(code, 0)
        self.assertIn("Error", output)

    def test_no_arguments(self):
        code, output = self.run_main([])
        self.assertNotEqual(code, 0)
        self.assertIn("Usage", output)

    def test_successful_run(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("10.00\n20.00\n")
            name = f.name
        try:
            code, output = self.run_main([name])
            self.assertEqual(code, 0)
            self.assertIn("Total: $30.00", output)
        finally:
            os.unlink(name)

    def test_invalid_line_warning(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("5.00\nbad\n")
            name = f.name
        try:
            code, output = self.run_main([name])
            self.assertEqual(code, 0)
            self.assertIn("skipping invalid amount", output)
            self.assertIn("bad", output)
            self.assertIn("Total: $5.00", output)
        finally:
            os.unlink(name)


if __name__ == "__main__":
    import sys

    unittest.main()
