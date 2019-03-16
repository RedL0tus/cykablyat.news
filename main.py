#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json
import random

# Sanic!!!
from sanic import Sanic
from sanic.log import logger
from sanic_jinja2 import SanicJinja2

# Configurations
CONF = 'config.json'
PORT = 10010
HOST = '0.0.0.0'

# Sanic & SanicJinja2 instances
APP = Sanic(__name__)
JINJA = SanicJinja2(APP, pkg_path='.')


class Blyat(object):
    """Blyat!"""


class Cyka(Blyat):
    """The main class"""

    def __init__(self, config_path='config.json'):
        """
        Initialize the object
        :param config_path:
        """
        self.config_path = config_path
        self.news = dict()
        self.reload()
        logger.info('Instance initialized')

    def reload(self):
        """
        Reload the configuration
        :return: None
        """
        with open(self.config_path) as f:
            self.news = json.loads(f.read())
        logger.info('Configuration loaded')
        return

    async def redir(self, request):
        """
        Do the actual thing
        :param request: Provided by Sanic
        :return: Response rendered by SanicJinja2
        """
        passage = random.choice(self.news['news'])
        return JINJA.render('template.html', request, news=passage)


if __name__ == '__main__':
    logger.info('Starting up')
    ayy = Cyka(config_path=CONF)
    APP.add_route(ayy.redir, '/')
    APP.run(host=HOST, port=PORT)
