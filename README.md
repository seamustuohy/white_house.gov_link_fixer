# white_house.gov_link_fixer
Opens the latest archived Presidential White House website a whitehouse.gov link exists within.

This script will check a whitehouse.gov link against [archived Presidential White House websites](https://www.archives.gov/presidential-records/research/archived-white-house-websites) to find the latest working version of that URL. It will then open that url in the browser. It only provides the most recent working version. It won't show you all the previous working versions. So, if multiple previous presidents had a version of a website it won't necessarily find you the one you are looking for.

# Usage
```
usage: Archived WhiteHouse.gov link fixer (WHGLF). [-h] [--verbose] [--debug] [--print_on_found] [--url URL]

options:
  -h, --help            show this help message and exit
  --verbose, -v         Turn verbosity on
  --debug, -d           Turn debugging on
  --print_on_found, -p  Print the archived url instead of opening it in the browser.
  --url URL, -u URL     whitehouse.gov URL to try find in the archives.
```

This will open the President Biden version of the url and print nothing.
```
$ python3 whglf.py -u 'https://www.whitehouse.gov/wp-content/uploads/2022/04/M-22-12.pdf'
```

This will print the President Biden version of the url and open nothing in the webrowser.
```
$ python3 whglf.py -p -u 'https://www.whitehouse.gov/wp-content/uploads/2022/04/M-22-12.pdf'
https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/04/M-22-12.pdf
```

This will log the President Biden version of the url and then open it in the webrowser.
```
$ python3 whglf.py -v -u 'https://www.whitehouse.gov/wp-content/uploads/2022/04/M-22-12.pdf'
INFO:__main__:Found the archived url https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/04/M-22-12.pdf
```

This will fail because the url doesn't exist.
```
$ python3 whglf.py -v -u 'https://www.whitehouse.gov/imafakeurlthatdoesntexist.html'
ERROR:__main__:Could not find an archived URL. Sorry....
```
