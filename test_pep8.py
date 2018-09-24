import pep8
import unittest

# no need to import
CHECK_FILE = ['a2.py']


class Test_PEP8(unittest.TestCase):
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(CHECK_FILE)
        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
