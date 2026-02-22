Small project as a proof of concept.\
[NiceGUI](https://nicegui.io/) is used as frontend to downloand youtube videos. 
The backend is powered by 
[yt-dlp](https://github.com/yt-dlp/yt-dlp).\


# Run
- Clone the project
- Copy .env_template to .env and update .env
- Execute ./build_and_run.sh
- Visit http://localhost:{FRONTEND_PORT}. Where FRONTEND_PORT is defined in .env

# Howto
- Paste a youtube link in the *URL* textbox.
- Choose wether you want to download the video or the audio only.
- You can set the title of the file. If not the title of the youtube video is used.
- Connect the device of your choice with the included ftp server to transfer youre freshly loaded files.  