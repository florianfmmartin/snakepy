# imports
import blessed

# class Term
class Term:
    # init
    def __init__(self):
        self.term = blessed.Terminal()
        self.width = self.term.width
        self.height = self.term.height
