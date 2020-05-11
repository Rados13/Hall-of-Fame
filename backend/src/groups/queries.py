from itertools import chain


class Querying:
    groups_objects = None
    groups_id = None

    def __init__(self, data, groups_id):
        self.groups_objects = data
        self.groups_id = groups_id

    def filter_group_list(self):
        marks = self.groups_objects.mongo_aggregate([
            {'$match': {'id': {'$in': self.groups_id}}},
            {'$project': {'marks': '$enrolled_list.marks_list'}},
            {'$unwind': '$_id'},
            {'$unwind': '$marks'},
        ])
        marks = [elem['marks'] for elem in marks]
        return list(chain.from_iterable(marks))

    def get_student_list(self):
        students = self.groups_objects.mongo_aggregate([
            {'$match': {'id': {'$in': self.groups_id}}},
            {'$project': {'students': '$enrolled_list'}},
            {'$unwind': '$_id'},
            # {'$unwind': '$students.marks_list'},
            {'$group': {'_id': '$students.user_id', 'data': {'$addToSet': '$students.marks_list'}}}
        ])
        students = [elem['data'] for elem in students]
        students =  list(chain.from_iterable(students))
        return  list(chain.from_iterable(students))

    def get_for_what_list(self):
        names = self.groups_objects.mongo_aggregate([{'$match': {'id': {'$in': self.groups_id}}},
                                                     {'$project': {'marks': '$enrolled_list.marks_list'}},
                                                     {'$unwind': '$_id'},
                                                     {'$unwind': '$marks'},
                                                     {'$group': {'_id': '$marks.for_what'}}])
        names = [elem['_id'] for elem in names]
        return list(chain.from_iterable(names))
