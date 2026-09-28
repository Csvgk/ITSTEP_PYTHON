class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class ProductTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def add_product(self, product):
        new_node = Node(product)
        if self.root is None:
            self.root = new_node
            self.count += 1
            return

        current = self.root
        while True:
            if product.id < current.product.id:
                if current.left is None:
                    current.left = new_node
                    self.count += 1
                    return
                current = current.left
            elif product.id > current.product.id:
                if current.right is None:
                    current.right = new_node
                    self.count += 1
                    return
                current = current.right
            else:
                print(f"Товар з id {product.id} вже існує")
                return

    def find_product(self, id):
        current = self.root
        while current is not None:
            if id == current.product.id:
                return current.product
            elif id < current.product.id:
                current = current.left
            else:
                current = current.right
        return None

    def contains(self, id):
        return self.find_product(id) is not None

    def show_products(self, node=None, first_call=True):
        if first_call:
            node = self.root
            print("Каталог товарів:")
        if node is not None:
            self.show_products(node.left, False)
            print(f"{node.product.id} — {node.product.name} — {node.product.price} грн")
            self.show_products(node.right, False)

    def find_cheapest(self, node=None, first_call=True):
        if first_call:
            node = self.root
            if node is None:
                return None
        cheapest = node.product
        if node.left is not None:
            left_cheapest = self.find_cheapest(node.left, False)
            if left_cheapest.price < cheapest.price:
                cheapest = left_cheapest
        if node.right is not None:
            right_cheapest = self.find_cheapest(node.right, False)
            if right_cheapest.price < cheapest.price:
                cheapest = right_cheapest
        return cheapest

    def find_most_expensive(self, node=None, first_call=True):
        if first_call:
            node = self.root
            if node is None:
                return None
        most_expensive = node.product
        if node.left is not None:
            left_expensive = self.find_most_expensive(node.left, False)
            if left_expensive.price > most_expensive.price:
                most_expensive = left_expensive
        if node.right is not None:
            right_expensive = self.find_most_expensive(node.right, False)
            if right_expensive.price > most_expensive.price:
                most_expensive = right_expensive
        return most_expensive

    def count_products(self):
        return self.count


catalog = ProductTree()
catalog.add_product(Product(50, "Laptop", 30000))
catalog.add_product(Product(25, "Mouse", 800))
catalog.add_product(Product(75, "Monitor", 12000))
catalog.add_product(Product(10, "Cable", 250))
catalog.add_product(Product(35, "Keyboard", 1500))
catalog.add_product(Product(60, "Headphones", 2000))

catalog.show_products()


def show_menu():
    print("\n1. Додати товар")
    print("2. Знайти товар за ID")
    print("3. Перевірити наявність товару за ID")
    print("4. Показати всі товари")
    print("5. Знайти найдешевший товар")
    print("6. Знайти найдорожчий товар")
    print("7. Кількість товарів у каталозі")
    print("0. Вихід")


while True:
    show_menu()
    choice = input("Оберіть дію: ")

    if choice == "1":
        new_id = int(input("Введіть ID товару: "))
        name = input("Введіть назву товару: ")
        price = float(input("Введіть ціну товару: "))
        catalog.add_product(Product(new_id, name, price))

    elif choice == "2":
        search_id = int(input("Введіть ID товару: "))
        found = catalog.find_product(search_id)
        if found:
            print(f"\nТовар знайдено:\n{found.name}\nЦіна: {found.price} грн")
        else:
            print("\nТовар не знайдено")

    elif choice == "3":
        search_id = int(input("Введіть ID товару: "))
        print(catalog.contains(search_id))

    elif choice == "4":
        catalog.show_products()

    elif choice == "5":
        cheapest = catalog.find_cheapest()
        if cheapest:
            print(f"Найдешевший товар: {cheapest.name} — {cheapest.price} грн")
        else:
            print("Каталог порожній")

    elif choice == "6":
        expensive = catalog.find_most_expensive()
        if expensive:
            print(f"Найдорожчий товар: {expensive.name} — {expensive.price} грн")
        else:
            print("Каталог порожній")

    elif choice == "7":
        print(f"Кількість товарів: {catalog.count_products()}")

    elif choice == "0":
        print("Вихід з програми")
        break

    else:
        print("Невірний вибір, спробуйте ще раз")