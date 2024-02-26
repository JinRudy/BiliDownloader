
from moviepy.editor import VideoFileClip

import os, time

class VideoProcessor:
    def __init__(self, video_path):
        self.video = VideoFileClip(video_path)
        self.video_path = video_path
        self.filename = os.path.basename(video_path).split(".")[0]

    def subclip(self, start, end):
        trimmed_video = self.video.subclip(start, end)
        trimmed_video.write_videofile(f'{self.filename}-{time.time()}-{start}-{end}.mp4')

    def audio_subclip(self, start, end):
        filename = self.filename
        if os.path.exists(f'{filename}.mp3'):
            print("文件已存在于当前目录,请重新选择！")
            return
        self.video.audio.write_audiofile(f'{filename}.mp3')
        
if __name__ == '__main__':
    video_path = "D:\Program Files (x86)\Majjcom\BiliDownloader\BiliDownloader\Download\GitHub_一周热点汇总第9期_202\\001-GitHub_一周热点汇总第9期_202.mp4"
    video = VideoProcessor(video_path)
    video.subclip(20,40);
    # video.audio_subclip(20,40)