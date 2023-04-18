import unittest
import calculate


class TestSentences(unittest.TestCase):
    def test_all_sentences_1(self):
        self.assertEqual(calculate.all_sentences("I love python!!!"), 1)

    def test_all_sentences_2(self):
        self.assertEqual(calculate.all_sentences("Do you love python, Mr. Pliska?"), 1)

    def test_all_sentences_3(self):
        self.assertEqual(calculate.all_sentences("I love python..."), 1)

    def test_non_declarative_sentences(self):
        self.assertEqual(calculate.calc_non_declarative_sentences("I love python! What about you, Mr. Pliska?"
                                                                  "I love python too..."), 2)


    def test_count_words(self):
        self.assertEqual(calculate.count_words("I love python!!!"), 3)

    def test_average_length_of_sentences(self):
        self.assertEqual(calculate.average_length_of_sentence("GO placidly amid the noise and haste,"
                                                              "and remember what peace there may be in silence."
                                                              "As far as possible without surrender"
                                                              "be on good terms with all persons."), 64)


    def test_average_length_of_words(self):
        self.assertEqual(calculate.average_length_of_words("GO placidly amid the noise and haste,"
                                                              "and remember what peace there may be in silence."
                                                              "As far as possible without surrender"
                                                              "be on good terms with all persons."), 5)


    def test_delete_numbers(self):
        self.assertEqual(calculate.delete_numbers("aaaa 1999 ddddd888ddd ddddd999 9999dddd"),
                         "aaaa ddddd888ddd ddddd999 9999dddd")


    def test_count_characters(self):
        self.assertEqual(calculate.count_characters("I love python!!!"), 11)


    def test_get_top_ngrams(self):
        self.assertEqual(calculate.get_top_ngrams("I love python!!!", 2, 2),
                         "[(('i', 'love'), 1), (('love', 'python'), 1)]")

if __name__ == '__main__':
    unittest.main()
