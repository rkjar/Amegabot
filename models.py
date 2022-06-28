from pydantic import BaseModel


class Config(BaseModel):
    email: str
    password: str
    to_email: list
    subject: str

    def __init__(self):
        super().__init__()

    def config_parser(self, textfile: str) -> dict:
        return self.parse_file(textfile).dict()