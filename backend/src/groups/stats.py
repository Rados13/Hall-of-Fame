def avg_points_for_what(data, mark_names):
    result = {}
    max_points = 0
    for name in mark_names:
        sum = 0
        students_num = 0
        for elem in data:
            if elem['for_what'] == name:
                sum += elem['value']
                students_num += 1
                if 'max_points' in elem and str(name) not in result:
                    result[str(name)] = {'max_points': elem['max_points']}
                    print(result)
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


