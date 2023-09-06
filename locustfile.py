from locust import HttpUser, task, run_single_user
import requests

class Hello(HttpUser):
    host = "https://httpbin.org"

    @task(1)
    def hello_get(self):
        self.client.get("/get")