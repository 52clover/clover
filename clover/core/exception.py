"""
# clover视图异常装饰器，当捕获视图异常时将返回状态码500和异常信息。
# author ：taoyanli0808
# date   ：2020年8月6日22:03:10
# version：1.0.0
"""

from functools import wraps

from flask import jsonify
from flask import make_response

from sqlalchemy.exc import SQLAlchemyError as _SQLAlchemyError
from requests.exceptions import RequestException as _RequestException

from clover.exts import db


class CloverException(Exception):

    def __init__(self):
        self.status = 100
        self.message = "Clover平台内部错误！"


class DatabaseException(_SQLAlchemyError):

    def __init__(self):
        self.status = 200
        self.message = "数据库错误，请联系管理员！"


class RequestException(_RequestException):

    def __init__(self):
        self.status = 300
        self.message = "被测试的接口HTTP(S)请求出错误！"


class ResponseException(CloverException):

    def __init__(self):
        self.status = 400
        self.message = "被测试的接口返回错误的响应！"


class KeywordException(CloverException):

    def __init__(self):
        self.status = 500
        self.message = "平台执行关键字发生错误！"


def catch_exception(cls=CloverException):
    """
    # 捕获异常的装饰器，传入需要捕获的异常类型。
    #
    :param cls: 异常类型
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


def catch_view_exception(func):
    """
    # 捕获视图异常的装饰器
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            response = make_response(
                jsonify({
                    'status': 500,
                    'message': str(error),
                    'data': {
                        'function': func.__name__
                    }
                }), 500
            )
            return response
    return wrapper


def catch_database_exception(func):
    """
    # 捕获数据库异常的装饰器
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except _SQLAlchemyError:
            db.rollback()
            return DatabaseException()
    return wrapper


if __name__ == '__main__':
    e = CloverException()
    print(e.__dict__)
