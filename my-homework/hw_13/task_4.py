class Phone:
    def __init__(self, model: str, number: str):
        self.model = model
        self.number = number

class CallPhone(Phone):
    def call(self, other_number: str) -> None:
        print("This phone does calls.")

class MessagePhone(Phone):
    def send_message(self, other_number: str, text: str) -> None:
        print("This phone sends messages.")

class PhotoPhone(Phone):
    def take_photo(self) -> None:
        print("This phone takes pictures.")
class GamePhone(Phone):
    def play_game(self, game: str) -> None:
        print("This phone has games to play on it.")

class BasicPhone(CallPhone, MessagePhone):
    def call(self, other_number: str) -> None:
        print(f"Calling {other_number} from {self.number}")

    def send_message(self, other_number: str, text: str) -> None:
        print(f"Sending '{text}' to {other_number} from {self.number}")

class CameraPhone(BasicPhone, PhotoPhone):
    def take_photo(self) -> None:
        print(f"Taking a photo with {self.model}")

class SmartPhone(CameraPhone, GamePhone):
    def play_game(self, game: str) -> None:
        print(f"Playing {game} on {self.model}")

if __name__ == "__main__":
    smart_phone = SmartPhone('iPhone', '+1234567890')
    print(smart_phone.call('+0987654321'))
    print(smart_phone.send_message('+0987654321', 'call me back'))
    print(smart_phone.take_photo())
    print(smart_phone.play_game('chess.com'))