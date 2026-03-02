class TransactionController:
    def __init__(self, transaction_service):
        self.transaction_service = transaction_service

    def create_transaction(self, transaction_data):
        return self.transaction_service.create_transaction(transaction_data)

    def get_transaction(self, transaction_id):
        return self.transaction_service.get_transaction(transaction_id)

    def update_transaction(self, transaction_id, transaction_data):
        return self.transaction_service.update_transaction(transaction_id, transaction_data)

    def delete_transaction(self, transaction_id):
        return self.transaction_service.delete_transaction(transaction_id)