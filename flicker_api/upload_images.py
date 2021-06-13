import os.path
import flickrapi
import webbrowser
import simplejson as json

api_key = u'c5fe55c278cdd7d072ddf2e0b83ed79e'
api_secret = u'46a168cf91dba3ff'

flickr = flickrapi.FlickrAPI(api_key, api_secret)
# photos = flickr.photos.search(user_id='193140407@N08', per_page='10')
# sets = flickr.photosets.getList(user_id='193140407@N08')
# print("photos", photos)
# title = sets['photosets']['photoset'][0]['title']['_content']

# print('First set title: %s' % sets)


print('Step 1: authenticate')

# flickr = flickrapi.FlickrAPI(api_key, api_secret)
# (token, frob) = flickr.get_token_part_one(perms='write')
# if not token:
#     input("press enter")
# flickr.get_token_part_two((token, frob))

# Only do this if we don't have a valid token already
if not flickr.token_valid(perms='write'):

    # Get a request token
    flickr.get_request_token(oauth_callback='oob')

    # Open a browser at the authentication URL. Do this however
    # you want, as long as the user visits that URL.
    authorize_url = flickr.auth_url(perms='write')
    webbrowser.open_new_tab(authorize_url)

    # Get the verifier code from the user. Do this however you
    # want, as long as the user gives the application the code.
    verifier = str(input('Verifier code: '))

    # Trade the request token for an access token
    flickr.get_access_token(verifier)

print('Step 2: use Flickr')
# resp = flickr.photos.getInfo(photo_id='51200710135')


# def callback(progress):
#     print(progress)


# class FileWithCallback(object):
#     def __init__(self, filename, callback):
#         self.file = open(filename, 'rb')
#         self.callback = callback
#         # the following attributes and methods are required
#         self.len = os.path.getsize(filename)
#         self.fileno = self.file.fileno
#         self.tell = self.file.tell

#     def read(self, size):
#         if self.callback:
#             self.callback(self.tell() * 100 // self.len)
#         return self.file.read(size)


# params = {}
# params['fileobj'] = FileWithCallback(params['samir.jpg'], callback)
# rsp = flickr.upload(params)
rsp = flickr.upload(
    '/home/samir/Documents/python_practices/flicker_api/samir.jpg', tags='''test2''', title='''Samir Khanal''', description='''test image for image upload with flicker api''')
# jsets = json.loads(rsp)
print("response:", rsp.get("stat"))
print("photoid:", rsp.find("photoid").text)
