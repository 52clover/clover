
from functools import wraps

from flask import jsonify
from flask import make_response

from sqlalchemy.exc import SQLAlchemyError as _SQLAlchemyError
from requests.exceptions import RequestException as _RequestException


class CloverException(Exception):

    def __init__(self):
        self.status = 100
        self.message = "Cloverƽ̨�ڲ�����"


class DatabaseException(_SQLAlchemyError):

    def __init__(self):
        self.status = 200
        self.message = "���ݿ��������ϵ����Ա��"


class RequestException(_RequestException):

    def __init__(self):
        self.status = 300
        self.message = "�����ԵĽӿ�HTTP(S)���������"


class ResponseException(CloverException):

    def __init__(self):
        self.status = 400
        self.message = "�����ԵĽӿڷ��ش������Ӧ��"


class KeywordException(CloverException):

    def __init__(self):
        self.status = 500
        self.message = "ƽִ̨�йؼ��ַ�������"


def catch_exception(cls=CloverException):
    """
    # �����쳣��װ������������Ҫ������쳣���͡�
    #
    :param cls: �쳣����
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except cls as error:
                print(cls)
                response = make_response(
                    jsonify(error.__dict__), 500
                )
                return response
        return wrapper
    return decorator


if __name__ == '__main__':
    e = CloverException()
    print(e.__dict__)
