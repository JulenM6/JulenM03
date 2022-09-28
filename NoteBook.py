import datetime
import sys

last_id = 0

class Note:
    
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags
    
class Notebook:
    
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def search(self, filter):
        return [note for note in self.notes if
                note.match(filter)]
    
class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.opcions = {
                "1": self.show_notes,
                "2": self.search_notes,
                "3": self.add_note,
                "4": self.quit
                }

    def display_menu(self):
        print("""
Menu Llibreta
1. Veure totes les notes
2. Buscar notes
3. Afegir nota
4. Sortir
""")

    def run(self):
        while True:
            self.display_menu()
            escull = input("Escull una opcio: ")
            action = self.opcions.get(escull)
            if action:
                action()
            else:
                print("{0} no es una opcio valida".format(escull))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(note.id, note.tags, note.memo, note.date)
            

    def search_notes(self):
        filter = input("Buscar: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Afegeix la memo: ")
        tags = input("Afegeix tags: ")
        self.notebook.new_note(memo, tags)
       
        print("La teva nota s'ha afegit")

    def quit(self):
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()