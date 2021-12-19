import datetime as dt
import unittest

from Budget.Components.Account.Src.TransactionData import TransactionData


class TestTransactionData(unittest.TestCase):
    def setUp(self):
        self.amount = 25000.0
        self.date = dt.date(2021, 12, 4)
        self.description = "Lön"
        self.tag = "default"

        self.new_amount = 2000.0
        self.new_date = dt.date(2021, 11, 12)
        self.new_description = "Övrigt"
        self.new_tag = "change"


    def testCreateTransactionData(self):
        tags = [self.tag]

        # ### Create TransactionData ###
        td = TransactionData(self.amount,
                             self.date,
                             self.description,
                             tags)

        self.assertEqual(td.get_amount(), self.amount)
        self.assertEqual(td.get_date(), self.date)
        self.assertEqual(td.get_description(), self.description)
        self.assertEqual(td.get_tags(), tags)

        id = td.get_id()
        id_parts = id.split('-')
        id_length = sum(map(len, id_parts))

        self.assertEqual(id_length, 50)


    def testUpdateTransactionDataFields(self):
        tags = [self.tag]

        # ### Create TransactionData ###
        td = TransactionData(self.amount,
                             self.date,
                             self.description,
                             tags)

        id = td.get_id()

        # ### Update TransactionData using setters ###
        td.set_amount(self.new_amount)
        td.set_date(self.new_date)
        td.set_description(self.new_description)

        self.assertEqual(td.get_amount(), self.new_amount)
        self.assertEqual(td.get_date(), self.new_date)
        self.assertEqual(td.get_description(), self.new_description)
        self.assertEqual(td.get_id(), id)


    def testchangeTransactionDataTags(self):
        tags = [self.tag]

        # ### Create TransactionData ###
        td = TransactionData(self.amount,
                             self.date,
                             self.description,
                             tags)

        id = td.get_id()

        self.assertEqual(td.get_tags(), tags)

        # ### Update tags ###
        tags.append(self.new_tag)
        td.add_tag(self.new_tag)

        self.assertEqual(td.get_tags(), tags)

        # ### Clear tags ###
        td.clear_tags()

        self.assertEqual(td.get_tags(), [])

        # ### Test remove_tag ###

        # Add new tag to empty list
        self.assertTrue(td.add_tag(self.tag))
        # Add new tag to list
        self.assertTrue(td.add_tag(self.new_tag))
        # Add already existing tag to list
        self.assertFalse(td.add_tag(self.new_tag))
        # Check that all tags added correctly
        self.assertEqual(td.get_tags(), tags)
        # Remove first tag from list
        self.assertTrue(td.remove_tag(self.tag))
        # Check that correct tag was removed
        self.assertEqual(td.get_tags(), [self.new_tag])
        # Remove second tag
        self.assertTrue(td.remove_tag(self.new_tag))
        # Check that the tag was removed
        self.assertEqual(td.get_tags(), [])
        # Try to remove tag from empty list
        self.assertFalse(td.remove_tag(self.tag))

        # Check that nothing else changed
        self.assertEqual(td.get_amount(), self.amount)
        self.assertEqual(td.get_date(), self.date)
        self.assertEqual(td.get_description(), self.description)
        self.assertEqual(td.get_id(), id)


if __name__ == "__main__":
    unittest.main()
