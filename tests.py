from overhoor import *

import unittest

class OverhoorTests(unittest.TestCase):
    def test_check_correct(self):
        self.assertTrue(check_correct("yes", "yes"))
        self.assertFalse(check_correct("yes", ""))
        self.assertFalse(check_correct("yes", 1))


    def test_check_meaning(self):
        DATA = [["One", "Een"], ["Two", "Twee"]]
        self.assertTrue(get_meaning(1, DATA), "Twee")


    def test_pick_random_new_question(self):
        DATA = [["Hi", "Hoi"], ["Bye", "Doei"]]
        question_no, asked_questions_list = pick_random_new_question([0], DATA)
        expected_number = 1
        expected_list = [0, 1]
        self.assertEqual(question_no, expected_number)
        self.assertEqual(asked_questions_list, expected_list)
        self.assertNotEqual(question_no, 0)


    def test_do_administration(self):
        n_correct, n_wrong, questions_to_repeat, final_repeat_list = do_administration(False, 1, 0, 0, [], [])
        expected_ncorrect = 0
        expected_nwrong = 1
        self.assertEqual(n_correct, expected_ncorrect)
        self.assertEqual(n_wrong, expected_nwrong)
        self.assertEqual(questions_to_repeat, [False, False, 1])
        self.assertEqual(final_repeat_list, [1])
        n_correct, n_wrong, questions_to_repeat, final_repeat_list = do_administration(True, 1, 0, 0, [], [])
        expected_ncorrect = 1
        expected_nwrong = 0
        self.assertEqual(n_correct, expected_ncorrect)
        self.assertEqual(n_wrong, expected_nwrong)
        self.assertEqual(questions_to_repeat, [])
        self.assertEqual(final_repeat_list, [])


    def test_repeat_question(self):
        result_repeat_list = repeat_question([0], [["Hoi", "Hi"]])
        expected = []
        self.assertEqual(result_repeat_list, expected)
        result_repeat_list = repeat_question([False, 0], [["Hoi", "Hi"]])
        expected = [0]
        self.assertEqual(result_repeat_list, expected)
        result_repeat_list = repeat_question([False, False, 0], [["Hoi", "Hi"]])
        expected = [False, 0]
        self.assertEqual(result_repeat_list, expected)

if __name__ == '__main__': 
    unittest.main()
