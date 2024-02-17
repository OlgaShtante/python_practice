class AuthService:
    def register(self, user: 'User') -> None:
        print(f"{user.name} registered with email address {user.email} and password {user.password}")

    def login(self, user: 'User') -> None:
        print(f"{user.name} logged in with email {user.email} and password {user.password}")

    def logout(self, user: 'User') -> None:
        print(f"{user.name} logged out")


class EmailService:
    def send_email(self, user: 'User', subject: str, message: str, recipients: list) -> None:
        print(f"{user.name} sent message {message} with {subject} {recipients}")


class ReportService:
    def generate_report(self, user: 'User', data: dict) -> None:
        print(f"{user.name} generates a report with data {data}")


class User:
    def __init__(self, name: str, email: str, password: str, role: str):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def change_password(self, new_password: str) -> None:
        print(f"Password {self.name} changed from {self.password} to {new_password}")


if __name__ == "__main__":
    user = User('Olga', 'os@gmail.com', 'Passw0rd!', 'Admin')
    auth = AuthService()
    auth.register(user)
    auth.login(user)
    auth.logout(user)
    user.change_password('Passw0rd12345!')
    email = EmailService()
    email.send_email(user, 'Greetings', 'Hello, how are you? :)', 'Dzmitry')
    report = ReportService()
    report.generate_report(user, {'topic':'class', 'sub_topic':'methods'})
