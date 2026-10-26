import datetime
import re

class FoodItem:
    def __init__(self, item_id, name, category, price, stock):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def __str__(self):
        return f"{str(self.item_id):<6} | {self.name:<15} | {self.category:<12} | ${self.price:<8.2f} | {self.stock:<6} |"


class RestaurantSystem:
    def __init__(self):
        # Initial mock data
        self.menu = {
            1: FoodItem(1, "Burger", "Fast Food", 8.99, 20),
            2: FoodItem(2, "Pizza", "Fast Food", 12.99, 15),
            3: FoodItem(3, "Caesar Salad", "Healthy", 6.50, 10),
            4: FoodItem(4, "Coke", "Beverages", 2.50, 50)
        }
        self.users = {
            "admin": {
                "password": "admin123", 
                "role": "admin", 
                "name": "System Admin",
                "email": "admin@restaurant.com",
                "phone": "8547124512"
            },
            "bhargavi": {
                "password": "bhargavi007", 
                "role": "customer", 
                "name": "bhargavi niharika",
                "email": "bhargavi@gmail.com",
                "phone": "9638527412"
            }
        }
        self.orders = {}
        self.order_counter = 1001
        self.current_user = None

    def main_menu(self):        
        while True:
            print("\nMain Menu\n")
            print("1. Login")
            print("2. Register Customer Account")
            print("3. Exit")
            
            main_choice = self.numeric_input_validate("\nEnter your choice: ")
            
            if main_choice == 1:
                self.login()
            elif main_choice == 2:
                self.register_customer()
            elif main_choice == 3:
                print("\nThank you for using ood Ordering and Management system")
                break
            else:
                print("\nInvalid choice Please select correct choice")

    def numeric_input_validate(self, prompt, min_value=None):
        
        while True:
            try:
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    print(f"\nValue must be at least {min_value}.")
                    continue
                return value
            except ValueError:
                print("\nPlease enter a valid integer number")

    def float_input_validate(self, prompt, min_value=None):
        
        while True:
            try:
                value = float(input(prompt))
                if min_value is not None and value <= min_value:
                    print(f"\nValue must be greater than {min_value}")
                    continue
                return value
            except ValueError:
                print("\nPlease enter a valid decimal number")

    def login(self):
        username = input("\nEnter username: ").strip().lower()
        password = input("\nEnter password: ").strip()

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            role = self.users[username]["role"]
            print(f"\nLogin successful Welcome, {self.users[username]['name']}")
            
            if role == "admin":
                self.admin_menu()
            else:
                self.customer_menu()
        else:
            print("\nInvalid username or password Please try again")

    def register_customer(self):
        print("\nCustomer Registration")
        name = input("\nEnter full name: ").strip()
        
        # Email Validation
        while True:
            email = input("\nEnter your email address: ").strip().lower()            
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                break
            print("\nInvalid email format please use correct format")

        # Phone Number Validation
        while True:
            phone = input("\nEnter phone number: ").strip()
            # Checks if phone contains only digits and is between 10 to 15 characters long
            if phone.isdigit() and len(phone) >= 10:
                break
            print("\nInvalid phone number Please enter at least 10 numeric digits")

        # Username Check
        while True:
            username = input("\nEnter username: ").strip().lower()
            if not username:
                print("\nUsername cannot be empty")
                continue
            if username in self.users:
                print("\nUsername already exists Please choose another")
                continue
            break

        # Password Validation
        while True:
            password = input("\nChoose a password (min 6 characters): ").strip()
            if len(password) >= 6:
                break
            print("\nPassword is too short It must be at least 6 characters long")

        # Storing validated details
        self.users[username] = {
            "password": password, 
            "role": "customer", 
            "name": name,
            "email": email,
            "phone": phone
        }
        print("\nRegistration successful")

    # Customer Menu
    def customer_menu(self):
        cart = {} 
        
        while True:
            print(f"\nCustomer Menu\n")
            print("1. View Food Menu")
            print("2. Search Food Items")
            print("3. Add Item to Cart")
            print("4. Remove Item from Cart")
            print("5. View Cart & Calculate Total Bill")
            print("6. Place Food Order")
            print("7. View Order History")
            print("8. Cancel Order")
            print("9. Logout")

            choice = self.numeric_input_validate("\nSelect customer option: ")

            if choice == 1:
                self.view_menu()
            elif choice == 2:
                self.search_food()
            elif choice == 3:
                self.add_to_cart(cart)
            elif choice == 4:
                self.remove_from_cart(cart)
            elif choice == 5:
                self.view_cart(cart)
            elif choice == 6:
                self.place_order(cart)
            elif choice == 7:
                self.view_order_history()
            elif choice == 8:
                self.cancel_order()
            elif choice == 9:
                self.current_user = None
                print("\nLogged out successfully")
                break
            else:
                print("\nInvalid customer choice")

    def view_menu(self):
        print("\nFood Item Details\n")
        print("\n" + "--------------------------------------------------------------")
        print(f"{'ID':<6} | {'Food Name':<15} | {'Category':<12} | {'Price':<9} | {'Stock':<6} |")
        print("--------------------------------------------------------------")
        
        if not self.menu:
            print("No items available.")
            print("--------------------------------------------------------------")
            return
            
        for item in self.menu.values():
            print(item)
            
        print("--------------------------------------------------------------")

    def search_food(self):
        keyword = input("\nEnter food name or category to search: ").strip().lower()
        print(f"\nSearch Results for '{keyword}':")
        
        print("\n" + "--------------------------------------------------------------")
        print(f"{'ID':<6} | {'Food Name':<15} | {'Category':<12} | {'Price':<9} | {'Stock':<6} |")
        print("--------------------------------------------------------------")
        
        found = False
        for item in self.menu.values():
            if keyword in item.name.lower() or keyword in item.category.lower():
                print(item)
                found = True
                
        print("--------------------------------------------------------------")
        
        if not found:            
            print("\nNo matching items found")

    def add_to_cart(self, cart):
        self.view_menu()
        item_id = self.numeric_input_validate("\nEnter Food ID to add to cart: ")
        if item_id in self.menu:
            qty = self.numeric_input_validate("\nEnter quantity: ")
            if qty > 0 and qty <= self.menu[item_id].stock:
                cart[item_id] = cart.get(item_id, 0) + qty
                print(f"\nAdded {qty} x {self.menu[item_id].name} to cart successfully")
            else:
                print("\nInvalid quantity or exceeds available stock")
        else:
            print("\nInvalid Food ID")

    def remove_from_cart(self, cart):
        if not cart:
            print("\nCart is empty")
            return
            
        print("\nCurrent Cart")
        print("------------------------------------")
        print(f"{'ID':<6} | {'Food Name':<15} | {'Quantity':<8} |")
        print("------------------------------------")
        
        for item_id, qty in cart.items():
            item = self.menu[item_id]
            print(f"{str(item_id):<6} | {item.name:<15} | {str(qty):<8} |")
            
        print("------------------------------------")
        
        item_id = self.numeric_input_validate("\nEnter Food ID to remove: ", min_value=1)
        if item_id in cart:
            del cart[item_id]
            print("\nItem removed from cart successfully")
        else:
            print("\nItem not found in your cart")

    def view_cart(self, cart):
        if not cart:
            print("\nYour cart is empty")
            return 0.0
        
        print("\nCart Details & Bill")
        total = 0.0
        for item_id, qty in cart.items():
            item = self.menu[item_id]
            cost = item.price * qty
            total = cost + total
            print(f"\n{item.name} x {qty} = ${cost:.2f}")
        print(f"\nTotal Bill Amount: ${total:.2f}")
        return total

    def place_order(self, cart):
        if not cart:
            print("\nYour cart is empty Cannot place order")
            return
        
        total = self.view_cart(cart)
        confirm = input("\nDo you want confirm your order? (y/n): ").strip().lower()
        if confirm == 'y':
            # Deduct stock
            for item_id, qty in cart.items():
                self.menu[item_id].stock -= qty

            order_id = self.order_counter
            self.orders[order_id] = {
                "customer": self.current_user,
                "items": cart.copy(),
                "total": total,
                "status": "Pending"
            }
            print(f"\nOrder placed successfully Your Order ID is {order_id}")
            cart.clear()
            self.order_counter += 1
        else:
            print("\nOrder cancelled")

    def view_order_history(self):
        print(f"\nOrder History for {self.current_user}")
        
        print("\n---------------------------------------------")
        print(f"{'Order ID':<10} | {'Total Amount':<15} | {'Status':<12} |")
        print("\n---------------------------------------------")
        
        found = False
        for order_id, info in self.orders.items():
            if info["customer"] == self.current_user:
                print(f"{str(order_id):<10} | ${info['total']:<14.2f} | {info['status']:<12} |")
                found = True
                
        print("\n---------------------------------------------")
        
        if not found:
            print("\nNo orders found")

    def cancel_order(self):
        order_id = self.numeric_input_validate("Enter Order ID to cancel: ")
        if order_id in self.orders and self.orders[order_id]["customer"] == self.current_user:
            if self.orders[order_id]["status"] == "Pending":
                # Restore stock
                for item_id, qty in self.orders[order_id]["items"].items():
                    self.menu[item_id].stock += qty
                self.orders[order_id]["status"] = "Cancelled"
                print(f"\nOrder {order_id} has been cancelled")
            else:
                print("\nOrder cannot be cancelled as it is already processed or delivered")
        else:
            print("Invalid Order ID or unauthorized")

    # Admin Menu
    def admin_menu(self):
        while True:
            print("\nAdmin Management Menu\n")
            print("1. Add Food Item")
            print("2. Display Food Details")
            print("3. Update Food Details")
            print("4. Delete Food Item")
            print("5. Display Food Categories")
            print("6. Display and Update Orders")
            print("7. Display Customer Details")
            print("8. Generate Sales Reports")
            print("9. Logout")

            admin_option = self.numeric_input_validate("\nSelect admin option: ")

            if admin_option == 1:
                self.add_food_item()
            elif admin_option == 2:
                self.view_menu()
            elif admin_option == 3:
                self.update_food_item()
            elif admin_option == 4:
                self.delete_food_item()
            elif admin_option == 5:
                self.manage_categories()
            elif admin_option == 6:
                self.view_and_update_orders()
            elif admin_option == 7:
                self.view_customer_details()
            elif admin_option == 8:
                self.generate_sales_reports()
            elif admin_option == 9:
                self.current_user = None
                print("\nLogged out successfully")
                break
            else:
                print("\nInvalid admin choice")

    def add_food_item(self):
        item_id = self.numeric_input_validate("\nEnter Food ID: ")
        if item_id in self.menu:
            print("\nFood ID already exists")
            return
        name = input("Enter food name: ").strip()
        category = input("Enter category: ").strip()
        price = self.float_input_validate("Enter price: ", min_value=0.0)
        stock = self.numeric_input_validate("Enter initial stock: ", min_value=0)

        self.menu[item_id] = FoodItem(item_id, name, category, price, stock)
        print("\nFood item added successfully")

    def update_food_item(self):
        self.view_menu()
        item_id = self.numeric_input_validate("Enter Food ID to update: ")
        if item_id in self.menu:
            item = self.menu[item_id]
            print(f"Updating: {item.name}")
            item.price = self.float_input_validate("Enter new price: ", min_value=0.0)
            item.stock = self.numeric_input_validate("Enter new stock quantity: ", min_value=0)
            print("\nFood details updated successfully")
        else:
            print("\nFood item not found")

    def delete_food_item(self):
        self.view_menu()
        item_id = self.numeric_input_validate("Enter Food ID to delete: ")
        if item_id in self.menu:
            del self.menu[item_id]
            print("\nFood item deleted successfully")
        else:
            print("\nFood item not found")

    def manage_categories(self):
        print("\nAvailable Food Categories")
        categories = set(item.category for item in self.menu.values())
        for cat in categories:
            print(f"\n* {cat}")

    def view_and_update_orders(self):
        if not self.orders:
            print("\nNo orders placed yet")
            return
            
        print("\nAll Customer Orders")
        print("-----------------------------------------------------------------")
        print(f"{'Order ID':<10} | {'Customer':<12} | {'Total Amount':<14} | {'Status':<12}")
        print("-----------------------------------------------------------------")
        
        for order_id, info in self.orders.items():
            print(f"{str(order_id):<10} | {info['customer']:<12} | ${info['total']:<13.2f} | {info['status']:<12}")
            
        print("-----------------------------------------------------------------")

        order_id = self.numeric_input_validate("\nEnter Order ID to update status: ", min_value=1)
        if order_id in self.orders:
            print("\n1. Preparing\n2. Delivered\n3. Cancelled")
            status_choice = self.numeric_input_validate("Select new status (1-3): ", min_value=1)
            status_map = {1: "Preparing", 2: "Delivered", 3: "Cancelled"}
            if status_choice in status_map:
                self.orders[order_id]["status"] = status_map[status_choice]
                print(f"\nOrder {order_id} status updated to {status_map[status_choice]}")
            else:
                print("\nInvalid status option")
        else:
            print("\nOrder ID not found")

    def view_customer_details(self):
        print("\nRegistered Customers")
        print("----------------------------------------------------------------------")
        print(f"{'Username':<12} | {'Full Name':<16} | {'Email':<20} | {'Phone':<10}  |")
        print("----------------------------------------------------------------------")
        
        found = False
        for username, info in self.users.items():
            if info["role"] == "customer":
                print(f"{username:<12} | {info['name']:<16} | {info['email']:<20} | {info['phone']:<10} |")
                found = True
                
        print("----------------------------------------------------------------------")
        
        if not found:
            print("\nNo registered customers found")

    def generate_sales_reports(self):
        print("\nSales Report")
        total_revenue = 0.0
        completed_orders = 0
        for info in self.orders.values():
            if info["status"] != "Cancelled":
                total_revenue += info["total"]
                completed_orders += 1
        print(f"Total Completed Orders: {completed_orders}")
        print(f"Total Revenue Generated: ${total_revenue:.2f}")


# Entry point
if __name__ == "__main__":
    app = RestaurantSystem()
    print("\nWelcome to Food Ordering and Management System\n")
    app.main_menu()