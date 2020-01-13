
import traceback

from flask import request
from flask import jsonify

from clover.environment.service import TeamService
from clover.environment.service import KeywordService
from clover.environment.service import VariableService
from clover.views import CloverView


class TeamView(CloverView):

    def __init__(self):
        super(TeamView, self).__init__()
        self.service = TeamService()

    def create(self):
        """
        :return:
        """
        data = request.get_json()

        if 'team' not in data or not data['team']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter team[{0}]".format(data['team']),
                'data': data
            })

        if 'project' not in data or not data['project']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter project[{0}]".format(data['project']),
                'data': data
            })

        if 'owner' not in data or not data['owner']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter owner[{0}]".format(data['owner']),
                'data': data
            })

        try:
            id = self.service.create(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def delete(self):
        """
        :return:
        """
        data = request.get_json()

        if 'id' not in data or not data['id']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter id[{0}]".format(data['id']),
                'data': data
            })

        try:
            id = self.service.detele(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def update(self):
        """
        :return:
        """
        data = request.get_json()

        if 'id' not in data or not data['id']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter id[{0}]".format(data['id']),
                'data': data
            })

        try:
            id = self.service.update(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def search(self):
        """
        :return:
        """
        data = request.values.to_dict()

        try:
            total, result = self.service.search(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': result,
                'total': total,
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def aggregate(self):
        """
        :return:
        """
        data = request.get_json()

        try:
            data = self.service.aggregate(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': data
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })


class VariableView(CloverView):

    def __init__(self):
        super(VariableView, self).__init__()
        self.service = VariableService()

    def create(self):
        """
        :return:
        """
        data = request.get_json()

        if 'team' not in data or not data['team']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter team[{0}]".format(data['team']),
                'data': data
            })

        if 'project' not in data or not data['project']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter project[{0}]".format(data['project']),
                'data': data
            })

        if 'owner' not in data or not data['owner']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter owner[{0}]".format(data['owner']),
                'data': data
            })

        try:
            id = self.service.create(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def delete(self):
        """
        :return:
        """
        data = request.get_json()

        if 'id' not in data or not data['id']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter id[{0}]".format(data['id']),
                'data': data
            })

        try:
            id = self.service.detele(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def update(self):
        """
        :return:
        """
        data = request.get_json()

        if 'id' not in data or not data['id']:
            return jsonify({
                'status': 400,
                'message': "invalid parameter id[{0}]".format(data['id']),
                'data': data
            })

        try:
            id = self.service.update(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def search(self):
        """
        :return:
        """
        data = request.values.to_dict()

        try:
            total, result = self.service.search(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': result,
                'total': total,
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })


class KeywordView(CloverView):

    def __init__(self):
        super(KeywordView, self).__init__()
        self.service = KeywordService()

    def create(self):
        """
        :return:
        """
        data = request.get_json()

        if 'name' not in data or not data['name']:
            return jsonify({
                'status': 400,
                'message': '关键字需要定义名称!',
                'data': data
            })

        if 'snippet' not in data or not data['snippet']:
            return jsonify({
                'status': 400,
                'message': '关键字缺少实现代码!',
                'data': data
            })

        if 'mock' not in data or not data['mock']:
            return jsonify({
                'status': 400,
                'message': '关键字缺少必要的测试数据!',
                'data': data
            })

        try:
            result = self.service.create(data)
            return jsonify({
                'status': 0,
                'message': "创建关键字成功！",
                'data': result
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'data': data
            })

    def delete(self):
        """
        :return:
        """
        data = request.get_json()

        if 'id' not in data or not data['id']:
            return jsonify({
                'status': 400,
                'message': "删除关键字时缺少必要的ID",
                'data': data
            })

        try:
            id = self.service.delete(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def update(self):
        """
        :return:
        """
        data = request.get_json()

        if 'id' not in data or not data['id']:
            return jsonify({
                'status': 400,
                'message': "更新关键字时缺少必要的ID",
                'data': data
            })

        try:
            id = self.service.update(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': id
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def search(self):
        """
        :return:
        """
        data = request.values.to_dict()

        try:
            total, result = self.service.search(data)
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': result,
                'total': total,
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'traceback': traceback.format_stack(),
                'data': data
            })

    def debug(self):
        """
        :return:
        """
        data = request.get_json()

        if 'name' not in data or not data['name']:
            return jsonify({
                'status': 400,
                'message': '关键字需要定义名称!',
                'data': data
            })

        if 'snippet' not in data or not data['snippet']:
            return jsonify({
                'status': 400,
                'message': '关键字缺少实现代码!',
                'data': data
            })

        if 'mock' not in data or not data['mock']:
            return jsonify({
                'status': 400,
                'message': '关键字缺少必要的测试数据!',
                'data': data
            })

        try:
            result = self.service.debug(data)
            return jsonify({
                'status': 0,
                'message': "创建关键字成功！",
                'data': result
            })
        except Exception as error:
            return jsonify({
                'status': 500,
                'message': str(error),
                'data': data
            })
