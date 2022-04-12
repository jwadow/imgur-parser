import string
import random
import os
import shutil
import requests
import threading

noneWorking = [0, 503, 4939, 4940, 4941, 6167, 12003, 5556, 5082]
userhome = os.path.expanduser('~')

#edit this to change folder or parsing threads
save_folder = userhome + '/Desktop/imgur-parser/'
parse_threads = 20

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

def main():
    while True:
        amount = int(''.join(random.choice('5' + '6') for _ in range(1)))
        if amount == 6:
            N = 3
            picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N)))
            picture2 = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(N)))
            name = picture + picture2
            printsc = "http://i.imgur.com/" + "" + str(picture) + str(picture2) + ".jpg"

        if amount == 5:
            N = 5
            picture = str(''.join(
                random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N)))
            name = picture
            printsc = "http://i.imgur.com/" + "" + str(picture) + ".jpg"

        #line = str(name) + ".jpg"
        response = requests.get(printsc, stream=True)
        image_file = save_folder + str(name) + ".jpg"
        with open(image_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

        size = os.path.getsize(image_file)
        if size in noneWorking:
            #print("[-] Invalid: " + str(name))
            os.remove(image_file)
        else:
            print("Saved: " + printsc)

if __name__ == '__main__':
    for i in range(parse_threads):
        my_thread = threading.Thread(target=main)
        my_thread.start()
