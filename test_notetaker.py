import unittest
from note_taker import NoteTaker  

class TestNoteTaker(unittest.TestCase):

    def setUp(self):
        self.note_taker = NoteTaker()

    def test_add_note(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.assertEqual(len(self.note_taker.notes), 1)
        self.assertEqual(self.note_taker.notes[0]["title"], "Test Note")

    def test_view_note(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        content = self.note_taker.view_note("Test Note")
        self.assertEqual(content, "This is a test note.")

    def test_edit_note(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.edit_note("Test Note", "Edited content")
        content = self.note_taker.view_note("Test Note")
        self.assertEqual(content, "Edited content")

    def test_delete_note(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.delete_note("Test Note")
        self.assertEqual(len(self.note_taker.notes), 0)

    def test_list_notes(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.add_note("Another Note", "Another test note.")

    def test_add_tag(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.add_tag("Test Note", "test")
        self.assertIn("test", self.note_taker.notes[0]["tags"])

    def test_search_notes_by_tag(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.add_tag("Test Note", "test")

    def test_archive_note(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.archive_note("Test Note")
        self.assertEqual(len(self.note_taker.archived_notes), 1)
        self.assertEqual(len(self.note_taker.notes), 0)

    def test_restore_note(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.archive_note("Test Note")
        self.note_taker.restore_note("Test Note")
        self.assertEqual(len(self.note_taker.archived_notes), 0)
        self.assertEqual(len(self.note_taker.notes), 1)

    def test_list_archived_notes(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.archive_note("Test Note")

    def test_set_priority(self):
        self.note_taker.add_note("Test Note", "This is a test note.")
        self.note_taker.set_priority("Test Note", 2)
        self.assertEqual(self.note_taker.notes[0]["priority"], 2)

    def test_sort_notes_by_priority(self):
        self.note_taker.add_note("Low Priority", "This is a low priority note.")
        self.note_taker.add_note("High Priority", "This is a high priority note.")
        self.note_taker.set_priority("Low Priority", 1)
        self.note_taker.set_priority("High Priority", 2)
        self.note_taker.sort_notes_by_priority()
        self.assertEqual(self.note_taker.notes[0]["title"], "Low Priority")
        self.assertEqual(self.note_taker.notes[1]["title"], "High Priority")

if __name__ == '__main__':
    unittest.main()
