from datetime import datetime, timedelta

from exif import Image
from datetime import datetime

start_time = datetime.now()
now_time = datetime.now()
while (now_time < start_time + timedelta(minutes=10)): # this makes sure our program stops after 10 mins
    def get_time(image):
        with open(image, 'rb') as image_file:
            img = Image(image_file)
            time_str = img.get("datetime_original")
            time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
            return time


    def time_diff(photo1, photo2):
        time_1 = get_time(photo1)
        time_2 = get_time(photo2)
        return time_2 - time_1
    now_time = datetime.now()









print(time_diff('atlas_photo_012.jpg', 'atlas_photo_013.jpg'))