from typing import Optional

from steam.errors import STEAM_ERROR_CODES


class SteamError(Exception):

    def __init__(self, error_code: int, error_msg: Optional[str] = None):
        self.error_msg = error_msg
        self.error_code = error_code

    def __str__(self) -> str:
        return str({
            'error': STEAM_ERROR_CODES[self.error_code] if self.error_code in STEAM_ERROR_CODES else self.error_code,
            'msg': self.error_msg,
        })


class UnknownSteamError(SteamError):
    ...
