# YouTube Video Downloader

A Python-based YouTube video downloader with playlist support using yt-dlp.

## Features

- ✅ Download single videos or playlists
- ✅ Multiple quality options (Best, 1080p, 720p, 480p)
- ✅ Audio-only download (MP3)
- ✅ Playlist control (entire, single video, first 5, custom range)
- ✅ Automatic downloads folder creation
- ✅ Error handling and user-friendly interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/barisyildizel1-creator/Python-Projects.git
cd YouTube-Video-Downloader
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the downloader:
```bash
python Downloader.py
```

Follow the interactive prompts to:
1. Enter YouTube URL (single video or playlist)
2. Choose quality options
3. Select playlist handling (if applicable)

## Quality Options

1. **Best** - Original quality
2. **1080p** - High definition
3. **720p** - Standard HD (recommended for compatibility)
4. **480p** - Standard definition
5. **Audio only** - MP3 format

## Playlist Options

When a playlist is detected:
1. **Download entire playlist** - All videos
2. **Download single video** - Only the specific video
3. **Download first 5 videos** - Good for testing
4. **Download specific range** - Custom start/end numbers

## Requirements

- Python 3.7+
- yt-dlp
- FFmpeg (for audio extraction)

## File Structure

```
YouTube-Video-Downloader/
├── Downloader.py          # Main application
├── ROADMAP.md            # Development roadmap
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── downloads/           # Downloaded videos (auto-created)
```

## Contributing

This is a learning project. Feel free to suggest improvements or report issues!

## License

This project is for educational purposes.