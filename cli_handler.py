import sys

class CLI_Handler():
    def __init__(self):
        pass

    def arguements_handler(self, arguements=sys.argv):
        self.arguements = arguements
        return self.arguements
    
    def input_validator(self):
        self.arguements_handler()
        print(self.arguements)
        if self.arguements[1].lower() != "search":
            raise ValueError(f"Error - did not start with search insead found - {self.arguements[1]}")
        if len(self.arguements) > 10:
            raise SyntaxError(f"Error - Too many arguments - found {len(self.arguements)} where max is 10")
        

       


        return True



cli_handler = CLI_Handler()


cli_handler.input_validator()
