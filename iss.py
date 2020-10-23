#!/usr/bin/env python
import requests
import time
import turtle

__author__ = """Darrell Purcell with help from
Daniel Lomelino and
https://docs.python.org/3/library/turtle.html#turtle.dot
https://www.geeksforgeeks.org/turtle-setpos-and-turtle-goto-functions-in-python/
"""


def in_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    space_dict = r.json()
    people = space_dict['people']
    total_in_space = space_dict['number']
    for person in people:
        print('Name: ' + person['name'])
        print('Craft: ' + person['craft'])
    print(f'Total astronauts in space: {total_in_space}')


def iss_data():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    api_dict = r.json()
    coords = api_dict['iss_position']
    x = float(coords['longitude'])
    y = float(coords['latitude'])
    timestamp = api_dict['timestamp']
    return [x, y, timestamp]


def render_map(x, y):
    r = 'http://api.open-notify.org/iss-pass.json?lat=39.76838&lon=-86.15804'
    passes_obj = requests.get(r)
    passes_data = passes_obj.json()
    pass_time = time.ctime(passes_data['response'][0]['risetime'])

    marker = turtle.Turtle()
    indy_x = -86.15804
    indy_y = 39.76838
    screen = turtle.Screen()

    screen.setup(width=720, height=360)
    screen.bgpic('map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')
    marker.penup()
    marker.goto(indy_x, indy_y)
    marker.dot(10, 'yellow')
    marker.color('yellow')
    marker.write(pass_time)
    marker.shape('iss.gif')
    marker.penup()
    marker.goto(x, y)
    turtle.done()


def main():
    in_space()
    coords = iss_data()
    render_map(coords[0], coords[1])


if __name__ == '__main__':
    main()
