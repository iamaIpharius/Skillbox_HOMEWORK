import requests
import json

death_req = requests.get('https://www.breakingbadapi.com/api/deaths')
print(death_req.text)
data_death = json.loads(death_req.text)

most_deaths = sorted(data_death, key=lambda x: x['number_of_deaths'])[-1]
ep_req = requests.get('https://www.breakingbadapi.com/api/episodes')

data_ep = json.loads(ep_req.text)
most_deaths_ep = list(
    filter(lambda x: x['season'] == str(most_deaths['season']) and x['episode'] == str(most_deaths['episode']),
           data_ep))

most_deaths_episode_data = {
    'episode_id': most_deaths_ep[0]['episode_id'],
    'season': most_deaths['season'],
    'episode': most_deaths['episode'],
    'number_of_deaths': most_deaths['number_of_deaths'],
    'death': most_deaths['death']
}
with open('most_death_episode.json', 'w') as file:
    json.dump(most_deaths_episode_data, file, indent=4)

print(most_deaths_episode_data)

