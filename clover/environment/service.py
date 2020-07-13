import re
import json
import datetime

from clover.exts import db
from clover.core.keyword import Keyword
from clover.models import query_to_dict, soft_delete
from clover.environment.models import TeamModel
from clover.environment.models import KeywordModel
from clover.environment.models import VariableModel


class TeamService(object):

    def create(self, data):
        """
        :param data:
        :return:
        """
        model = TeamModel(**data)
        db.session.add(model)
        db.session.commit()

    def detele(self, data):
        """
        :param data:
        :return:
        """
        model = TeamModel.query.get(data['id'])
        if model is not None:
            soft_delete(model)

    def update(self, data):
        """
        # 使用id作为条件，更新数据库重的数据记录。
        # 通过id查不到数据时增作为一条新的记录存入。
        :param data:
        :return:
        """
        old_model = TeamModel.query.get(data['id'])
        if old_model is None:
            model = TeamModel(**data)
            db.session.add(model)
            db.session.commit()
        else:
            {setattr(old_model, k, v) for k, v in data.items()}
            old_model.updated = datetime.datetime.now()
            db.session.commit()

    def search(self, data):
        """
        type=team&team=team1
        limit=10&skip=0&type=team
        NOTE: 有两种传参查询方式，需要多data做相应处理
        :param data:
        :return:
        """
        filter = {'enable': 0}

        if 'team' in data and data['team']:
            filter.setdefault('team', data.get('team'))

        if 'owner' in data and data['owner']:
            filter.setdefault('owner', data.get('owner'))

        try:
            offset = int(data.get('offset', 0))
        except TypeError:
            offset = 0

        try:
            limit = int(data.get('limit', 10))
        except TypeError:
            limit = 10

        results = TeamModel.query.filter_by(
            **filter
        ).order_by(
            TeamModel.created.desc()
        ).offset(offset).limit(limit)
        results = query_to_dict(results)
        count = TeamModel.query.filter_by(**filter).count()
        return count, results

    def aggregate(self, data):
        """
        {'type': 'team', 'key': 'team'}
        {'type': 'team', 'key': 'owner'}
        # cascader: 按照element ui库cascader需要的数据格式返回数据。
        #           团队和项目配置数据不会特别多，因此无需过多关注性能。
        :param data:
        :return: 所有数据
        """
        if 'cascader' in data:
            cascader = {}
            results = TeamModel.query. \
                with_entities(TeamModel.team, TeamModel.project). \
                filter(TeamModel.enable == 0). \
                distinct().all()
            for team, project in results:
                if team not in cascader:
                    cascader.setdefault(team, {
                        'label': team,
                        'value': team,
                        'children': [{
                            'label': project,
                            'value': project
                        }],
                    })
                else:
                    labels = [item['label'] for item in cascader[team]['children']]
                    if project not in labels:
                        cascader[team]['children'].append({
                            'label': project,
                            'value': project
                        })
            return list(cascader.values())
        else:
            if data['key'] == 'team':
                results = TeamModel.query.with_entities(TeamModel.team). \
                    filter(TeamModel.enable == 0). \
                    distinct().all()
                return [r[0] for r in results]
            elif data['key'] == 'owner':
                results = TeamModel.query.with_entities(TeamModel.owner). \
                    filter(TeamModel.enable == 0). \
                    distinct().all()
                return [r[0] for r in results]
            else:
                return []

    def navigation(self, data):
        """
        {
            $team: [$project...],
            $team: [$project...]
        }
        :param data:
        :return: 所有数据
        """
        results = TeamModel.query.filter(TeamModel.enable == 0)

        options = {}
        for result in results:
            if result.team not in options:
                options.setdefault(result.team, [result.project])
            else:
                options[result.team].append(result.project)

        return options


class VariableService(object):

    def create(self, data):
        """
        :param data:
        :return:
        """
        # 查询数据库name值，存在已有变量就返回变量名存在
        filter = {
            "enable": 0,
            "name": data["name"],
            "project": data["project"]
        }
        count = VariableModel.query.filter_by(**filter).count()
        if not count:
            model = VariableModel(**data)
            db.session.add(model)
            db.session.commit()
        return count

    def detele(self, data):
        """
        :param data:
        :return:
        """
        model = VariableModel.query.get(data['id'])
        if model is not None:
            soft_delete(model)

    def update(self, data):
        """
        # 使用id作为条件，更新数据库重的数据记录。
        # 通过id查不到数据时增作为一条新的记录存入。
        :param data:
        :return:
        """
        status = 0
        filter = {"name": data["name"], "project": data["project"], "enable": 0}
        count = VariableModel.query.filter_by(**filter).count()
        if count >= 1:
            status = 1
            return status
        else:
            old_model = VariableModel.query.get(data['id'])
            if old_model is None:
                model = VariableModel(**data)
                db.session.add(model)
                db.session.commit()
            else:
                {setattr(old_model, k, v) for k, v in data.items()}
                old_model.updated = datetime.datetime.now()
                db.session.commit()
            return status

    def search(self, data):
        """
        type=team&team=team1
        limit=10&skip=0&type=team
        NOTE: 有两种传参查询方式，需要多data做相应处理
        :param data:
        :return:
        """
        filter = {'enable': 0}

        if 'team' in data and data['team']:
            filter.setdefault('team', data.get('team'))

        if 'owner' in data and data['owner']:
            filter.setdefault('owner', data.get('owner'))

        try:
            offset = int(data.get('offset', 0))
        except TypeError:
            offset = 0

        try:
            limit = int(data.get('limit', 10))
        except TypeError:
            limit = 10

        results = VariableModel.query.filter_by(
            **filter
        ).order_by(
            VariableModel.created.desc()
        ).offset(offset).limit(limit)
        results = query_to_dict(results)
        count = VariableModel.query.filter_by(**filter).count()
        return count, results


class KeywordService(object):

    def create(self, data):
        """
        # 暂时没有前端页面 -- SQL暂时不更换
        # 这里需要先提取函数名，然后关键字用函数名进行索引，存到数据库。
        # 如果数据库中函数名已经存在怎么办，是否需要先查询，重复则失败？
        :param data:
        :return:
        """
        keyword = data.get('keyword')
        description = data.get('description')

        # 执行关键字提取函数名称
        _keyword = Keyword(keyword)
        function_name = _keyword.get_function_name_from_source()

        data = {
            'name': function_name,
            'description': description,
            'keyword': keyword
        }

        model = KeywordModel(**data)
        db.session.add(model)
        db.session.commit()
        return model.id

    def delete(self, data):
        """
        :param data:
        :return:
        """
        id = data.get('id')
        model = KeywordModel.query.get(id)
        if model is not None:
            soft_delete(model)

    def update(self, data):
        """
        :param data:
        :return:
        """
        id = data.get('id')
        old_model = KeywordModel.query.get(id)
        if old_model is None:
            model = TeamModel(**data)
            db.session.add(model)
            db.session.commit()
        else:
            {setattr(old_model, k, v) for k, v in data.items()}
            old_model.updated = datetime.datetime.now()
            db.session.commit()

    def search(self, data):
        """
        :param data:
        :return:
        """
        filter = {'enable': 0}

        # 如果按照id查询则返回唯一的数据或None
        if 'id' in data and data['id']:
            filter.setdefault('id', data.get('id'))
            result = KeywordModel.query.get(data['id'])
            count = 1 if result else 0
            result = result.to_dict() if result else None
            return count, result

        try:
            offset = int(data.get('offset', 0))
        except TypeError:
            offset = 0

        try:
            limit = int(data.get('limit', 10))
        except TypeError:
            limit = 10

        results = KeywordModel.query.filter_by(**filter) \
            .offset(offset).limit(limit)
        results = query_to_dict(results)
        count = KeywordModel.query.filter_by(**filter).count()
        return count, results

    def debug(self, data):
        """
        # 自定义关键字中提取函数名和参数，在后面拼接出调用请求，
        # 最后交给exec函数执行，如果提取函数名和参数失败则不处理。
        :param data:
        :return:
        """
        keyword = data.get('keyword')
        expression = data.get('expression')
        _keyword = Keyword(keyword)
        _keyword.is_keyword(expression)
        result = _keyword.execute()
        return result