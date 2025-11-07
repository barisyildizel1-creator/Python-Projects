from yt_dlp import YoutubeDL
import os

def get_download_info():
    """Get URL and quality choice from user"""
    url = input("Enter YouTube URL: ")
    
    # Check if it's a playlist
    playlist_options = None
    if 'playlist' in url or 'list=' in url:
        print("\n🎵 Playlist detected!")
        print("Playlist options:")
        print("1. Download entire playlist")
        print("2. Download single video from playlist")
        print("3. Download first 5 videos")
        print("4. Download specific range (e.g., videos 1-10)")
        
        playlist_choice = input("Choose playlist option (1-4): ")
        
        if playlist_choice == '4':
            start = input("Start video number: ")
            end = input("End video number: ")
            playlist_options = {'start': start, 'end': end}
        else:
            playlist_options = {'choice': playlist_choice}
    
    print("\nQuality options:")
    print("1. Best (original quality)")
    print("2. 1080p")
    print("3. 720p") 
    print("4. 480p")
    print("5. Audio only (MP3)")
    
    quality = input("Choose quality (1-5): ")
    return url, quality, playlist_options

def get_format_from_choice(choice):
    """Convert user choice to yt-dlp format string"""
    formats = {
        '1': 'best',
        '2': 'best[height<=1080]',
        '3': 'best[height<=720]',
        '4': 'best[height<=480]',
        '5': 'bestaudio'
    }
    return formats.get(choice, 'best[height<=720]')  # Default to 720p

def create_ydl_opts(format_choice, quality_choice, playlist_options=None):
    """Create yt-dlp options based on user choice"""
    # Ensure downloads directory exists
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    ydl_opts = {
        'format': format_choice,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'ignoreerrors': True,
        'no_warnings': True,
    }
    
    # Handle playlist options
    if playlist_options:
        choice = playlist_options.get('choice')
        if choice == '2':  # Single video from playlist
            ydl_opts['noplaylist'] = True
        elif choice == '3':  # First 5 videos
            ydl_opts['playlistend'] = 5
        elif choice == '4':  # Specific range
            start = playlist_options.get('start', '1')
            end = playlist_options.get('end', '10')
            ydl_opts['playliststart'] = int(start)
            ydl_opts['playlistend'] = int(end)
        # choice == '1' downloads entire playlist (no extra options needed)
    
    # Add audio extraction for MP3 option
    if quality_choice == '5':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    
    return ydl_opts

def download_video(url, ydl_opts):
    """Download video with given options"""
    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(f"\nDownloading: {url}")
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def main():
    """Main function to run the downloader"""
    print("=== YouTube Video Downloader ===")
    
    # Get user input
    url, quality_choice, playlist_options = get_download_info()
    
    # Get format string
    format_choice = get_format_from_choice(quality_choice)
    
    # Create options
    ydl_opts = create_ydl_opts(format_choice, quality_choice, playlist_options)
    
    # Download video
    download_video(url, ydl_opts)

if __name__ == "__main__":
    main()