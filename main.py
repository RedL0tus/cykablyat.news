#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json
import random

from sanic import Sanic
from sanic_jinja2 import SanicJinja2

CONF = 'config.json'

app = Sanic(__name__)

jinja = SanicJinja2(app, pkg_path='.')

news = {}
with open(CONF) as f:
    news = json.loads(f.read())


@app.route('/')
@jinja.template('template.html')
async def redir(request):
    passage = random.choice(news['news'])
    return {'news': passage}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10010)
