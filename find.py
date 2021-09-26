from data import get_data


def find_author(token, authors=None):
    """
    Function to get data from spotify api
    """
    return_dict = {}

    for author in authors:
        
        artist_data = get_data(
            url=f"https://api.spotify.com/v1/artists/{author}",

            headers={"Authorization": f"Bearer {token}"}
        )

        if artist_data['name'] not in return_dict:
            return_dict[artist_data['name']] = {

            }

            
            return_dict[artist_data['name']]['songs'] = {}

        
        return_dict[artist_data['name']]['artist_image'] = artist_data['images'][0]['url']

        song_data = get_data(
            url=f"https://api.spotify.com/v1/artists/{author}/top-tracks?market=US",
            
            headers={"Authorization": f"Bearer {token}"}
        )
        for i in song_data['tracks']:
            art = i['album']['images'][0]['url']
            song_name = i['name']
            song_url = i['preview_url']
            return_dict[artist_data['name']]['songs'][song_name] = {
                'image': art,
                'song_url': song_url
            }
    return return_dict
