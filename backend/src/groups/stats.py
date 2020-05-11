def avg_points_for_what(data, mark_names):
    result = {}
    for name in mark_names:
        sum = 0
        students_num = 0
        for elem in data:
            if elem['for_what'] == name:
                sum += elem['value']
                students_num += 1
        result[str(name)] = (sum / students_num) if students_num != 0 else 0.0

    return result


def avg_points_all_students(data):
    sum = 0
    for marks_list in data:
        for elem in marks_list:
            if 'value' in elem:
                sum += elem['value']
    return sum / len(data)
