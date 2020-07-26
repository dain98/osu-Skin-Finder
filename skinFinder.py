import urllib.request, json
import time

print("OSU! SKIN FOLDER READER")
print("Press Ctrl + C to kill the program.")
print("Attempting to open skin.txt...")
try:
    with open("skin.txt","w+") as f:
        currentSkin = ""
        while True:
            with urllib.request.urlopen("http://localhost:24050/json") as url:
                data = json.loads(url.read().decode("utf8"))
            skin = str(data['menu']['skinFolder'])
            if currentSkin != skin:
                f.seek(0)
                f.truncate()
                try:
                    f.write(skin)
                    print(f"Skin found: {skin}")
                    currentSkin = skin
                except:
                    f.write("ERROR")
                    print("Error trying to read skin--most likely strange characters within skin name.")
                    currentSkin = skin
                f.flush()

            # time.sleep(1)

except Exception as e:
    print(e)
    try:
        os.system('pause')  #windows, doesn't require enter
    except whatever_it_is:
        os.system('read -p "Press any key to continue"')
