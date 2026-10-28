class Order:
    def __init__(self, order_id: str, total_price: float):
        self.order_id = order_id
        self.total_price = total_price
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Completed"

    def summary(self) -> str:
        return f"Order #{self.order_id} | Total: ${self.total_price:.2f} | Status: {self.status}"


class Customer:
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, order: Order):
        self.orders.append(order)
        print(f"Order #{order.order_id} added to customer {self.name}.")

    def view_order_history(self):
        print(f"--- Order History for {self.name} ({self.email}) ---")
        for order in self.orders:
            print(f" - {order.summary()}")


if __name__ == "__main__":
    customer = Customer("CUST-101", "Jane Doe", "jane.doe@example.com")
    o1 = Order("ORD-5001", 129.50)
    o2 = Order("ORD-5002", 45.00)

    customer.place_order(o1)
    customer.place_order(o2)
    o1.mark_complete()
    customer.view_order_history()
