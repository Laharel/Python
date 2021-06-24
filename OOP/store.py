class store:
	def __init__(self,name,products=[]):
		self.name = name
		print(name,products)

	def add_product(self, new_product): #takes a product and adds it to the store
		pass
	def sell_product(self, id): #remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
		pass
	def inflation(self, percent_increase): # increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
		pass
	def set_clearance(self, category, percent_discount): # updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
		pass



    # def add_product(self, new_product):
    #     self.products.append(new_product)
    #     # print(self.products)

    # def sell_product(self, id):
    #     self.products.pop(id)

    # def inflation(self, percent_increase):
    #     for product in self.products:
    #         product.update_price(percent_increase, True)

    # def set_clearance(self, category, percent_discount):
    #     for product in self.products:
    #         if product.category == category:
    #             product.update_price(percent_discount, False)


jack=store("jack")


#================================================

class Store:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products
    def add_product(self, new_product):
        self.products.append(new_product)
        # print(self.products)

    def sell_product(self, id):
        self.products.pop(id)

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
    def print_info(self):
        print(self.name, self.price, self.category)


ketchup = Product("ketchup", 10, "kitchen")
mayo = Product("mayo", 10, "kitchen")
table = Product("table", 50, "living room")

panda = Store("panda")

# Test 1: add product to store 
panda.add_product(ketchup)
panda.add_product(mayo)
panda.add_product(table)
print(panda.products[0].name)

# Test 2: sell product
panda.sell_product(0)
print(len(panda.products))
# print(panda.products)

# Test 3: inflation by %10 OUTPUT: may price 11, table price 55
panda.inflation(0.10)
print(panda.products[0].name,panda.products[0].price)
print(panda.products[1].name,panda.products[1].price)

# Test 4: set_clearance to product with category = kitchen OUTPUT: mayo price 9.9
panda.set_clearance("kitchen", 0.10)#11*0.1=1.1=>11-1.1=9.9
print(panda.products[0].name,panda.products[0].price)
print(panda.products[0].print)


# Test 5: 




