
from werkzeug.utils import import_string


class Plugin(object):

    def __init__(self):
        self.type = None

    def create(self, **kwargs):
        """
        :return:
        """
        # 使用import_string寻找模型的类型，参数为str
        if not isinstance(self.type, str):
            raise ValueError("模型名必须为字符串。")

        # 实例化服务，保存到数据库
        service = import_string(self.type)()
        return service.create(kwargs)


class TeamPlugin(Plugin):

    def __init__(self):
        super(TeamPlugin, self).__init__()
        self.type = 'clover.environment.service:TeamService'


class VariablePlugin(Plugin):

    def __init__(self):
        super(VariablePlugin, self).__init__()
        self.type = 'clover.environment.service:VariableService'


class InterfacePlugin(Plugin):

    def __init__(self):
        super(InterfacePlugin, self).__init__()
        self.type = 'clover.interface.service:InterfaceService'


class SuitePlugin(Plugin):

    def __init__(self):
        super(SuitePlugin, self).__init__()
        self.type = 'clover.suite.service:SuiteService'


class Pipeline(Plugin):

    def __init__(self):
        super(Pipeline, self).__init__()
        self.team = None
        self.project = None
        self.suite = None
        self.variables = []
        self.interfaces = []

    def parse(self, content, type=None):
        """
        :param content:
        :param type:
        :return:
        """
        raise NotImplementedError

    def create(self):
        """
        :return:
        """
        # 首先创建项目信息。
        team_plugin = TeamPlugin()
        team_plugin.create(
            team=self.team,
            project=self.project,
            owner='plugin'
        )
        # 然后创建变量
        for variable in self.variables:
            variable_plugin = VariablePlugin()
            variable_plugin.create(
                team=self.team,
                project=self.project,
                owner='plugin',
                **variable
            )
        # 接着创建接口
        cases = []
        for interface in self.interfaces:
            interface_plugin = InterfacePlugin()
            id, _, _, _ = interface_plugin.create(
                team=self.team,
                project=self.project,
                **interface
            )
            cases.append(id)
        # 最后创建套件
        if cases:
            suite_plugin = SuitePlugin()
            suite_plugin.create(
                name=self.suite,
                team=self.team,
                project=self.project,
                type='interface',
                cases=cases
            )
