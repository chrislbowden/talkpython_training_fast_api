# Introduction to FastAPI 

Tutorial from https://training.talkpython.fm/.

Builds a basic API that, given a city, will request weather from https://openweathermap.org/api.

# Notes
Tutorial could be improved with guidance on writng tests for APIs.

Why not dockerise the app?

Is it a good idea to use mypy?

From experience I've noticed developers new to type hints, pydantic and mypy might let pydantic abstractions leak into the rest of the api when trying to satisfy mypy.
