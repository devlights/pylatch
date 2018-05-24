"""
pylatch.processlatch のユニットテストが定義されています。

REFERENCES::
http://d.hatena.ne.jp/pythonco/20061015/p3
https://www.yoheim.net/blog.php?q=20160903
https://docs.python.jp/3/library/doctest.html
"""
import unittest as ut
import doctest as dc
import pylatch.processlatch as pl


class TestCountDownLatch(ut.TestCase):
    """pylatch.processlatch.CountDownLatch のユニットテストクラスです。"""

    def test_doctest(self):
        """doctest を実行します。"""
        ut.TextTestRunner().run(dc.DocTestSuite(pl))
