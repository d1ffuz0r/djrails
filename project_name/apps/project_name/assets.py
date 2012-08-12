# -*- coding: utf-8 -*-

from django_assets import Bundle, register

js = Bundle('js/home.coffee',
            filters='coffeescript',
            output='gen/javascript.js')

css = Bundle('css/home.ccss',
             filters='clevercss',
             output='gen/all.css')

register('js_all', js)
register('css_all', css)