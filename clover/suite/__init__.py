#coding=utf-8

from flask import Blueprint

testsuite = Blueprint('suite', __name__)

from clover.suite import views