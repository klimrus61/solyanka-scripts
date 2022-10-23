class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.count_customer = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count_customer += 1
        total = 0
        if self.count_customer % self.n == 0:
            for i, prod in enumerate(product):
                idx = self.products.index(prod)
                total += self.prices[idx] * amount[i]
            total = total * ((100 - self.discount) / 100)
            self.count_customer = 0
        else:
            for i, prod in enumerate(product):
                idx = self.products.index(prod)
                total += self.prices[idx] * amount[i]
        return total
            

class Cashier1:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n, self.i, self.d = n, 0, discount
        self.price = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        bill = sum(self.price[p] * a for p, a in zip(product, amount))
        return bill if self.i % self.n != 0 else bill * (1 - self.d / 100)
            
        