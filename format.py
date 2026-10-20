import os
import random
os.chdir(os.path.dirname(__file__))
def format(filename):
    final_format = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            line = line.strip().split("|")
            if line[0] == "Q":
                final_format.append([line[1], []])
            elif line[0] == "A":
                final_format[-1][1].append(line[1:])
    return final_format

def format_response(list):
    list_of_reponse = []
    for i in range(len(list)):
        list_of_reponse.append(list[i][0])
    return list_of_reponse

def correction(answer_list, correction_list, negative_point):
    correct_answer = []
    note = 0
    for question in correction_list:
        correct_for_this_question = []
        for i in range(len(question)):
            if question[i][1] == 'V':
                correct_for_this_question.append(i + 1)
        correct_answer.append(correct_for_this_question)
    if not negative_point:
        for i in range(len(answer_list)):
            if int(answer_list[i]) in correct_answer[i]:
                note += 1
    elif negative_point:
        for i in range(len(answer_list)):
            if int(answer_list[i]) in correct_answer[i]:
                note += 1
            elif int(answer_list[i]) == 0:
                note = note
            else:
                note -= 1
    return note 


            

