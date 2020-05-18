import matplotlib.pyplot as plt
from HallOfFame.settings import MEDIA_ROOT, os, MEDIA_URL
import socket


def avg_points_for_what(data, mark_names):
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

    return result


def avg_points_all_students(data):
    sum = 0
    max_points = 0
    for marks_list in data:
        for elem in marks_list:
            if 'value' in elem:
                sum += elem['value']
                max_points += elem['max_points']

    return {'val': sum / len(data), 'max_points': max_points / len(data)}


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
    print(data)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    whats = list(data.keys())
    values = [elem['val'] for elem in data.values()]
    max_points = [elem['max_points'] for elem in data.values()]
    diffrences = [max_points[i] - values[i] for i in range(len(values))]
    print(whats, "   ", values, "   ", max_points)
    ax.bar(whats, values, color='b')
    ax.bar(whats, diffrences, bottom=values, color='r')
    ax.set_title("Stat per group")
    plot_name += '.png'
    path = os.path.join(MEDIA_ROOT, plot_name)
    plt.savefig(path)
    url = os.path.join(MEDIA_URL, plot_name)
    return host + url
