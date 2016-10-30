# Earthview Wallpaper Downloader
I love the wallpapers of [earthview.withgoogle.com]. They are great as desktop wallpapers. So I wrote a script to parse the download url of wallpaper from the site and then download the image and set that as desktop wallpaper. 😃

First clone this repo and give permission to execute `run.sh`.
```sh
$ chmod a+x run.sh
```
Then add `run.sh` to the crontab to change the wallpaper on whatever time duration you want.
```sh
crontab -e
```
This will open an editor, add cron command to the editor, then save and exit.
For example, to run this script hourly, write this command in crontab editor (`crontab -e`).
```
0 * * * * /path/to/run.sh
```

[earthview.withgoogle.com]: https://www.earthview.withgoogle.com
