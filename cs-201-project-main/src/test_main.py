"""Test module for main.py to ensure correctness of lexer + parser classes and other functions."""

import main
import pytest


def test_one_file_reading():
    """Test to determine that the correctness of the file reading functionality of main.py"""
    test_input = "input/input.txt"
    test_str_output = []
    # Read in the string and convert to a list.
    test_str_output = main.read_file(test_input)

    # Assert that the output is not empty.
    assert test_str_output != 0


def test_two_generate_tokens_is_not_empty():
    """Test to assure that the correct tokens are being generated and not returning an empty value."""
    # initialize variables used for testing.
    test_input = "="
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    # Read in the string and convert to a list.
    test_token_output = main.generate_tokens(list(test_input), lexer, parser)

    # assert that data has been put in test_token_output list.
    assert test_token_output != 0


def test_three_special_case_token_list():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "IF"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    # ensure that the parser produces the right output for the provided input.
    output = parser.parse(lexer.tokenize(test_input))
    assert output == ("IF", "IF")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["IF", "IF"]


def test_four_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "LIST"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    # ensure that the parser produces the right output for the provided input.
    output = parser.parse(lexer.tokenize(test_input))
    assert output == ("expr", ("LIST", "LIST"))

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["LIST", "LIST"]


def test_five_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "="
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("EQUALS", "=")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["EQUALS", "="]


def test_six_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "WHILE"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("WHILE", "WHILE")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["WHILE", "WHILE"]


def test_seven_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "DICTIONARY"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("expr", ("DICTIONARY", "DICTIONARY"))

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["DICTIONARY", "DICTIONARY"]


def test_eight_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "FUNCTION"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("FUNCTION", "FUNCTION")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["FUNCTION", "FUNCTION"]


def test_nine_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "INT"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("INTEGERTYPE", "INT")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["INTEGERTYPE", "INT"]


def test_ten_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "B"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("INTVARIABLENAME", "B")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["INTVARIABLENAME", "B"]


def test_eleven_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "&="
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("EQUALSTO", "&=")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == [("EQUALSTO", "&=")]


def test_twelve_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "!="
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("NOTEQUALSTO", "!=")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == [("NOTEQUALSTO", "!=")]


def test_eleven_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "&="
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("EQUALSTO", "&=")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["EQUALSTO", "&="]


def test_twelve_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "+"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("ADD", "+")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["ADD", "+"]


def test_thirteen_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "-"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("SUBTRACT", "-")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["SUBTRACT", "-"]


def test_fourteen_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "*"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("MULTIPLY", "*")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["MULTIPLY", "*"]


def test_fifeteen_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "/"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("DIVIDE", "/")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["DIVIDE", "/"]


def test_sixteen_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "ELIF"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("ELSEIF", "ELIF")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["ELSEIF", "ELIF"]


def test_seventeen_special_case_token():
    """Test to ensure the parser processes a particular token correctly."""
    # initialize variables used for testing.
    test_input = "9"
    test_str_output = []
    test_token_output = []

    # initialize lexer and parser objects from the mylexer and myparser classes.
    lexer = main.MyLexer()
    parser = main.MyParser()

    output = parser.parse(lexer.tokenize(test_input))
    # ensure that the parser produces the right output for the provided input.
    assert output == ("INTVALUE", "9")

    # add the test input to the str output.
    test_str_output.append(test_input)
    # generate the tokens in main.
    test_token_output = main.generate_tokens(test_str_output, lexer, parser)

    # ensure that the token output has data
    assert len(test_token_output) != 0
    # ensure that the token output has the right amount of data.
    assert len(test_token_output) == 1
    # ensure that the token output has the precise expected output in the list.
    assert test_token_output[0] == ["INTVALUE", "9"]


# def test_genereate_scope_table():
#     """Test to verify the generate_scope_table is validated for correctness."""
#     # initialize variables used for testing.
#     test_input = "IF A = B"
#     test_str_output = []
#     test_token_output = []
#     test_scope_table = []

#     # initialize lexer and parser objects from the mylexer and myparser classes.
#     lexer = main.MyLexer()
#     parser = main.MyParser()

#     # Read in the string and convert to a list.
#     test_output = main.read_file(test_input)
#     test_token_output = main.generate_tokens(test_str_output, lexer, parser)
#     # test_scope_table = main.generate_scope_table(test_token_output)

#     # Ensure that the length of the scope table is not 0.
#     # assert test_scope_table != 0
