class NoteTaker:
    def __init__(self):
        self.notes = []
        self.archived_es = []

    def add_note(self, title, content):
        self.notes.append({"title": title, "content": content, "tags": [], "priority": 0})
        print(f"Note '{title}' added.")

    def view_note(self, title):
        for note in self.notes:
            if note["title"] == title:
                return note["content"]
        return f"Note '{title}' not found."

    def edit_note(self, title, new_content):
        for note in self.notes:
            if note["title"] == title:
                note["content"] = new_content
                print(f"Note '{title}' edited.")
                return
        print(f"Note '{title}' not found.")

    def delete_note(self, title):
        for note in self.notes:
            if note["title"] == title:
                self.notes.remove(note)
                print(f"Note '{title}' deleted.")
                return
        print(f"Note '{title}' not found.")

    def list_notes(self):
        if self.notes:
            print("Notes:")
            for note in self.notes:
                print(f"- {note['title']} (Priority: {note['priority']})")
        else:
            print("No notes available.")

    def add_tag(self, title, tag):
        for note in self.notes:
            if note["title"] == title:
                note["tags"].append(tag)
                print(f"Tag '{tag}' added to note '{title}'.")

    def search_notes_by_tag(self, tag):
        matching_notes = []
        for note in self.notes:
            if tag in note["tags"]:
                matching_notes.append(note["title"])
        if matching_notes:
            print(f"Notes with tag '{tag}':")
            for title in matching_notes:
                print(f"- {title}")
        else:
            print(f"No notes found with tag '{tag}'.")

    def archive_note(self, title):
        for note in self.notes:
            if note["title"] == title:
                archived_note = self.notes.pop(self.notes.index(note))
                self.archived_notes.append(archived_note)
                print(f"Note '{title}' archived.")

    def restore_note(self, title):
        for archived_note in self.archived_notes:
            if archived_note["title"] == title:
                restored_note = self.archived_notes.pop(self.archived_notes.index(archived_note))
                self.notes.append(restored_note)
                print(f"Note '{title}' restored.")

    def list_archived_notes(self):
        if self.archived_notes:
            print("Archived Notes:")
            for note in self.archived_notes:
                print(f"- {note['title']} (Priority: {note['priority']})")
        else:
            print("No archived notes available.")

    def set_priority(self, title, priority):
        for note in self.notes:
            if note["title"] == title:
                note["priority"] = priority
                print(f"Priority of note '{title}' set to {priority}.")

    def sort_notes_by_priority(self):
        self.notes.sort(key=lambda x: x["priority"])

# Create an instance of the NoteTaker class
note_taker = NoteTaker()

# Example usage of the functions
note_taker.add_note("Meeting Notes", "Discuss project timeline.")
note_taker.add_note("Grocery List", "Milk, eggs, bread, and bananas")

note_taker.add_tag("Meeting Notes", "work")
note_taker.add_tag("Grocery List", "shopping")

note_taker.set_priority("Meeting Notes", 2)
note_taker.set_priority("Grocery List", 1)

note_taker.sort_notes_by_priority()

note_taker.list_notes()
