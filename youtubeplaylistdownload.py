from pytube import Playlist
import os
import moviepy.editor as mp
from pydub import AudioSegment

# Define the YouTube playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLRxwlG9Zrvy7E5qvVxFNLKfuwI8xzSY3h"

# Create a Playlist object with the URL
playlist = Playlist(playlist_url)

# Define the output directory where the videos should be saved
output_folder = ""

# Loop through each video in the playlist and download in 360p quality
for video in playlist.videos:
    video.streams.filter(res="360p").first().download(output_path=output_folder)

# Convert the downloaded videos to MP3
for file in os.listdir(output_folder):
    # Check if the file is a video file
    if file.endswith(".mp4"):
        # Create a VideoFileClip object with the video file
        video_path = os.path.join(output_folder, file)
        clip = mp.VideoFileClip(video_path)

        # Set the output file path for the MP3 file
        mp3_path = os.path.join(output_folder, file.replace(".mp4", ".mp3"))

        # Extract the audio from the clip and save it as MP3
        clip.audio.write_audiofile(mp3_path)

        # Close the clip to free up resources
        clip.close()

        # Delete the original video file to save space
        os.remove(video_path)

        # Compress the audio file if it's larger than 10 MB
        audio_size = os.path.getsize(mp3_path)
        if audio_size > 10 * 1024 * 1024:
            print(f"Compressing {mp3_path}...")
            audio = AudioSegment.from_file(mp3_path, format="mp3")
            compressed_audio = audio.export(mp3_path, format="mp3", parameters=["-b:a", "64k"])
            compressed_audio.close()
