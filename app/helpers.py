from flask import request


def _t(template_name):
    if request.MOBILE:
        return "mob_%s" % template_name
    return template_name

