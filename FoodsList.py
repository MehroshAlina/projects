from itertools import product
import uuid

class FoodsList():

    _list = []

    def __init__(self):

        self._list = self.getAllItems()

    def getAllItems(self):
        return {
            1: {
                'FoodID': 1,
                'Name': 'Tandoori Chicken',
                'Quantity': '4 pieces',
                'Price': 240,
                'Discount': 0,
                'Stock': 1000
            },
            2: {
                'FoodID': 2,
                'Name': 'Vegan Burger',
                'Quantity': '1 pieces',
                'Price': 320,
                'Discount': 0,
                'Stock': 1000
            },
            3: {
                'FoodID': 3,
                'Name': 'Truffle Cake',
                'Quantity': '500gm',
                'Price': 900,
                'Discount': 0,
                'Stock': 1000
            }
        }


    def generateID(self):
        return uuid.uuid1().int


    def getFoodItem(self,FoodID=''):

        if FoodID == '':
            return;

        return self._list.get(FoodID)
