class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = set()
        prereqs = set()
        prereq_map = {}
        in_degree = {}

        for course, prereq in prerequisites:
            if prereq in prereq_map.keys():
                prereq_map[prereq].append(course)
            else:
                prereq_map[prereq] = [course]
            in_degree[course] = in_degree.get(course, 0) + 1
            courses.add(course)
            prereqs.add(prereq)
        not_taken_free = courses|prereqs
        taken = [i for i in range(numCourses) if i not in not_taken_free]
        can_take = prereqs - courses
        while can_take:
            course = can_take.pop()

            taken.append(course)
            if course in prereq_map.keys():
                new_courses = prereq_map[course]
                for new_c in new_courses:
                    in_degree[new_c] -= 1
                    if in_degree[new_c] == 0:
                        can_take.add(new_c)

        if len(taken)>=numCourses:
            return taken
        else:
            return []