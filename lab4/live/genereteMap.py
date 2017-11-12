# -*- coding: utf-8 -*-
import json
import random


def generate_map():
    with open('config.json') as config:
        data = json.load(config)

        map_size = data['mapSize']
        initial_predator_count = data['initialPredatorCount']
        initial_victim_count = data['initialVictimCount']
        initial_barrier_count = data['initialBarrierCount']

        positions = []

        for i in range(map_size):
            for j in range(map_size):
                positions.append((i, j))

        predator_positions = []
        for i in range(initial_predator_count):
            predator_position = random.choice(positions)
            predator_positions.append(predator_position)
            positions.remove(predator_position)

        victim_positions = []
        for i in range(initial_victim_count):
            victim_position = random.choice(positions)
            victim_positions.append(victim_position)
            positions.remove(victim_position)

        barrier_positions = []
        for i in range(initial_barrier_count):
            barrier_position = random.choice(positions)
            barrier_positions.append(barrier_position)
            positions.remove(barrier_position)

        live_map = [[0 for i in range(map_size)] for j in range(map_size)]
        for i in range(map_size):
            for j in range(map_size):
                if (i, j) in positions:
                    live_map[i][j] = " "
                elif (i, j) in predator_positions:
                    live_map[i][j] = "P"
                elif (i, j) in victim_positions:
                    live_map[i][j] = "V"
                else:
                    live_map[i][j] = "B"

        with open('map', 'w') as map_file:
            for row in live_map:
                for column in row:
                    map_file.write(column)
                    print column
                map_file.write('\n')


generate_map()
