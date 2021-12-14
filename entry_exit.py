input = [['rohit', 'exit'],
         ['manish', 'entry'],
         ['rakesh', 'entry'],
         ['rakesh', 'entry'],
         ['manish', 'exit'],
         ['rakesh', 'exit']]



from collections import defaultdict


def check_entry_exit(input):

    if not input:
        return [], []

    emp_dict = defaultdict(list)
    exit_issue = []
    entry_issue = []

    for emp, action in input:
        
        if emp not in emp_dict:
            emp_dict[emp].append(action)
        
        elif action == 'exit' and emp_dict[emp][-1] == 'entry':
            print("---", emp_dict[emp])
            emp_dict[emp].pop()

        else:
            emp_dict[emp].append(action)
    
    for emp, actions in emp_dict.items():

        print(emp, actions)
        if not actions:
            continue
        if 'entry' in actions:
            entry_issue.append(emp)
        if 'exit' in actions:
            exit_issue.append(emp)

    return entry_issue, exit_issue



print(check_entry_exit(input))

    


    