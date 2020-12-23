import json
from pathlib import Path

import fastapi
import uvicorn

from starlette.staticfiles import StaticFiles



from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()

def configure():
	configure_routing()
	configure_apikeys()

def configure_routing():
	api.mount('/static', StaticFiles(directory='static'), name='static')
	api.include_router(home.router)
	api.include_router(weather_api.router)

def configure_apikeys():
	file = Path('settings.json').absolute()
	if not file.exists():
		raise Exception("settings.json file not found, please see settings.template.")

	with open('settings.json') as fin:
		settings = json.load(fin)
		openweather_service.api_key = settings.get('api_key')

if __name__ == '__main__':
	configure()
	uvicorn.run(api, port=8000, host='127.0.0.1')
else:
	configure()