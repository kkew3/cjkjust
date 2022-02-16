# -*- coding: utf-8 -*-

import pytest

import cjkjust

try:
    import wcwidth
except ImportError:
    installed_wcwidth = False
else:
    installed_wcwidth = True


def test_cjkljust():
    if not installed_wcwidth:
        assert cjkjust.cjkljust(u'hello', 10, u'*') == u'hello*****'
        assert cjkjust.cjkljust(u'你好world', 10, u'*') == u'你好world*'
        assert cjkjust.cjkljust(u'你好world', 1, u'*') == u'你好world'
        assert cjkjust.cjkljust(u'你好\tworld', 12, u'*') == u'你好\tworld**'
    else:
        assert cjkjust.cjkljust(u'hello', 10, u'*') == u'hello*****'
        assert cjkjust.cjkljust(u'你好world', 10, u'*') == u'你好world*'
        assert cjkjust.cjkljust(u'你好world', 1, u'*') == u'你好world'
        # test default value
        assert cjkjust.cjkljust(u'你好\tworld', 12, u'*') == u'你好\tworld**'

        # alternating `raises_on_indeterminate` and see if it takes immediate
        # effects
        cjkjust.raises_on_indeterminate = True
        with pytest.raises(ValueError):
            cjkjust.cjkljust(u'你好\tworld', 12, u'*')

        cjkjust.raises_on_indeterminate = False
        assert cjkjust.cjkljust(u'你好\tworld', 12, u'*') == u'你好\tworld**'

        cjkjust.raises_on_indeterminate = True
        with pytest.raises(ValueError):
            cjkjust.cjkljust(u'你好\tworld', 12, u'*')
