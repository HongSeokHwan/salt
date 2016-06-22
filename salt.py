import sys
import time

from base.config import Config
from base.log import logger
from base.singleton import SingletonMixin
from collect import CollectDelegate
from compress import CompressDelegate
import base.util as util


class SaltMan(SingletonMixin):
    def __init__(self, config, collect_delegate, compress_delegate):
        super(SaltMan, self).__init__()
        self.config = config
        self.collect_delegate = collect_delegate
        self.compress_delegate = compress_delegate

    def run(self):
        logger.info('Start SaltMan.')
        lc = util.LoopChecker('Main loop')
        while True:
            try:
                targets = self.collect_delegate.collect(self.config)
                self.compress_delegate.compress(self.config, targets)
                time.sleep(1)
                lc.check()
                if len(targets) > 0:
                    lc.reset()
            except:
                e = sys.exc_info()[0]
                logger.error(e)
                time.sleep(5)


if __name__ == '__main__':
    SaltMan(Config().config, CollectDelegate(), CompressDelegate()).run()
