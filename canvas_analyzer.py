import canvas_requests
import datetime
import matplotlib.pyplot as plt
import numpy as np


"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment(except from the person who made this rule)."
author: Becky Ren
"""
__version__ = 7
def main(user_name):
    print_user_info(canvas_requests.get_user(user_name))
    filter_available_courses(canvas_requests.get_courses(user_name))
    print_courses(filter_available_courses(canvas_requests.get_courses(user_name)))
    get_course_ids(canvas_requests.get_courses(user_name))
    thing=choose_course(get_course_ids(canvas_requests.get_courses(user_name)))
    summarize_points(canvas_requests.get_submissions(user_name,thing ))
    summarize_groups(canvas_requests.get_submissions(user_name,thing))
    plot_scores(canvas_requests.get_submissions(user_name,thing))
    plot_grade_trends(canvas_requests.get_submissions(user_name,thing))
'''3) filter_available_courses
# 4) print_courses
# 5) get_course_ids
# 6) choose_course
# 7) summarize_points
# 8) summarize_groups
# 9) plot_scores
# 10) plot_grade_trends'''

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

def print_courses(course_list:[dict])->str:
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
    thing=["Lab","Practical","Project","Quiz","Class Activities","Discussion Forums","Learning Quizzes",
           "Programming Problems"]
    for portion in thing:
        points_obtained=0
        points_possible=0
        group1=0
        for dictionary in submissions:
            if dictionary['assignment']['group']['name'] ==portion:
                if dictionary['score'] != None:
                    points_obtained += dictionary['score'] * dictionary['assignment']['group']['group_weight']
                    points_possible += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                        'group_weight']
                    group1 = round((points_obtained / points_possible) * 100)
        print("* "+portion+" : "+str(group1))



def plot_scores(submissions:[dict]):
    points=0
    new_list=[]
    for dictionary in submissions:
        if dictionary['score'] != None and dictionary['assignment']['points_possible']:
            points= round((dictionary['score']*100)/dictionary['assignment']['points_possible'],2)
            new_list.append(points)
    #print (new_list)
    plt.hist(new_list)
    plt.xlabel('Grades')
    plt.ylabel('Number of Assignments')
    plt.title('Distribution of Grades')
    plt.show()



def plot_grade_trends(submissions:[dict]):
    '''a_string_date = "2017-08-30T16:20:00Z"
    due_at = datetime.datetime.strptime(a_string_date, "%Y-%m-%dT%H:%M:%SZ")'''
    total_points=0
    points_obtained=0
    points2_obtained=0
    points3_obtained=0
    empty_list = []
    list1=[]
    list2=[]
    list3=[]

    for dictionary in submissions:
        total_points += dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
            'group_weight']
        a_string_date=dictionary['assignment']['due_at']
        due_at= datetime.datetime.strptime(a_string_date, "%Y-%m-%dT%H:%M:%SZ")
        empty_list.append(due_at)#might need to exclude str in actual graphing
    #for calculating the lists of scores, you are keeping a running total for the percentage of the grades so far
    #score*weight gives the numberator but you need total points from both graded and ungraded assignments
    for dictionary in submissions:
        points3_obtained+=dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                    'group_weight']
        list3.append(round((points3_obtained/total_points)*100,2))
        if dictionary['score']!=None:
            points_obtained+=dictionary['score'] * dictionary['assignment']['group']['group_weight']
            points2_obtained+=dictionary['score'] * dictionary['assignment']['group']['group_weight']
            list1.append(round((points_obtained/total_points)*100,2))
            list2.append(round((points2_obtained/total_points)*100,2))


        else:
            points_obtained+=dictionary['assignment']['points_possible'] * dictionary['assignment']['group'][
                    'group_weight']
            points2_obtained+=0
            list1.append((round((points_obtained/total_points)*100,2)))
            list2.append(round((points2_obtained/total_points)*100,2))
    plt.ylabel('Grade')
    plt.title('Grade Trend')
    #plt.xticks(np.arange(len(empty_list)),empty_list, rotation=90)

    plt.plot(empty_list, list1, label="Highest")
    plt.plot(empty_list, list2, label="Lowest")
    plt.plot(empty_list, list3, label="Maximum")
    plt.legend()
    plt.show()
    '''print(empty_list)
    print(list1)
    print(list2)
    print(list3)'''




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
    #main('ron')
    #main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')



