# -*- coding: utf-8 -*-

from base.log import logger
from base.singleton import SingletonMixin


class Util(SingletonMixin):
    def __init__(self):
        super(Util, self).__init__()


class LoopChecker(object):
    def __init__(self, msg):
        self.msg = msg
        self.cur_count = 1
        self.next_count = 2

    def check(self):
        self.cur_count += 1
        if self.cur_count >= self.next_count:
            self.next_count *= 2
            logger.info('%s (%d)' % (self.msg, self.cur_count))
