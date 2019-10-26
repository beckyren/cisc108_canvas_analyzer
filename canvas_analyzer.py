import canvas_requests


"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment(except from Dr. Bart who has been patient thus far with
every little things I've asked help on."
author: Becky Ren
"""
__version__ = 7
def main(user_name):
    print_user_info(canvas_requests.get_user("hermione"))
    filter_available_courses(canvas_requests.get_courses('hermione'))
    print_course(filter_available_courses(canvas_requests.get_courses('hermione')))
    get_course_ids(canvas_requests.get_courses('hermione'))
    #choose_course(get_course_ids(canvas_requests.get_courses('hermione')))
    summarize_points(canvas_requests.get_submissions('hermione', 52))
    summarize_groups(canvas_requests.get_submissions('hermione',52))
    plot_scores(canvas_requests.get_submissions('hermione',52))


# 1) main
# 2) print_user_info
def print_user_info(a_dict):
    string_I_need="{'lti_user_id': None, 'sis_user_id': None, 'avatar_url': " \
                  "'https://i.imgur.com/gaNCiuW.png', 'calendar': None, 'login_id': " \
                  "'hgranger@hogwarts.edu', 'locale': None, 'title': 'Student', 'short_name': 'Hermione Granger', " \
                  "'time_zone': 'Europe/London', 'name': 'Hermione Granger', 'id': 42, 'primary_email': 'hgranger@hogwarts.edu'," \
                  " 'bio': 'Interested in Magic, Learning, and House Elf Rights', 'sortable_name': 'granger, hermione'}"

    print ("Name: "+ a_dict['short_name']+"\n"
           "Title: "+a_dict['title']+"\n"
           "Primary Email: "+a_dict['login_id']+"\n"
           "Bio: "+ a_dict['bio'])

def filter_available_courses(course_list:[dict])->[dict]:
    new_list=[]
    for dictionary in course_list:
        if dictionary['workflow_state']=='available':
            new_list.append(dictionary)
    return new_list

def print_course(course_list:[dict])->str:
    for dictionary in course_list:
        print(str(dictionary['id']) +' : ' + str(dictionary['name']))

def get_course_ids(course_list:[dict])->[int]:
    new_list=[]
    for dictionary in course_list:
        new_list.append(dictionary['id'])

    return new_list
"""You are here trying to figure out why the returns aten't showing even though printing shows it works
Skip this for now and try to get the other functions written"""
def choose_course(course_list:[int])->int:
    course=0
    while int(course) not in course_list :
        course=input("Hello user, please return one of your course IDs")
        """Need to fix for when string is entered"""
    return int(course)
def summarize_points(submissions:[dict]):
    points_possible=0
    points_obtained=0
    for dictionary in submissions:
        if dictionary['score']!=None:
            points_obtained += dictionary['score']*dictionary['assignment']['group']['group_weight']
            points_possible += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                'group_weight']
    print("Points possible so far: "+str(points_possible))
    print("Points obtained: "+str(points_obtained))
    print("Current grade: "+str(round((points_obtained/points_possible)*100)))

def summarize_groups(submissions:[dict]):
    group1=0
    group2=0
    group3=0
    group4=0
    points_possible=0
    points_obtained=0
    points2_obtained=0
    points2_possible=0
    points3_obtained=0
    points3_possible=0
    points4_obtained=0
    points4_possible=0
    for dictionary in submissions:
        if dictionary['assignment']['group']['name'] == "Class Activities":
            if dictionary['score'] != None:
                points_obtained += dictionary['score'] * dictionary['assignment']['group']['group_weight']
                points_possible += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                    'group_weight']
                group1 = round((points_obtained / points_possible) * 100)
        if dictionary['assignment']['group']['name'] == "Discussion Forums":
            if dictionary['score'] != None:
                points2_obtained += dictionary['score'] * dictionary['assignment']['group']['group_weight']
                points2_possible += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                    'group_weight']
                group2 = round((points2_obtained/points2_possible) * 100)
        if dictionary['assignment']['group']['name'] == "Learning Quizzes":
            if dictionary['score'] != None:
                points3_obtained += dictionary['score'] * dictionary['assignment']['group']['group_weight']
                points3_possible += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                    'group_weight']
                group3 = round((points3_obtained / points3_possible) * 100)
        if dictionary['assignment']['group']['name'] == "Programming Problems":
            if dictionary['score'] != None:
                points4_obtained += dictionary['score'] * dictionary['assignment']['group']['group_weight']
                points4_possible += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                    'group_weight']
                group4 = round((points4_obtained/points4_possible) * 100)
    print(group1)
    print(group2)
    print(group3)
    print(group4)
def plot_scores(submissions:[dict]):
    points=0
    new_list=[]
    for dictionary in submissions:
        if dictionary['score'] != None and dictionary['assignment']['points_possible']:
            points= round((dictionary['score']*100)/dictionary['assignment']['points_possible'],2)
            new_list.append(points)

    print (new_list)

"""you can set a variable equal to a value but that value is used as a key"""
'''set two dictionaries equal to each other see if changing onen chganges the other'''
'''side eddects-modifying a list, etc
Student=some dictionary with aformat
other list is made following dictionary format can be used in a function that takes in a student dictionaty'''
'''is type dictionary [student] or{student}'''







# 3) filter_available_courses
# 4) print_courses
# 5) get_course_ids
# 6) choose_course
# 7) summarize_points
# 8) summarize_groups
# 9) plot_scores
# 10) plot_grade_trends

# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')
print(filter_available_courses(canvas_requests.get_courses('hermione')))
"""I think this is the reason why your thing is printinh put while every other function is not printing"""
print(canvas_requests.get_submissions('hermione',52))