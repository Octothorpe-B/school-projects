"""Main Python module to handle the creation of the programming language!"""

from sly import Lexer, Parser
import argparse


class MyLexer(Lexer):
    """The Lexer class to store important information about token declarations, values, and error reporting."""
    # Store the token definitions in a dictionary.
    tokens = {
        ID,
        INTVARIABLENAME,
        INTVALUE,
        INTEGERTYPE,
        ADD,
        SUBTRACT,
        DIVIDE,
        MULTIPLY,
        LIST,
        DICTIONARY,
        IF,
        ELSEIF,
        THEN,
        FOR,
        WHILE,
        FUNCTION,
        EQUALS,
        EQUALSTO,
        NOTEQUALSTO,
    }

    literals = {"-", "+", "*", "/", "(", " )", "="}

    # Define id requirements and reserved id keywords ie: foobar.
    ID = r"[a-z_][0-9_]*"
    ID["list"] = LIST
    ID["if"] = IF
    ID["elseif"] = ELSEIF
    ID["then"] = THEN
    ID["while"] = WHILE
    ID["dictionary"] = DICTIONARY
    ID["for"] = FOR
    ID["while"] = WHILE
    ID["function"] = FUNCTION

    # Specififcally define other tokens listed in the "tokens" dictionary.
    LIST = r"LIST"
    IF = r"IF"
    ELSEIF = r"ELIF"
    WHILE = r"WHILE"
    DICTIONARY = r"DICTIONARY"
    FOR = r"FOR"
    FUNCTION = r"FUNCTION"
    EQUALS = r"="
    EQUALSTO = r"&="
    NOTEQUALSTO = r"!="
    ADD = r"\+"
    SUBTRACT = r"-"
    MULTIPLY = r"\*"
    DIVIDE = r"/"

    # Define the singular data type for this programming language, type int (my favorite type)!
    INTEGERTYPE = r"INT"
    INTVALUE = r"[0-9_][0-9_]*"
    INTVARIABLENAME = r"[a-zA-Z_][a-zA-Z_]*"

    # If a new line is detected count it as a new line.
    @_(r"\n+")
    def new_line(self, t):
        self.lineno = t.value.count("\n")

    # If an empty space is detected count it as an empty space.
    @_(r" +")
    def empty_space(self, t):
        self.lineno = t.value.count(" ")

    # Simple Type Checking, if a float value is recognized raise an error and skip the total error fragment.
    @_(r".[0-9_][0-9_]*")
    def float_value_not_accepted_error(self, t):
        print(
            "At Line %d, Float Value Not Accepted %r %r Continued..."
            % (self.lineno, t.value[0], t.value[1])
        )
        self.index += 1

    # Simple Type Checking, If a string value is detected raise an error and skip the total error fragment.
    @_(r"'[a-zA-Z_][a-zA-Z_]*'")
    def string_value_not_accepted_error(self, t):
        print(
            "At Line %d, String Value Not Accepted %r %r Continued..."
            % (self.lineno, t.value[0], t.value[1])
        )
        self.index += 1

    # If the comment symbol "~" is detected skip the comment symbol and proceding message.
    @_(r"~.*")
    def detected_comment(self, t):
        pass

    # If a separate undefined error is detected raise it.
    def error(self, t):
        print("At Line %d, Bad character %r" % (self.lineno, t.value[0]))
        self.index += 1


class MyParser(Parser):
    """Parser class to store information about debugging and how token rules function."""
    # generate the debug file in src containing debugging information.
    debugfile = "parser.out"
    # generate tokens from lexer rules.
    tokens = MyLexer.tokens

    # Define token rules.
    @_("ADD")
    def expr(self, p):
        return ("ADD", p.ADD)

    @_("SUBTRACT")
    def expr(self, p):
        return ("SUBTRACT", p.SUBTRACT)

    @_("MULTIPLY")
    def expr(self, p):
        return ("MULTIPLY", p.MULTIPLY)

    @_("DIVIDE")
    def expr(self, p):
        return ("DIVIDE", p.DIVIDE)

    @_("LIST")
    def data_structure(self, p):
        return ("LIST", p.LIST)

    @_("DICTIONARY")
    def data_structure(self, p):
        return ("DICTIONARY", p.DICTIONARY)

    @_("data_structure")
    def expr(self, p):
        return p

    @_("IF")
    def conditional_statement(self, p):
        return ("IF", p.IF)

    @_("ELSEIF")
    def conditional_statement(self, p):
        return ("ELSEIF", p.ELSEIF)

    @_("THEN")
    def conditional_statement(self, p):
        return ("THEN", p.THEN)

    @_("conditional_statement")
    def expr(self, p):
        return p[0]

    @_("FOR")
    def iterative_logic(self, p):
        return ("FOR", p.FOR)

    @_("WHILE")
    def iterative_logic(self, p):
        return ("WHILE", p.WHILE)

    @_("iterative_logic")
    def expr(self, p):
        return p[0]

    @_("FUNCTION")
    def expr(self, p):
        return ("FUNCTION", p.FUNCTION)

    @_("EQUALSTO")
    def expr(self, p):
        return ("EQUALSTO", p.EQUALSTO)

    @_("NOTEQUALSTO")
    def expr(self, p):
        return ("NOTEQUALSTO", p.NOTEQUALSTO)

    @_("EQUALS")
    def expr(self, p):
        return ("EQUALS", p.EQUALS)

    @_("INTEGERTYPE")
    def expr(self, p):
        return ("INTEGERTYPE", p.INTEGERTYPE)

    @_("INTVARIABLENAME")
    def expr(self, p):
        return ("INTVARIABLENAME", p.INTVARIABLENAME)

    @_("INTVALUE")
    def expr(self, p):
        return ("INTVALUE", p.INTVALUE)

    @_("ID")
    def expr(self, p):
        return ("ID", p.ID)


def read_file(file_name: str):
    """Function to read in the input file and save it in a list."""
    source_code_list = []
    # Open the specified input file and add to list + print out all elements.
    # If the input is a txt file open the file and pull the contents and save into the source code list.
    if ".txt" in file_name:
        with open(file_name) as e:
            source_code_list = list(e)
        print("Printing out the elements from the input file...\n")
        for line in source_code_list:
            print(line)
        return source_code_list


def generate_tokens(List: list, lexer, parser):
    """Function to generate the tokens"""
    token_line_value = 0
    token_counter = 1
    output = []
    # For each line of code in the file get the tokens of a line and append them to the token list.
    print("Printing out the tokens of the input file...\n")
    for element in List:
        for token in lexer.tokenize(element):
            print("Token Type=%r, Token Value=%r" % (token.type, token.value))
            # Save the token type and value as a list within one element of a list.
            token = [token.type, token.value]
            output.append(token)
        token_line_value += 1

    # Display determined tokens in the terminal with their frequency.
    print("\nPrinting out the stored list of the inputted program token list...\n")
    for element in output:
        print("Token Number:", token_counter, element)
        token_counter += 1
    return output


# def generate_scope_table():
#     """Function to create a two dimensional array containing data about the scope of variables in a program."""
#     scope_table = [[1][1]]


if __name__ == "__main__":
    # Create lists to handle line and token frequency and to store code + generated tokens.
    source_code_list = []
    main_source_code_token_list = []
    generated_scopes = []

    # Create a input argument for input file + initializearguments + capture the input file name.
    main_arg_parse = argparse.ArgumentParser()
    main_arg_parse.add_argument(
        "-i", "--input", required=True, help="Input File to run", type=str
    )
    arguments = vars(main_arg_parse.parse_args())
    input_file = arguments["input"]

    print("Thank you for using the Jordan language!")
    # Read in the input file and save in a list.
    source_code_list = read_file(input_file)

    # Create instances of the lexer and parser classes + generate and display tokens.
    lexer = MyLexer()
    parser = MyParser()
    main_source_code_token_list = generate_tokens(source_code_list, lexer, parser)

    # Call the generate scope function.
    # generated_scopes = generate_scope_table()
