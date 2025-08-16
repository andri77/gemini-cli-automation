from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)  # Simulate user thinking time between tasks

    @task(3)  # Higher weight means this task will be executed more often
    def get_all_products(self):
        self.client.get("/products", name="Get All Products")

    @task(1) # Lower weight
    def get_single_product(self):
        product_id = random.randint(1, 20)  # Assuming there are at least 20 products
        self.client.get(f"/products/{product_id}", name="Get Single Product")

    @task(1)
    def add_new_product(self):
        new_product_data = {
            "title": "test product",
            "price": 13.5,
            "description": "lorem ipsum dolor sit amet",
            "image": "https://i.pravatar.cc",
            "category": "electronic",
        }
        self.client.post("/products", json=new_product_data, name="Add New Product")

    # You can add more tasks for update, delete, etc., if needed

    def on_start(self):
        # This method is called when a Locust user starts
        # You can use it for login, setup, etc.
        pass
