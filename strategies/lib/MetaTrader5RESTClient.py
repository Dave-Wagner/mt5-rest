import requests
import json


class MetaTrader5RESTClient:
    def __init__(self, host, port, api_key):
        self.base_url = f"http://{host}:{port}"
        self.headers = {"Authorization": api_key}

    def _request(self, method, endpoint, **kwargs):
        response = requests.request(
            method, f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)
        response.raise_for_status()  # Raises a HTTPError if the response status is 4xx, 5xx
        return response.json()

    def get_account_info(self):
        return self._request("GET", "/info")

    def get_account_balance(self):
        return self._request("GET", "/balance")

    def get_symbol_info(self, name):
        return self._request("GET", f"/symbols/{name}")

    def get_account_orders(self):
        return self._request("GET", "/orders")

    def get_account_order(self, id):
        return self._request("GET", f"/orders/{id}")

    def get_account_orders_history(self):
        return self._request("GET", "/history")

    def get_account_order_history(self, id):
        return self._request("GET", f"/history/{id}")

    def get_account_deals(self, offset, limit):
        return self._request("GET", f"/deals?offset={offset}&limit={limit}")

    def get_account_deal(self, id):
        return self._request("GET", f"/deals/{id}")

    def get_account_positions(self):
        return self._request("GET", "/positions")

    def get_account_position(self, id):
        return self._request("GET", f"/positions/{id}")

    def send_order(self, order):
        return self._request("POST", "/trade", data=json.dumps(order))
