import pytest
import mock
from ttt import Board
from ttt import Player
from ttt import TicTacToe

@pytest.fixture
def board():
    board = Board()
    return board

@pytest.fixture
def player():
    player = Player('X')
    return player

@pytest.fixture
def ttt():
    playerX = Player('X')
    playerO = Player('O')
    board = Board()
    ttt = TicTacToe(board, playerX, playerO)
    return ttt

# Controls the game play
#class TicTacToe
    # initialize
        # set up the board
        # set up the players
        # assign the starting player


    # play
        # loop infinitely
            # call the board rendering method
            # ask for coordinates from the current player
            # break the loop IF the game is over
            # switch players

    # check_game_over
        # check_victory
        # check_draw
def test_TicTacToe_check_game_over(ttt):
    assert ttt.check_game_over() == False
    for i in range(6,9):
        ttt.board.add_piece(i)
    assert ttt.check_game_over() == True

    # check_victory
        # IF board says current player's piece has
        # a winning_combination?
            # display a victory message
def test_TicTacToe_check_victory(ttt):
    assert ttt.check_victory() == False
    for i in range(3):
        ttt.board.add_piece(i)
    assert ttt.check_victory() == True

    # check_draw
        # IF Board says we've filled up
            # display a draw message
def test_TicTacToe_check_draw(ttt):
    assert ttt.check_draw() == False
    for i in range(len(ttt.board.state)):
        ttt.board.add_piece(i)
    assert ttt.check_draw() == True
    

    # switch_players
        # PlayerX >> PlayerO or vice versa
def test_TicTacToe_switch_players(ttt):
    assert ttt.player.marker == 'X'
    ttt.switch_players()
    assert ttt.player.marker == 'O'

# Manages all player-related functionality
#class Player
    # initialize
        # Set marker type (e.g. X or O)
def test_Player_init(player):
	assert player.marker == "X"
	
    # get_coordinates
        # loop infinitely
            # ask_for_coordinates
            # IF validate_coordinates_format is true
                # IF piece can be placed on Board
                    # break the loop

    # ask_for_coordinates
        # Display message asking for coordinates
        # pull coordinates from command line


    # validate_coordinates_format
        # UNLESS coordinates are in the proper format
            # display error message
def test_Player_validate_coordinates_format(player):
	assert player.validate_coordinates_format(8) == True
	assert player.validate_coordinates_format('O') == False


# Maintains game board state
#class Board
    # initialize board
        # set up blank data structure
def test_Board_init(board):
	empty = 0
	assert all(board.state) == empty

    # render
        # loop through data structure
           # display an existing marker if any, else blank
'''
def test_Board_render():
	board = Board()
	assert board.render() == "1 2 3\n4 5 6\n7 8 9\n"
'''

    # add_piece
        # IF piece_location_valid?
            # place piece
        # ELSE
            # display error message
def test_Board_add_piece(board):
	board.add_piece(0)
	assert board.state[0] != 0
	  
    # piece_location_valid?
        # Is the placement within_valid_coordinates?
        # Are the piece coordinates_available?
def test_Board_piece_location_valid(board):
	assert board.piece_location_valid(4) == True
	assert board.piece_location_valid(-1) == False

    # within_valid_coordinates?
        # UNLESS piece coords are in the acceptible range
            # display an error message
def test_Board_within_valid_coordinates(board):
	assert board.within_valid_coordinates(0) == True
	assert board.within_valid_coordinates(8) == True
	assert board.within_valid_coordinates(9) == False
	
    # coordinates_available?
        # UNLESS piece coords are not occupied
            # display error message
def test_Board_coordinates_available(board):
	assert board.coordinates_available(0) == True
	board.add_piece(0)
	assert board.coordinates_available(0) == False
	
    # winning_combination?
        # is there a winning_diagonal?
        # or winning_vertical? 
        # or winning_horizontal? for that piece?
@pytest.mark.parametrize("fst, snd, trd", [
    (0, 4, 8), (0, 3, 6), (0, 1, 2)]) 
def test_Board_winning_combination(board, fst, snd, trd):
    assert board.winning_combination() == False
    board.add_piece(fst)
    board.add_piece(trd)
    assert board.winning_combination() == False
    board.add_piece(snd)
    assert board.winning_combination() == True

    # winning_diagonal?
        # check if specified piece has a triplet across diagonals
@pytest.mark.parametrize("fst, snd, trd", [
    (0, 4, 8), (2, 4, 6),]) 
def test_Board_winning_diagonal(board, fst, snd, trd):
	board.add_piece(fst)
	board.add_piece(trd)
	assert board.winning_diagonal() == False
	board.add_piece(snd)
	assert board.winning_diagonal() == True
    
    # winning_vertical?
        # check if specified piece has a triplet across verticals
@pytest.mark.parametrize("fst, snd, trd", [
    (0, 3, 6), (1, 4, 7), (2, 5, 8),])
def test_Board_winning_vertical(board, fst, snd, trd):
	board.add_piece(fst)
	board.add_piece(trd)
	assert board.winning_vertical() == False
	board.add_piece(snd)
	assert board.winning_vertical() == True

    # winning_horizontal?
        # check if specified piece has a triplet across horizontals
@pytest.mark.parametrize("fst, snd, trd", [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),])
def test_Board_winning_horizontal(board, fst, snd, trd):
	board.add_piece(fst)
	board.add_piece(trd)
	assert board.winning_horizontal() == False
	board.add_piece(snd)
	assert board.winning_horizontal() == True
    # diagonals
        # return the diagonal pieces

    # verticals
        # return the vertical pieces

    # horizontals
        # return the horizontal pieces

    # full?
        # does every square contain a piece?
def test_Board_is_full(board):
    assert board.is_full() == False
    board.add_piece(0)
    assert board.is_full() == False
    for i in range(1,len(board.state)):
        board.add_piece(i)
    assert board.is_full() == True
