from tictactoe_xm2312.tictactoe_xm2312 import *
def test_initialize_board():
    board = initialize_board()

    expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    assert board == expected_board, "The board was not initialized correctly."


def test_initialize_board():
    board = initialize_board()
    expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert board == expected_board, "The board was not initialized correctly."

def test_make_move_valid():
    board = initialize_board()

    assert make_move(board, 0, 0, 'X') == True, "'X' move was not successful"
    assert board[0][0] == 'X', "'X' was not placed correctly on the board"

    assert make_move(board, 1, 1, 'O') == True, "'O' move was not successful"
    assert board[1][1] == 'O', "'O' was not placed correctly on the board"