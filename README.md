# youtubeplaylistdownloader
Download all the videos from a Youtube Playlist and convert it in Audio, so then you can train an AI Voice Cloner with them

YouTube Playlist Downloader and MP3 Converter
This Python code downloads a YouTube playlist and converts each video in the playlist to an MP3 audio file. Here's what the code does step-by-step:

Imports the necessary modules: pytube, os, moviepy.editor, and pydub.

Defines the YouTube playlist URL and saves it to a variable named playlist_url.

Creates a Playlist object using the playlist_url variable.

Defines the output directory where the videos should be saved and saves it to a variable named output_folder.

Loops through each video in the playlist and downloads the video in 360p quality to the output_folder using the download() method of the Video object.

Loops through each file in the output_folder directory and checks if the file is a video file using the endswith() method of the str object. If the file is a video file, it creates a VideoFileClip object using the video file, sets the output file path for the MP3 file, extracts the audio from the clip using the audio.write_audiofile() method of the VideoFileClip object, closes the clip to free up resources, deletes the original video file to save space, and compresses the audio file if it's larger than 10 MB.

The program finishes executing.
