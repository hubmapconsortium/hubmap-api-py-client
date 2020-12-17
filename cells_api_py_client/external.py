from cells_api_py_client.internal import InternalClient


class Client():
    def __init__(self, base_url):
        self.client = InternalClient(base_url)
