import functools

from fastapi import HTTPException
from sqlalchemy import exc


def no_result_found_handler():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args):
            try:
                return await func(*args)
            except exc.NoResultFound:
                raise HTTPException(status_code=404, detail="No such element!")
        return wrapped
    return wrapper
