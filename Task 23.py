class User:
    def __init__(self, userName: str, email: str, role: str):
        self.username = userName
        self.email = email
        self.role = role
        
    def get_info(self):
        return self.username, self.email
    
class UserAccount(User):
    def __init__(self, userName: str, email: str, role: str, password: str):
        super().__init__(userName, email, role)
        self.__password = password
        self.failed_attempts = 0
    
    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return password == self.__password

    def reset_password(self, new_password):
        if self.role == "admin":
            self.__password = new_password
    
    def increase_failed_attempts(self):
        self.failed_attempts += 1
        if (self.failed_attempts >= 3):
            self.role = "blocked"
