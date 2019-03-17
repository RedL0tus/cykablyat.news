#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import yaml
import random
import signal

# Sanic!!!
from sanic import Sanic
from sanic.log import logger
from sanic_jinja2 import SanicJinja2

# Configurations
NEWS = 'news'
CONF = 'config.json'
PORT = 10010
HOST = '0.0.0.0'
PID_FILE = 'cykablyat.pid'
HEADERS = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0',
    'X-Served-By': 'Blyat'
}

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
        self.news = list()
        self.reload()
        logger.info('Instance initialized')

    def reload(self):
        """
        Reload the configuration
        :return: None
        """
        if not os.path.exists(NEWS) and not os.path.isdir(NEWS):
            logger.error('News directory not found, quitting...')
            exit(1)
        for source_type in os.listdir(NEWS):
            for source in os.listdir(NEWS + '/' + source_type):
                with open(NEWS + '/' + source_type + '/' + source) as source_f:
                    source_content = yaml.load(source_f.read(), Loader=yaml.FullLoader)
                source_parsed = source_content
                source_parsed['type'] = source_type
                self.news.append(source_parsed)
                logger.debug('Loaded %s' % NEWS + '/' + source_type + '/' + source)
        logger.info('Configuration (re)loaded')
        return

    def signal_handler(self, signum, frame):
        """
        Singal handler for reloading configuration
        :param signum: The number of the signal
        :param frame: The stack frame provided by signal
        :return: None
        """
        logger.info('Received SIGNAL(%s), reloading configuration' % signum)
        logger.debug('Frame: %s', frame)
        self.reload()
        return

    async def redir(self, request):
        """
        Do the actual thing
        :param request: Provided by Sanic
        :return: Response rendered by SanicJinja2
        """
        passage = random.choice(self.news)
        return JINJA.render(
            'index.html', request, news=passage,
            headers=HEADERS
        )

    async def list(self, request):
        """
        List all the news
        :param request: Provided by Sanic
        :return: Response rendered by SanicJinja2
        """
        return JINJA.render(
            'list.html', request, news=self.news,
            headers=HEADERS
        )


if __name__ == '__main__':
    # Start the server
    logger.info('Starting up')
    logger.info('PID: %s' % os.getpid())
    # Write pid to file
    with open(PID_FILE, 'w') as pid_f:
        pid_f.write(str(os.getpid()))
    # Initialize the instance
    ayy = Cyka(config_path=CONF)
    APP.add_route(ayy.redir, '/')
    APP.add_route(ayy.list, '/list')
    # Activate signal handler
    signal.signal(signal.SIGHUP, ayy.signal_handler)  # SIGHUP
    # Link start!
    try:
        APP.run(host=HOST, port=PORT)
    finally:
        os.remove(PID_FILE)  # Remove PID file on exit
