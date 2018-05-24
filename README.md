# pylatch
Java や C# に存在する CountDownLatch を Python で簡易実装したものです。

(C# の場合は、 CountDownEvent がそれに当たる)

マルチスレッド版とマルチプロセス版があります。

どちらもクラス名は CountDownLatch です。

## 使い方 (マルチスレッド用)

利用するクラスは ```pylatch.threadlatch.CountDownLatch``` となります。

```python
    >>> # ---------------------------------------------
    >>> # スレッド処理で利用する場合
    >>> # ---------------------------------------------
    >>> import threading as th
    >>> import pylatch.threadlatch as pl

    >>> latch = pl.CountDownLatch(2)
    >>> th1 = th.Thread(target=lambda: latch.count_down())
    >>> th2 = th.Thread(target=lambda: latch.count_down())

    >>> latch.count
    2
    >>> latch.await(timeout=1.0)
    False

    >>> th1.start()
    >>> th1.join()
    >>> latch.count
    1
    >>> latch.await(timeout=1.0)
    False

    >>> th2.start()
    >>> th2.join()
    >>> latch.count
    0
    >>> latch.await(timeout=1.0)
    True
```

## 使い方 (マルチプロセス用)

利用するクラスは ```pylatch.processlatch.CountDownLatch``` となります。

```python
    >>> # ---------------------------------------------
    >>> # マルチプロセス処理で利用する場合
    >>> # ---------------------------------------------
    >>> import multiprocessing as mp
    >>> import pylatch.processlatch as pl

    >>> latch = pl.CountDownLatch(2)
    >>> proc1 = mp.Process(target=pl.__for_doctest, args=(latch,))
    >>> proc2 = mp.Process(target=pl.__for_doctest, args=(latch,))

    >>> latch.count
    2
    >>> latch.await(timeout=1.0)
    False

    >>> proc1.start()
    >>> proc1.join()
    >>> latch.count
    1
    >>> latch.await(timeout=1.0)
    False

    >>> proc2.start()
    >>> proc2.join()
    >>> latch.count
    0
    >>> latch.await(timeout=1.0)
    True
```

## テスト

現状、 doctest しか書いていません。そのうちユニットテスト追加します。

```sh
$ python -m doctest pylatch/threadlatch.py -v
$ python -m doctest pylatch/processlatch.py -v
```

# 参考情報

以下の情報を参考にさせていただきました。

- [Does Python have a similar control mechanism to Java's CountDownLatch?
](https://stackoverflow.com/questions/10236947/does-python-have-a-similar-control-mechanism-to-javas-countdownlatch)
- [Python で Java の CountDownLatch を実装してみる](https://qiita.com/shinkiro/items/75f3561d6bc96694ce30)
