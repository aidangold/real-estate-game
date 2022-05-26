# Author: Aidan Goldstein
# Github username: aidangold
# Date: TODO
# Description: TODO

class RealEstateGame:
    """ Class to represent the game object """

    def __init__(self):
        self._game_board = []

    def create_spaces(self, go_money, rents):
        """ creates the game spaces for properties and rent, with the amount players receive on landing/passing go """

        self._game_board.append("GO")


class Player:
    """ class to represent the player object and their information """

    def __init__(self, name, initial_balance):
        self._name = name
        self._balance = initial_balance
        self._properties = {}
        self._position = 0

    def get_balance(self):
        """ returns player's balance """
        return self._balance

    def get_properties(self):
        """ returns player's properties """
        return self._properties

    def get_position(self):
        """ returns player's position on the game board """
        return self._position


class Property:
    """ class to represent each property object that will be bought and used on spaces """

    def __init__(self, name, rent):
        self._owner = None
        self._rent = rent
        self._cost = rent * 5
        self._name = name

    def set_owner(self, player):
        """ sets the owner of the property to the player who purchased it """
        self._owner = player

    def get_rent(self):
        """ returns the rent amount for the property """
        return self._rent

    def get_cost(self):
        """ returns the cost of the property if it were to be purchased by a player """
        return self._cost

    def get_property_name(self):
        """ returns the property name """
        return self._name


game = RealEstateGame()

rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350, 350,
         350]
game.create_spaces(50, rents)
