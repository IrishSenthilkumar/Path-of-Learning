'''
Created on 12 Sep 2018

@author: Irish
'''

import random

class ShoppingCart:    # '_' means make private
    _itemList = []
    totalPrice = 0
    
    def __init__(self, customerID):
        self._cartID = random.randint(1, 100)
        self._customerID = customerID
    
    def getCartID(self):
        return self.cartID    # Remember to include self. when returning class variables
    
    def getCustomerID(self):
        return self.getCustomerID
    
    def getItems(self):
        return self.itemList
    
    def addItem(self, Item):
        self.itemList.append(_Item)
    
    def getTotalPrice(self):
        return self.totalPrice
       
    def printItems(self):
        items = []
        for x in self.itemList:
            items.append(x.getName())
        
        print(items)
    
    def confirmCart(self):
        for x in self.itemList:
            self.totalPrice = self.totalPrice + x.getPrice()
    
    
class Customer:
    
    def __init__(self, firstName, lastName, address):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.customerID = random.randint(1, 1000000)
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getAddress(self):
        return self.address
    
    def getID(self):
        return self.customerID


class Item:
    def __init__(self, itemNumber, price, name):
        self.itemNumber = itemNumber
        self.price = price
        self.name = name
    
    def getItemNumber(self):
        return self.itemNumber
    
    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name


class Cpu(Item):    # like 'Cpu extends Item'
    itemNumber = 1
    price = 200
    name = "cpu"
    
    def __init__(self):
        Item.__init__(self, self.itemNumber, self.price, self.name)


class MotherBoard(Item):
    itemNumber = 2
    price = 150
    name = "motherboard"
    
    def __init__(self):
        Item.__init__(self, self.itemNumber, self.price, self.name)
        

class Invoice:
    def __init__(self, Customer, ShoppingCart):
        self.customer = Customer
        self.cart = ShoppingCart
    
    def printInvoice(self):
        print("___________THIS IS AN AUTOMATED EMAIL, PLEASE DO NOT REPLY_________", end="\n\n")
        print("Hello ", self.customer.getFirstName(), ", ")
        print("\t Thank you for shopping at randomOnlineShop.com! \n\t Your invoice is below:")
        
        for x in self.cart.itemList:
            print("\t", x.getName(), "\t$", x.getPrice())
        
        print("\t Your total purchase amounts to : $", self.cart.getTotalPrice(), end="\n\n")
        print("Regards, \n ShoppingTeam")
def main():
    person = Customer("Irish", "Senthilkumar", "Ireland")
    cart = ShoppingCart(person.getID())
    cpu = Cpu()
    mb = MotherBoard()
    
    cart.addItem(cpu)
    cart.addItem(mb)
    cart.confirmCart()
    
    invoice = Invoice(person, cart)
    invoice.printInvoice()
    

if __name__ == "__main__":
    main()



        
        
    
    
    
    
       
        
    
        
