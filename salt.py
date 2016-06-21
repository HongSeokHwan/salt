import time

from base.config import Config
from base.log import logger
from base.singleton import SingletonMixin
from collect import CollectDelegate
from compress import CompressDelegate


class SaltMan(SingletonMixin):
    def __init__(self, config, collect_delegate, compress_delegate):
        super(SaltMan, self).__init__()
        self.config = config
        self.media_path = self.config['media_path']
        self.collect_delegate = collect_delegate
        self.compress_delegate = compress_delegate

    def run(self):
        logger.info('Start SaltMan.')
        while True:
            targets = self.collect_delegate.collect(self.media_path)
            self.compress_delegate.compress(targets)
            time.sleep(1)


if __name__ == '__main__':
    SaltMan(Config(), CollectDelegate(), CompressDelegate()).run()
