class history_service:
    def __init__(self, history_repository):
        self.history_repository = history_repository

    def get_history_by_user_id(self, user_id):
        return self.history_repository.get_history_by_user_id(user_id)