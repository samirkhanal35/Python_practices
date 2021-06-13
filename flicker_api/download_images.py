import flickrapi
import urllib
import urllib.request
from PIL import Image

api_key = u'...'
api_secret = u'...'

flickr = flickrapi.FlickrAPI(api_key, api_secret)

keyword = 'cats'

photos = flickr.walk(text=keyword, tag_mode='all', tags=keyword,
                     extras='url_c', per_page=10, sort='relevance')


urls = []
for i, photo in enumerate(photos):
    print(i)

    url = photo.get('url_c')
    urls.append(url)

    # get 50 urls
    if i > 50:
        break

print(urls)

# Download image from the url and save it to '00001.jpg'
data = urllib.request.urlretrieve(urls[0])
print(data)
# Resize the image and overwrite it
image = Image.open(data[0])
image = image.resize((256, 256), Image.ANTIALIAS)
image.save('00000.jpg')
