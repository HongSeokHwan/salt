ffmpeg -i "input_data/free_sample.mp4" -c:v libx264 -preset slow -b:v 1024k -c:a aac -b:a 64k -f mp4 -ss 00:01:00 -t 00:01:15 "input_data/output.mp4"

#$ ffmpeg -i "filepath/filename.avi" -codec:v libx264 -profile:v baseline -preset slow -b:v 1000k -maxrate 1000k -bufsize 2000k -vf scale=-1:720 -threads 0 -codec:a aac -b:a 128k -f mp4 -ss 00:01:00 -t 01:00:00 -strict experimental "outputfilepath/outputfilename.mp4"
