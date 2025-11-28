from pydantic import BaseModel


class CreateRoomResponse(BaseModel):
    room_id: str
    password: str


class JoinRoomRequest(BaseModel):
    room_id: str
    password: str
