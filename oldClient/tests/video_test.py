from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class VideoApp(App):
    def build(self):
        video_url = "file:///C:/Users/Adrian/Videos/MemeClips/Tokyo Drift.mp4"
        video = VideoPlayer(source=video_url, state='play')
        return video

if __name__ == '__main__':
    VideoApp().run()