from typing import Optional
from pydantic import BaseModel


class IPCheck(BaseModel):
    first_ip: Optional[int] = 0
    last_ip:Optional[int] = 255

    class Config:
        schema_extra = {
            "example": {
                "first_ip": 123,
                "last_ip": 200
            }
        }

class IPCheckResponse(BaseModel):
    msg:str
    ip_adress:dict

    class Config:
        schema_extra = {
            "example": {
                "msg": "Checked IP",
                "ip_adress": {
                    "127.0.0.1":True,
                    "127.0.0.2": False
                }
            }
        }

class SystemCheckResponse(BaseModel):
    msg:str

    class Config:
        schema_extra = {
            "example": {
                "msg": "Server is running"
            }
        }