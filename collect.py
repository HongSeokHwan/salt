import os
import time
from stat import *

import glob2

from base.log import logger


class CollectDelegate(object):
    def __init__(self):
        pass

    def collect(self, config):
        # logger.debug('Collect start')
        media_path = config['media_path']
        compress_day = config['compress_day']
        file_size_byte_limit = config['file_size_byte_limit']

        now = time.localtime()
        targets = []
        for filename in glob2.glob(media_path + '/**/*.mp4'):
            # logger.debug('Try file: %s' % filename)
            st = os.stat(filename)
            file_time = time.localtime(st[ST_MTIME])
            diff_sec = (time.mktime(now) - time.mktime(file_time)) / 60
            diff_days = diff_sec / (60 * 24)

            if diff_days < compress_day:
                continue

            file_size_byte = st[ST_SIZE]
            if file_size_byte < file_size_byte_limit:
                continue
            print filename
            logger.debug(
                'Collect target file exist: %s, %s bytes, %.2f days' % (
                    filename, "{:,}".format(file_size_byte), diff_days))
            targets.append(filename)
        return targets
