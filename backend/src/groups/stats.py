import matplotlib.pyplot as plt
from HallOfFame.settings import MEDIA_ROOT, os, MEDIA_URL
import numpy as np


def avg_points_by_label(data, mark_names):
    result = {}
    for name in mark_names:
        sum = 0
        students_num = 0
        for elem in data:
            if elem['for_what'] == name:
                sum += elem['value']
                students_num += 1
                if 'max_points' in elem and str(name) not in result:
                    result[str(name)] = {'max_points': elem['max_points']}
        result[str(name)]['val'] = (sum / students_num) if students_num != 0 else 0.0
    print(result)
    return result


def normalized_avg_points_by_label(data, mark_names):
    points = avg_points_by_label(data, mark_names)
    new_points = {}
    for label in points:
        # new_points[label]['max_points'] = 1
        val = points[label]['val'] / points[label]['max_points']
        # new_points[label] = {}
        # new_points[str(label)]['max_points'] = 1
        new_points[str(label)] = {'max_points': 1}
        new_points[str(label)]['val'] = val

        # new_points[label] = {'max_points': 1, 'val': val}
    print(new_points)
    return new_points


def avg_points_all_students(data):
    sum = 0
    max_points = 0
    for marks_list in data:
        for elem in marks_list:
            if 'value' in elem:
                sum += elem['value']
                max_points += elem['max_points']

    print({'val': sum / len(data), 'max_points': max_points / len(data)})
    return {'val': sum / len(data), 'max_points': max_points / len(data)}


def normalized_avg_points_all_students(data):
    sum = 0
    num_of = 0
    for marks_list in data:
        for elem in marks_list:
            if 'value' in elem:
                sum += elem['value']
                num_of += 1

    print({'val': sum / len(data), 'max_points': 1})
    return {'val': sum / len(data), 'max_points': 1}


def final_grade_for_all_students(enrolled_list):
    for student in enrolled_list:
        sum = 0
        total = 0
        for mark in student.marks_list:
            sum += mark.value
            total += mark.max_points
        result = sum / total
        if result < 0.5:
            student.final_grade = 2.0
        else:
            result -= 0.5
            result = round(result / 0.1)
            student.final_grade = 3.0 + result * 0.5

    return enrolled_list


def plot_data(plot_name, data, host):
    fig, ax = plt.subplots()

    whats = list(data.keys())
    values = [elem['val'] for elem in data.values()]
    max_points = [elem['max_points'] for elem in data.values()]
    diffrences = [max_points[i] - values[i] for i in range(len(values))]
    ind = np.arange(len(values))

    ax.bar(ind, values, color='b', tick_label=whats)
    # ax.bar(ind, values, color='b', label='Average', tick_label=whats)
    # ax.bar(ind, diffrences, bottom=values, color='r', label='Max', tick_label=whats)

    ax.set_ylabel('Percentage')
    ax.set_title("Average per exercise")
    ax.legend()
    ax.set_xticks(ind)
    ax.set_xticklabels(whats)
    a = plt.gca()
    a.set_ylim([0, 1])

    plot_name += '.png'
    path = os.path.join(MEDIA_ROOT, plot_name)
    plt.savefig(path)
    url = os.path.join(MEDIA_URL, plot_name)
    return host + url
#
#
# def plot_data(plot_name, data, host):
#     fig, ax = plt.subplots()
#
#     whats = list(data.keys())
#     values = [elem['val'] / elem['max_points'] * 100 for elem in data.values()]
#     max_points = [elem['max_points'] for elem in data.values()]
#     diffrences = [1 - values[i] for i in range(len(values))]
#     ind = np.arange(len(values))
#
#     ax.bar(ind, values, color='b', label='Average', tick_label=whats)
#     # ax.bar(ind, diffrences, bottom=values, color='r', label='Max', tick_label=whats)
#
#     ax.set_ylabel('Percentage')
#     ax.set_title("Average per exercise")
#     ax.legend()
#     ax.set_xticks(ind)
#     ax.set_xticklabels(whats)
#
#     plot_name += '.png'
#     path = os.path.join(MEDIA_ROOT, plot_name)
#     plt.savefig(path)
#     url = os.path.join(MEDIA_URL, plot_name)
#     return host + url
