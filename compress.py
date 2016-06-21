import subprocess

from moviepy.editor import VideoFileClip

from base.log import logger

FFMPEG = 'ffmpeg'
FFPROBE = 'ffprobe'


class CompressDelegate(object):
    def __init__(self):
        pass

    def get_video_duration(self, path):
        clip = VideoFileClip(path)
        return clip.duration

    def compress(self, input_path, output_path):
        logger.debug('Start compress video')
        # TODO: delete output_path if exist
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
        # TODO: check output_path exist or not
        return True
