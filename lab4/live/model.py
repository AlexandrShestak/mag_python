# -*- coding: utf-8 -*-
import json
import random
import argparse


class Victim(object):
    def __init__(self, max_age, duplication_time):
        self.max_age = max_age
        self.age = 0
        self.duplication_time = duplication_time
        self.time_without_duplication = 0


class Predator(object):
    def __init__(self, max_age, duplication_time, max_starvation_time):
        self.age = 0
        self.max_age = max_age
        self.duplication_time = duplication_time
        self.max_starvation_time = max_starvation_time
        self.starvation_time = 0
        self.time_without_duplication = 0


class Barrier(object):
    pass


def read_map(configuration_name, iterations_count):
    with open(configuration_name) as config:
        data = json.load(config)

        predator_max_age = data['predatorMaxAge']
        predator_duplication_time = data['predatorDuplicationTime']
        victim_duplication_time = data['victimDuplicationTime']
        predator_starvation_time = data['predatorStarvationTime']
        map_name = data['mapName']
        initial_predator_count = data['initialPredatorCount']
        initial_victim_count = data['initialVictimCount']

        map_size = data['mapSize']
        live_map = [[None for i in range(map_size)] for j in range(map_size)]

        map_file = open(map_name, 'r')
        row = 0
        for line in map_file:
            for column, elem in enumerate(line):
                if elem != '\n':
                    if elem == "P":
                        live_map[row][column] = Predator(predator_max_age, predator_duplication_time,
                                                         predator_starvation_time)
                    elif elem == "V":
                        live_map[row][column] = Victim(iterations_count, victim_duplication_time)
                    elif elem == "B":
                        live_map[row][column] = Barrier()
            row += 1
        map_file.close()

    return live_map, map_size, initial_predator_count, initial_victim_count


def find_nearest_empty_cells(row, column, live_map, map_size):
    nearest_empty_cells = []
    for row_variation in [-1, 0, 1]:
        for column_variation in [-1, 0, 1]:
            if 0 <= row + row_variation < map_size and 0 <= column + column_variation < map_size \
                    and live_map[row + row_variation][column + column_variation] is None:
                nearest_empty_cells.append((row + row_variation, column + column_variation))

    return nearest_empty_cells


def find_all_nearest_victim_cells(row, column, live_map, map_size):
    nearest_cells = []
    for row_variation in [-1, 0, 1]:
        for column_variation in [-1, 0, 1]:
            if 0 <= row + row_variation < map_size and 0 <= column + column_variation < map_size \
                    and isinstance(live_map[row + row_variation][column + column_variation], Victim):
                nearest_cells.append((row + row_variation, column + column_variation))

    return nearest_cells


# def print_live_map(live_map, map_size):
#     for i in xrange(0, map_size):
#         line = ""
#         for j in xrange(0, map_size):
#             if isinstance(live_map[i][j], Victim):
#                 line += "V"
#             elif isinstance(live_map[i][j], Predator):
#                 line += "P"
#             elif isinstance(live_map[i][j], Barrier):
#                 line += "B"
#             else:
#                 line += " "
#         print line


def write_result_to_file(live_map, map_size, result_name):
    with open(result_name, 'w') as result_file:
        for i in xrange(0, map_size):
            line = ""
            for j in xrange(0, map_size):
                if isinstance(live_map[i][j], Victim):
                    line += "V"
                elif isinstance(live_map[i][j], Predator):
                    line += "P"
                elif isinstance(live_map[i][j], Barrier):
                    line += "B"
                else:
                    line += " "
            result_file.write(line + '\n')


def generate_live(iterations_count, configuration_name, result_name):
    live_map, map_size, predator_count, victim_count = read_map(configuration_name, iterations_count)
    for live_age in xrange(0, iterations_count):

        # stop live if all predators or victims were died
        if predator_count == 0 or victim_count == 0:
            write_result_to_file(live_map, map_size, result_name)
            return

        exclude_cells = []
        for i in xrange(0, map_size):
            for j in xrange(0, map_size):
                if (i, j) not in exclude_cells:
                    current_instance = live_map[i][j]

                    # Predator will try to find Victim
                    if isinstance(current_instance, Predator):
                        nearest_victim_cells = find_all_nearest_victim_cells(i, j, live_map, map_size)
                        if nearest_victim_cells:
                            random_nearest_cell = random.choice(nearest_victim_cells)
                            current_instance.starvation_time = 0
                            live_map[random_nearest_cell[0]][random_nearest_cell[1]] = None
                            victim_count -= 1
                        else:
                            if current_instance.starvation_time == current_instance.max_starvation_time:
                                live_map[i][j] = None
                                current_instance = None
                                predator_count -= 1
                            else:
                                current_instance.starvation_time += 1

                    if isinstance(current_instance, Victim) or isinstance(current_instance, Predator):
                        nearest_empty_cells = find_nearest_empty_cells(i, j, live_map, map_size)
                        # duplicate if possible
                        if current_instance.time_without_duplication >= current_instance.duplication_time \
                                and nearest_empty_cells:
                            current_instance.time_without_duplication = 0
                            random_nearest_cell = random.choice(nearest_empty_cells)
                            if isinstance(current_instance, Victim):
                                new_entity = Victim(current_instance.max_age, current_instance.duplication_time)
                                victim_count += 1
                            else:
                                new_entity = Predator(current_instance.max_age, current_instance.duplication_time,
                                                      current_instance.max_starvation_time)
                                predator_count += 1
                            live_map[random_nearest_cell[0]][random_nearest_cell[1]] = new_entity
                            exclude_cells.append((random_nearest_cell[0], random_nearest_cell[1]))
                            nearest_empty_cells.remove(random_nearest_cell)

                        # check age and if entity is still alive then move it
                        if current_instance.age == current_instance.max_age:
                            live_map[i][j] = None
                            if isinstance(current_instance, Victim):
                                victim_count -= 1
                            else:
                                predator_count -= 1
                        elif nearest_empty_cells:
                            nearest_empty_cells.append((i, j))
                            random_nearest_cell = random.choice(nearest_empty_cells)
                            if random_nearest_cell != (i, j):
                                exclude_cells.append((random_nearest_cell[0], random_nearest_cell[1]))
                                live_map[random_nearest_cell[0]][random_nearest_cell[1]] = current_instance
                                live_map[i][j] = None
                        current_instance.age += 1
                        current_instance.time_without_duplication += 1

        # print_live_map(live_map, map_size)
    write_result_to_file(live_map, map_size, result_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Live generator')
    parser.add_argument('-i', '--iterations', help="number of iterations", type=int)
    parser.add_argument('-c', '--configuration', help="Configuration file name", type=str)
    parser.add_argument('-o', '--output', help="File name in which result will be written")
    args = parser.parse_args()

    if args.iterations and args.configuration and args.output:
        generate_live(args.iterations, args.configuration, args.output)
    else:
        print 'Not all arguments were provided'
