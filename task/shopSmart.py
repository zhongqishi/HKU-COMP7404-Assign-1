"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """    
    "*** YOUR CODE HERE ***"
    shopDict={};
    for thisShop in fruitShops:
      shopDict[thisShop] = thisShop.getPriceOfOrder(orderList);

    resultShop = fruitShops[0];

    for thisShop in fruitShops:
      if (shopDict[thisShop]<=shopDict[resultShop]):
        resultShop=thisShop;

    return resultShop;
    
def shopArbitrage(orderList, fruitShops):
    """
    input: 
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    output:
        maximum profit in amount
    """
    result = 0.0;
    for fruit in orderList:
      maxprice=0;
      minprice=9999999999999999;
      for thisShop in fruitShops:
        if(maxprice<=thisShop.getCostPerPound(fruit[0])):
          maxprice=thisShop.getCostPerPound(fruit[0]);
        if(minprice>=thisShop.getCostPerPound(fruit[0])):
          minprice=thisShop.getCostPerPound(fruit[0]);
      result += (maxprice-minprice)*fruit[1];

    return result;

def shopMinimum(orderList, fruitShops):
    """
    input: 
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    output:
        Minimun cost of buying the fruits in orderList
    """
    result = 0.0;
    for fruit in orderList:
     
      minprice=9999999999999999;
      for thisShop in fruitShops:
        if(minprice>=thisShop.getCostPerPound(fruit[0])):
          minprice=thisShop.getCostPerPound(fruit[0]);
      result += minprice*fruit[1];

    return result;

if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
  orders = [('apples',3.0)]
  print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
