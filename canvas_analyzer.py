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

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 7
def main(user_name):
    print_user_info(canvas_requests.get_user("hermione"))

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
    #return dictionary.items()
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
