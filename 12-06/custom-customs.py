

f = open("input.txt", "r")
#question_answers = [False]*26
question_answers = [True]*26
output_sum = 0
for x in f:
    if x == '\n':
        output_sum += len(list(filter(lambda a: a,question_answers)))
        question_answers = [True]*26
    else:
        #for idx, char in enumerate(x.strip()):
        #    question_answers[ord(char) - 97] = True
        for c in range(97,123):
            if chr(c) not in x:
                question_answers[c - 97] = False
output_sum += len(list(filter(lambda a: a,question_answers)))
print(output_sum)



