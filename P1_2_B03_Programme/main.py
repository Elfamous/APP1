import format
import os
import random
if __name__ == '__main__':
    filename = "QCM.txt"
    start_list = format.format(filename)
    random.shuffle(start_list)
    correction_list = []
    answer_list = []
    cotation_question = input("1. Systeme de cotation normal, 2. Systeme de cotation a point negatif : ")
    while cotation_question not in ["1", "2"]:
        cotation_question = input("Veuillez entrer une reponse valide : 1. Systeme de cotation normal, 2. Systeme de cotation a point negatif : ")
    if int(cotation_question) == 1:
        negative_point = False
    elif int(cotation_question) == 2:
        negative_point = True
    for questions in range(len(start_list)):
        print(start_list[questions][0])
        reponse = start_list[questions][1]
        correction_list.append(start_list[questions][1])
        for i, reponse in enumerate(format.format_response(reponse), 1):
            print(f"{i}. {reponse}")
        answer = input("Entrer votre reponse : ")
        answer_list.append(answer)
    print("Vous avez obtenu le score de :", format.correction(answer_list, correction_list, negative_point))
     





