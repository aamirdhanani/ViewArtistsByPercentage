#Personal client and secrect ID
#Need to be connected to the Spotify Web API
#Both Spotipy and MathLabPlot are needed to run this code
cid = "" 
scid = ""

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=cid,client_secret=scid)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#USERNAME and TARGET PLAYLIST ID
user = input("Enter your username: ")
USERNAME = user

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


#gets the artists from user tracks
x = []
def show_tracks(results):
    for item in results:
        track = item['track']
       # print track
        if track is not None:
            x.append(track['artists'][0]['name'])
            #print track['artists'][0]['name']
        
        #print track['name']

#Reformats the artists name
def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None



### MAIN INPUT ----------------------------------------------------------------------------------------------------------
#First part of input, asks for the playlist you want to get artists from

if len(sys.argv) > 1:
    user = sys.argv[1]
playlists = sp.user_playlists(USERNAME)

# Displays playlists and add there ID's to a list 
idList = []
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(playlist['name'])
        print (playlist['id'])
        idList.append (playlist['id'])
        print (i)
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

#Asks for a user to choose a playlist based on its number
print ("Please choose a playlist number")
target = input()
target = int(target)
print (idList[target])
id = idList[target]
results = get_playlist_tracks(sp._get_id,id)
 

#Calls for the lists of artists from the tracks
show_tracks(results)
Xtotal = x
Xval = list(dict.fromkeys(Xtotal))
Yval = []

#Gets the artist
for i in Xval:
    Yval.append(Xtotal.count(i))

# Creates the pie graph
import matplotlib.pyplot as plt
plt.pie(Yval, labels=Xval,rotatelabels=True,autopct='%1.1f%%',pctdistance=0.9,labeldistance=1,textprops={'fontsize':7})
plt.xticks(fontsize='5')
plt.show()

