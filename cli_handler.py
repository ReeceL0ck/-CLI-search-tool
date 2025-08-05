import sys
from ebay.api_handler import API_Handler

class CLI_Handler():
    def __init__(self):
        self.arguements = sys.argv
        self.API_Handler = API_Handler()
    
    def input_validator(self):
        print(self.arguements)
        if len(self.arguements) < 2:
            raise SyntaxError("Error - No arguments found")
        if len(self.arguements) == 2:
            raise SyntaxError("No search term provided - please provide a search term")
        if self.arguements[1].lower() != "search":
            raise SyntaxError(f"Error -search not  found - {self.arguements[1]}")
        if len(self.arguements) > 10:
            raise SyntaxError(f"Error - Too many arguments - found {len(self.arguements)} where max is 10")
        return True

    def _get_search_term(self):
        self.input_validator()
        seach_term = " ".join(self.arguements[2:])
        
        print(f"Search term: {seach_term}")
        return seach_term
    
    def _get_api_response(self):
        response = self.API_Handler._test("Test parameter")
        # print(response)
        # return response



cli_handler = CLI_Handler()


cli_handler._get_search_term()
cli_handler._get_api_response()