# Author: Aidan Goldstein
# Github username: aidangold
# Date: TODO
# Description: TODO

class RealEstateGame:
    """ Class to represent the game object """

    def __init__(self):
        self._game_board = []
        self._players = {}

    def create_spaces(self, go_money, rents):
        """ creates the game spaces for properties and rent, with the amount players receive on landing/passing go """
        count = 0
        go = Property("GO", go_money)
        self._game_board.append(go)
        for rent in rents:
            count += 1
            space = Property(count, rent)
            self._game_board.append(space)

    def create_player(self, name, balance):
        """ adds to the player dict a Player object with the name as they key and the Player object as the value """
        self._players[name] = Player(name, balance)


    def get_player_account_balance(self, name):
        """ Returns the account balance of the player that matches the name parameter """
        target = self._players[name]
        return target.get_balance()

    def get_player_current_position(self, name):
        """ this method similar to the above will use a given player's name and call to the Player class object and
        using the get_position method it will return the integer position on the board of that player. """
        target = self._players[name]
        return target.get_name()

    def buy_space(self, name):
        """ using the name of a player this method will allow that player to buy the property object of the index they
        are currently on. It will allow this to happen only after it checks that the property has no owner, the player
        has the available balance that is greater to the cost of the property. Then this will deduct the amount from
        their account, and add them as the owner of the property by interacting with the Property class and using
        the setter method. If this all is able to occur it return True, else False."""
        target = self._players[name]
        position = target.get_position()
        real_estate = self._game_board[position]
        if target.get_balance() > real_estate.get_cost():
            real_estate.set_owner(name)  # changes owner of the property to the player
            new_bal = target.get_balance() - real_estate.get_cost()
            target.set_balance(new_bal)
            return True
        else:
            return False


    def move_player(self, name, roll_num):
        """ This method will allow a player to move on the game-board. First this will check is the account balance
        of the player 0, if it is it will return. We will make sure the given integer is between 1 and 6. It will
        increase the index the player is on by that given integer. It will need to check if the number will exceed 25
        if it does it will circle back to the 0 index and increase the players account balance by the appropriate
        amount. Then when the player gets to their new spot it will check to see if that spot's property is owned,
        if it is the player will owe money to the player associated with that property in the correct amount. If the
        player's balance would reduce to 0 or below, then that player will become in active."""
        pass

    def check_game_over(self):
        """ This method will check if the game is over by seeing is there is only one player left as active with
        more than 0 in their account balance. If this is the case then this method will return the winning player's
        name. If not then it will return an empty string. """
        pass


class Player:
    """ class to represent the player object and their information """

    def __init__(self, name, initial_balance):
        self._name = name
        self._balance = initial_balance
        self._properties = {}
        self._position = 0

    def get_name(self):
        """ returns the player's name """
        return self._name

    def get_balance(self):
        """ returns player's balance """
        return self._balance

    def set_balance(self, balance):
        """ sets the players account balance to the given amount """
        self._balance = balance

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
game.create_player("Player 1", 1000)
game.create_player("Player 2", 1000)
game.create_player("Player 3", 1000)
game.get_player_account_balance("Player 2")
