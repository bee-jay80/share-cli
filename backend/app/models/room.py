class Room:
    """
    Represents a temporary file-sharing room.
    """
    def __init__(self, room_id: str, password: str, zip_path: str):
        self.room_id = room_id
        self.password = password
        self.zip_path = zip_path
