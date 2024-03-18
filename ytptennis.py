import random
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from moviepy.audio.fx.all import audio_fadein, audio_fadeout
from PIL import Image
from pytube import YouTube

def download_video(url, filename):
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').first().download(filename)

def add_audio(video_file, audio_file, output_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_file)
    video_clip.close()

def add_image(video_file, image_file, output_file, start_time):
    video_clip = VideoFileClip(video_file)
    img = Image.open(image_file)
    img = img.resize(video_clip.size)
    img_clip = video_clip.set_start(start_time).set_end(video_clip.duration)
    img_clip = img_clip.set_position(('center', 'bottom')).set_duration(video_clip.duration - start_time)
    final_clip = concatenate_videoclips([video_clip.subclip(0, start_time), img_clip])
    final_clip.write_videofile(output_file)
    final_clip.close()

def generate_ytp_tennis(source_video, audio_file, image_files, output_file, chaos=False, long=False):
    download_video(source_video, 'source.mp4')
    add_audio('source.mp4', audio_file, 'output.mp4')

    if chaos:
        # Implement chaos mode (random manipulation)
        pass

    if long:
        # Implement long mode (adding random videos before)
        pass

    # Add image/gif at random points
    for image_file in image_files:
        start_time = random.uniform(0, 20)  # Random start time within first 20 seconds
        add_image('output.mp4', image_file, 'output.mp4', start_time)

    os.rename('output.mp4', output_file)
    os.remove('source.mp4')

# Example usage
source_video = 'https://www.youtube.com/watch?v=your_source_video_id'
audio_file = 'your_audio_file.mp3'
image_files = ['image1.jpg', 'image2.jpg']  # Add paths to your image/gif files
output_file = 'final_output.mp4'

generate_ytp_tennis(source_video, audio_file, image_files, output_file, chaos=True, long=True)
