#create a clothing item class and a cart class 
#give the user a menu full of clothes and let them chose whether they want to browse all, shirts, pants, dresses, etc
#a bunch of these have to be already made classes
#for cart class make a checkout method
#checkout method includes total price(tax included and shipping included), choice to type in discount code, free shipping over a certain price
#put certain clothes in certain categories(shirts in shirts, pants in pants, dresses in dresses, etc)
#for cart make an add clothes in the cart
#for cart class create a method returning the total price(including tax and shipping if applicable)
#include one setter for clothing class which is size because we need the user to enter their size
#Clothing str includes name of outfit
import time#import module
class Item:#this is the class for a clothing item
    def __init__(self, name, clothing, color, price):#this parameter must include name of outfit, type of outfitcolor, price, size, quantity#we'll make a size and quantity setters
        self.name = name#initialize name
        self.clothing = clothing#initialize clothing
        self.color = color#initialize color
        self.price = price#initialize price
        self.size = "default"#initialze a default size
        self.quantity = 1#initialize default size
    #create setters
    def set_size(self, size):#setter for size so user can choose their sizes
        self.size = size#set the user input to the object's size
    def set_quant(self, quantity):#setter for quantity so the user can enter the number of clothes they want
        self.quantity = quantity#set the user input to the object's quantity
        self.price = self.price * quantity#multiply the quantity by the price to give the total price of the item
    #create getters
    def get_name(self):#return the name of the object 
        return self.name#return a string
    def get_clothing(self):#return the type of clothing
        return self.clothing#return a string 
    def get_color(self):#return the color
        return self.color#return a string
    def get_price(self):#return the price of the object
        return self.price#return a float
    def get_size(self):#return the size of the object
        return self.size#return a string
    def get_quant(self):#return the amount of objects
        return self.quantity#return integer
    #str is to display for the menu
    def __str__(self):#str to print out the label of the object
        return self.name.title() + ", " + self.color.title() + " - $" + str(self.price)#title capitalizes every first letter of a word
    #item_info is to show how much 
    def item_info(self):#this is to print out when the user is checking out their item(s)
        print("%s, %s - $%.2f\nSize:%s, Quantity:%d, Type:%s" % (self.name.title(), self.color.title(), self.price, self.size, self.quantity, self.clothing.title()))
        #title capitalizes every first letter of a word
        print()#space


class Cart:
    def __init__(self):#create constructor with no parameters
        self.bag = []#empty list is our shopping bag 
        self.wishlist = []#empty list for the wishlist
    def addtobag(self, outfit):#a method to add the item to their shopping bag
        self.bag.append(outfit)#use list method append to put the outfit parameter in the list
    def delete(self, outfit):#a method to delete the outfit from the list
        self.bag.remove(outfit)#use list method to remove the element from list
    def show_bag(self):#when the user asks to see their shopping cart
        print("Your bag:")
        print()
        if len(self.bag) == 0:
            print("Your bag is empty.")
        else:
            for i in self.bag:#the elements in the cart
                i.item_info()#print the information of the item
    def addtowish(self, outfit):#a method to add the item to their wishlist
        self.wishlist.append(outfit)#use list method append to put the element in the list
    def show_wish(self):#when the user asks to see their wishlist
        print("Your wishlist:")
        print()
        if len(self.wishlist) == 0:
            print("Your wishlist is empty.")
        else:
            for i in self.wishlist:#the elements in wishlist
                print(i)#print the elements str
    def checkout(self):#clear the checkout and give the user their total price including tax and shipping if over 45
        self.total = 0#initialize the total 
        print("Your cart:")
        print()
        for i in self.bag:#the elements of a cart
            i.item_info()#print item info first so the user can see their whole cart before purchasing
            self.total += i.get_price()#add the price of the item to your total
        if self.total == 0:
            print("Your bag is empty. Add an item to it!")
        elif self.total < 45:#if the total is more than $45
            print("Subtotal:    $%.2f" % (self.total))
            print("Tax:         $%.2f" % (self.total * 0.04))#Georgia sales tax is 4%
            print("Shipping:    $3.99")
            print("__________________")
            print("Grand total: $%.2f" % ((self.total * 1.04) + 5.99))#including subtotal, tax, and shipping
        else:
            print("Subtotal:    $%.2f" % (self.total))
            print("Tax:         $%.2f" % (self.total * 0.04))#Georgia sales tax is 4%   
            print("Shipping:    Free!")
            print("__________________")
            print("Grand total: $%.2f" % (self.total * 1.04))#including only subtotal and tax
        print()#space
        self.total = 0#set total to 0 for an empty bag
    def clear_bag(self):#method for the user to clear their whole bag or clear after checking out
        self.bag.clear()#list method to clear a list
            
#------------------------------------------------------------------------------------------------------------------
def menu(inventory):
    
    
    for row in range(len(inventory)):
        print("%d. %s" % (row + 1, inventory[row]))
    print()
        
def main():
    #create a list of all the clothes available on the site
    in_stock = []#list of all the clothes in stock and available on the website#nested list for each label
    blue_shirt = Item("Crop top", "shirts", "blue", 7.99)
    in_stock.append(blue_shirt)#add to list
    jeans = Item("Light blue jeans", "pants", "blue", 13.99)
    in_stock.append(jeans)#add to list
    pink_skirt = Item("Pinky skirts", "skirts", "pink", 8.99)
    in_stock.append(pink_skirt)#add to list
    white_shorts = Item("Classy shorts", "shorts", "white", 11.99)
    in_stock.append(white_shorts)#add to list
    brown_jacket = Item("Leather jacket", "jackets", "brown", 19.99)
    in_stock.append(brown_jacket)#add to list
    black_dress = Item("Little black dress", "dresses", "black", 9.99)
    in_stock.append(black_dress)#add to list
    yellow_dress = Item("Sunflower dress", "dresses", "yellow", 10.99)
    in_stock.append(yellow_dress)#add to list
    peach_blouse = Item("Peachy blouse", "shirt", "peach", 14.99)
    in_stock.append(peach_blouse)
    
    cart = Cart()#create shopping cart   
    print("Welcome to the Python Clothing Store! Shipping is free with a purchase over $45.")#title
    print()#space
    print("1.Show items in stock")
    print("2.Add items to bag")
    print("3.Show bag")
    print("4.Add item to wishlist")
    print("5.Show your wishlist")
    print("6.Check out")
    print("7.Clear bag")
    print("8.Quit")
    print()#space
    choice = int(input("Enter your option: "))
    while choice != 8:
        if choice == 1:
            menu(in_stock)#show user the clothes in stock
        if choice == 2:
            menu(in_stock)#display items for user to see
            num = int(input("Please choose an item: "))
            actual_size = input("Pick a size = XS, S, M, L, XL, 2XL, 3XL: ")
            actual_size = actual_size.upper()
            in_stock[num-1].set_size(actual_size)            
            cart.addtobag(in_stock[num - 1])#change it to the index
        if choice == 3:
            cart.show_bag()#call playlist method
        if choice == 4:
            menu(in_stock)#display items for the user to see
            num_again = int(input("Please choose an item:"))
            cart.addtowish(in_stock[num - 1])#change it to the index and add
        if choice == 5:
            cart.show_wish()#show wishlist method
        if choice == 6:
            cart.checkout()#checkout method
            break#program ends once user checks out
        if choice == 7:
            cart.clear_bag()
        time.sleep(1)#so it all doesn't print at once
        print()
        print("1.Show items in stock")
        print("2.Add items to bag")
        print("3.Show bag")
        print("4.Add item to wishlist")
        print("5.Show your wishlist")
        print("6.Check out")
        print("7.Clear bag")
        print("8.Quit")        
        print()#space
        choice = int(input("Enter your option:"))       

main()



