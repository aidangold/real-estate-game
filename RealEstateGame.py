# Author: Aidan Goldstein
# Github username: aidangold
# Date: TODO
# Description: TODO

class RealEstateGame:
    """ Class to represent the game object """

    def __init__(self):
        self._game_board = []
        self._players = {}
        self._go_money = 0

    def create_spaces(self, go_money, rents):
        """ creates the game spaces for properties and rent, with the amount players receive on landing/passing go """
        count = 0
        self._go_money = go_money
        go = Property("GO", go_money)
        self._game_board.append(go)
        for rent in rents:
            count += 1
            space = Property(count, rent)
            self._game_board.append(space)

    def create_player(self, name, balance):
        """ adds to the player dict a Player object with the name as they key and the Player object as the value """
        self._players[name] = Player(name, balance)

    def get_player_account_balance(self, name: str) -> int:
        """
        Returns the account balance of the player that matches the name parameter
        :param: name (str): unique name for player object.
        :returns: balance (int): integer value of player's remaining balance.
        """
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
        if self.get_player_account_balance(name) > real_estate.get_cost():
            real_estate.set_owner(name)  # changes owner of the property to the player
            new_bal = self.get_player_account_balance(name) - real_estate.get_cost()
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
        target = self._players[name]
        if self.get_player_account_balance(name) == 0:
            return
        if 1 <= roll_num <= 6:  # verifies the number is on a 6 sided die
            current = target.get_position()
            new_pos = current + roll_num
            if new_pos > 25:  # when position would exceed the length of the game board
                new_pos = new_pos - 26
                account = self.get_player_account_balance(name)
                target.set_balance(account + self._go_money)
                target.set_position(new_pos)
            position = target.get_position()
            real_estate = self._game_board[position]
            if real_estate.get_owner() is not None:
                tenant = target
                tenant_bal = tenant.get_balance()
                owner = self._players[real_estate.get_owner()]
                owner_bal = owner.get_balance()
                amount = real_estate.get_rent()
                tenant.set_balance(tenant_bal - amount)
                owner.set_balance(owner_bal + amount)

                if self.get_player_account_balance(name) <= 0:  # if this is the case we will set them inactive
                    tenant.clear_properties()
                    for listing in self._game_board:  # remove tenant from owner of all properties
                        if listing.get_owner() == tenant.get_name():
                            listing.set_owner(None)

    def check_game_over(self):
        """ This method will check if the game is over by seeing is there is only one player left as active with
        more than 0 in their account balance. If this is the case then this method will return the winning player's
        name. If not then it will return an empty string. """
        names = self._players.keys()
        losers = []
        winner = []
        for name in names:
            if self.get_player_account_balance(name) <= 0:
                losers.append(name)
            if self.get_player_account_balance(name) > 0:
                winner.append(name)
        if len(winner) == 1:
            return winner[0]
        else:
            return ""


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

    def clear_properties(self):
        """ allows the change and setting of the properties a player owns """
        self._properties.clear()

    def get_position(self):
        """ returns player's position on the game board """
        return self._position

    def set_position(self, new_pos):
        """ sets the position of the player to a new value """
        self._position = new_pos


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

    def get_owner(self):
        """ returns the owner of the property """
        return self._owner

    def get_property_name(self):
        """ returns the property name """
        return self._name
