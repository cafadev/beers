class OrderNotFound(Exception):
    def __init__(self, order_id):
        super().__init__(f"Order with id {order_id} not found")