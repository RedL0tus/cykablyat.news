#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json
import jinja2
import random
import aiohttp_jinja2

from aiohttp import web

CONF = 'config.json'

routes = web.RouteTableDef()

news = []
with open(CONF) as f:
    news = json.loads(f.read())


@routes.get('/')
@aiohttp_jinja2.template('template.html')
async def redir(request):
    passage = random.choice(news['news'])
    return {'news': passage}

if __name__ == '__main__':
    app = web.Application()
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader('.')
    )
    app.add_routes(routes)
    web.run_app(app, port=10010)
