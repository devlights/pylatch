"""
TestSuite を定義しているファイルです。

REFERENCES::
http://d.hatena.ne.jp/pythonco/20061015/p3
https://www.yoheim.net/blog.php?q=20160903
https://docs.python.jp/3/library/doctest.html
"""
import unittest as ut
import doctest as dc

import pylatch.threadlatch as pl_thread
import pylatch.processlatch as pl_process


def doctest_suite() -> ut.TestSuite:
    """doctest 用の TestSuite を構築して返します。"""
    test_suite = ut.TestSuite()

    test_suite.addTest(dc.DocTestSuite(pl_thread))
    test_suite.addTest(dc.DocTestSuite(pl_process))

    return test_suite


if __name__ == '__main__':
    ut.TextTestRunner().run(doctest_suite())
