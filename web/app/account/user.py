class User():
    def __init__(self, user_id, active=True):
        self.user_id = user_id
        self.active = active

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id
