# Clover全局配置
DEBUG = True
VERSION = '1.3.3'
DOMAIN = 'http://demo.52clover.cn'

# 全局功能配置
GLOBALS = {
    'timeout': {
        'connect': 3,
        'read': 60,
    },  # 全局接口超时配置，默认链接超时3秒，读超时60秒。
    'retry': 2,     # 全局接口重试配置，默认2次。
    'performance': 1000,       # 接口性能要求，1000ms以内。
}

# MySQL数据库配置
MYSQL = {
    'user': 'clover',
    'pswd': '52.clover',
    'host': '127.0.0.1',
    'port': '3306',
}
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pswd}@{host}:{port}/clover?charset=UTF8MB4'.format(**MYSQL)
SQLALCHEMY_TRACK_MODIFICATIONS=True

# 使用redis作为消息队列
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DATABASE = 0
REDIS_STREAM_NAME = 'clover'

# 功能控制，True则生效，False则无效
MODULE = {
    'join': True,   # 展示加入我们
    'task': False,  # 开发中的定时任务
    'keyword': True, # 开发中的关键字配置
}

NOTIFY = {
    # 通知的触发事件，成功时通知还是失败时通知
    'event': ['success', 'failed'],
    # 通知的方式，企业微信还是email，或则配置的其它方式
    'channel': {
        'email': {
            'sender': '1234567@qq.com',
            'receiver': ['1234567@qq.com'],
            'password': 'xxxxxxxxxxxxxxxx',
            'smtp_host': 'smtp.qq.com',
        },
        'wechat': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',    #这里是企微机器人的KEY配置
        'dingtalk': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',    #这里是钉钉机器人的access_token配置
    },
}
