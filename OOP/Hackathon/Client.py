class Client:
    def __init__(self, name , payment_status=True, is_authorized = False):
        self.name = name
        self.payment_status = payment_status
        self.is_authorized = is_authorized