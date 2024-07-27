from rich import print
import json 

tx = """

{'collaborative': False, 'description': 'test', 'external_urls': {'spotify': 'https://open.spotify.com/playlist/7r1Nbtbi87a9uYNkJ7k3Lo'}, 'followers': {'href': None, 'total': 0}, 'href': 'https://api.spotify.com/v1/playlists/7r1Nbtbi87a9uYNkJ7k3Lo', 'id': '7r1Nbtbi87a9uYNkJ7k3Lo', 'images': [{'height': None, 'url': 'https://i.scdn.co/image/ab67616d00001e02e096bebbaeaa92c78d7043b4', 'width': None}], 'name': 'test hai del alter', 'owner': {'display_name': 'Anantaksh', 'external_urls': {'spotify': 'https://open.spotify.com/user/yrltq9qnsp1yoqux7s90dlk3j'}, 'href': 'https://api.spotify.com/v1/users/yrltq9qnsp1yoqux7s90dlk3j', 'id': 'yrltq9qnsp1yoqux7s90dlk3j', 'type': 'user', 
'uri': 'spotify:user:yrltq9qnsp1yoqux7s90dlk3j'}, 'primary_color': None, 'public': True, 'snapshot_id': 'AAAAA1T4itu8UMS5bfrHvnxXVt78nf+M', 'tracks': {'href': 'https://api.spotify.com/v1/playlists/7r1Nbtbi87a9uYNkJ7k3Lo/tracks?offset=0&limit=100', 'items': [{'added_at': '2024-07-17T08:21:49Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/yrltq9qnsp1yoqux7s90dlk3j'}, 'href': 'https://api.spotify.com/v1/users/yrltq9qnsp1yoqux7s90dlk3j', 'id': 'yrltq9qnsp1yoqux7s90dlk3j', 'type': 'user', 'uri': 'spotify:user:yrltq9qnsp1yoqux7s90dlk3j'}, 'is_local': False, 'primary_color': None, 'track': {'preview_url': 'https://p.scdn.co/mp3-preview/fc038125cdbe460d4cdfd7e3a8f18490bb44cc10?cid=5dda5144c6d041e380261738bd36eeae', 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 
'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'explicit': False, 'type': 'track', 'episode': False, 'track': True, 'album': {'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 
'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'type': 'album', 'album_type': 'single', 'href': 'https://api.spotify.com/v1/albums/6OBk036VgLGkxpggcFPqJL', 'id': '6OBk036VgLGkxpggcFPqJL', 'images': [{'url': 'https://i.scdn.co/image/ab67616d0000b273e096bebbaeaa92c78d7043b4', 'width': 640, 'height': 640}, {'url': 'https://i.scdn.co/image/ab67616d00001e02e096bebbaeaa92c78d7043b4', 'width': 300, 'height': 300}, {'url': 'https://i.scdn.co/image/ab67616d00004851e096bebbaeaa92c78d7043b4', 'width': 64, 'height': 64}], 'name': 'ファタール - Fatal', 'release_date': '2024-07-04', 'release_date_precision': 'day', 'uri': 'spotify:album:6OBk036VgLGkxpggcFPqJL', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7AUc6z9aVJftqLkiWdQ1ew'}, 'href': 'https://api.spotify.com/v1/artists/7AUc6z9aVJftqLkiWdQ1ew', 'id': '7AUc6z9aVJftqLkiWdQ1ew', 'name': 'GEMN', 'type': 'artist', 'uri': 'spotify:artist:7AUc6z9aVJftqLkiWdQ1ew'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/3KJigfhLjMfuE2HXsgXbln'}, 'href': 'https://api.spotify.com/v1/artists/3KJigfhLjMfuE2HXsgXbln', 'id': '3KJigfhLjMfuE2HXsgXbln', 'name': '中島健人', 'type': 'artist', 'uri': 'spotify:artist:3KJigfhLjMfuE2HXsgXbln'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/7mvhRvEAHiCTQHUnH7fgnv'}, 'href': 'https://api.spotify.com/v1/artists/7mvhRvEAHiCTQHUnH7fgnv', 'id': '7mvhRvEAHiCTQHUnH7fgnv', 'name': 'Tatsuya Kitani', 'type': 'artist', 'uri': 'spotify:artist:7mvhRvEAHiCTQHUnH7fgnv'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/6OBk036VgLGkxpggcFPqJL'}, 'total_tracks': 1}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7AUc6z9aVJftqLkiWdQ1ew'}, 'href': 'https://api.spotify.com/v1/artists/7AUc6z9aVJftqLkiWdQ1ew', 'id': '7AUc6z9aVJftqLkiWdQ1ew', 'name': 'GEMN', 'type': 'artist', 'uri': 'spotify:artist:7AUc6z9aVJftqLkiWdQ1ew'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/3KJigfhLjMfuE2HXsgXbln'}, 'href': 'https://api.spotify.com/v1/artists/3KJigfhLjMfuE2HXsgXbln', 'id': '3KJigfhLjMfuE2HXsgXbln', 'name': '中島健人', 'type': 'artist', 'uri': 'spotify:artist:3KJigfhLjMfuE2HXsgXbln'}, {'external_urls': 
{'spotify': 'https://open.spotify.com/artist/7mvhRvEAHiCTQHUnH7fgnv'}, 'href': 'https://api.spotify.com/v1/artists/7mvhRvEAHiCTQHUnH7fgnv', 'id': '7mvhRvEAHiCTQHUnH7fgnv', 'name': 'Tatsuya Kitani', 'type': 'artist', 'uri': 'spotify:artist:7mvhRvEAHiCTQHUnH7fgnv'}], 'disc_number': 1, 'track_number': 1, 'duration_ms': 219200, 'external_ids': {'isrc': 'JPU902401969'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/7gJD9BarjoFwL2BNQ0rpWT'}, 'href': 'https://api.spotify.com/v1/tracks/7gJD9BarjoFwL2BNQ0rpWT', 'id': '7gJD9BarjoFwL2BNQ0rpWT', 'name': 'ファタール - Fatal', 'popularity': 71, 'uri': 'spotify:track:7gJD9BarjoFwL2BNQ0rpWT', 'is_local': False}, 'video_thumbnail': {'url': None}}], 'limit': 100, 'next': None, 'offset': 0, 'previous': None, 'total': 1}, 'type': 'playlist', 'uri': 'spotify:playlist:7r1Nbtbi87a9uYNkJ7k3Lo'}

"""

tx = tx.replace("'", '"')
print(tx)
