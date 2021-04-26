questions  = ['name','surname','age','city','fav color']
answers = ['vipul','shah',22,'delhi','red']

for q,a in zip(questions, answers) :
    print(f'what is your {q}?\n ->It is {a}')
    