import subprocess
import os.path
import shutil

from moviepy.editor import VideoFileClip

import base.util as util
from base.log import logger

FFMPEG = 'ffmpeg'
FFPROBE = 'ffprobe'


class CompressDelegate(object):
    def __init__(self):
        pass

    def get_video_duration(self, path):
        clip = VideoFileClip(path)
        return clip.duration

    def compress(self, config, input_paths):
        for input_path in input_paths:
            success = self._compress_one(config, input_path)
            # check fail

    def _compress_one(self, config, input_path):
        logger.debug('Start compress video')
        output_path = util.get_uuid_mp4()
        duration = int(self.get_video_duration(input_path))
        cmd = [FFMPEG, '-y',
               '-i', input_path,
               '-c:v', 'libx264',
               '-preset', 'slow',
               '-b:v', '1024k',
               '-c:a', 'aac',
               '-b:a', '64k',
               '-f', 'mp4',
               output_path]
        if duration > 20:
            start = duration - 20
            end = duration
            cmd = [
                FFMPEG, '-y',
                '-i', input_path,
                '-c:v', 'libx264',
                '-preset', 'slow',
                '-b:v', '1024k',
                '-c:a', 'aac',
                '-b:a', '64k',
                '-f', 'mp4',
                '-ss', str(start),
                '-t', str(end),
                output_path]

        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        process.communicate()
        if os.path.exists(output_path):
            origin_path = input_path
            new_path = output_path
            shutil.move(new_path, origin_path)
            return True
        return False
