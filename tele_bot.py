from Question import Question

question_promts=[
    'Когда вы рассказываете дома о своей работе, вы обычно употребляете?\n(а)безличные формы\n(б)местоимения "я" или "мы"\n\n',
    'В работе больше дорожите?\n(а)своей самостоятельностью\n(б) возможностью диалога с коллегами и руководством\n\n',
    'Если в неудачах обвиняют лично вас, вы отвечаете?\n(а) меня подвели\n(б)да, это моя ошибка\n\n',
    'Конфликты на работе\n(а) их лучше избегать\n(б) иногда они полезны для дела\n\n',
    'Если надо принять решение, вы\n(а) рассчитываете на свою интуицию\n(б) принимаете во внимание мнение окружающих\n\n',
    'Когда ваша любимая команда проигрывает\n(а) это может вывести из себя\n(б) воспринимается это спокойно\n\n',
    'На совещаниях вы\n(а) сразу и твердо отстаиваете свое мнение\n(б) сначала слушаете других\n\n',
    'Окончательное решение\n(а) может принадлежать коллективу\n(б) всегда дело одного человека\n\n',
    'Ваши коллеги\n(а) должны разделять ваши методы работы\n(б) естественно, работают каждый по-своему\n\n',
    'Как вы воспринимаете тот факт, что другие живут и думают по-иному?\n(а) с трудом\n(б) легко\n\n',
    'Когда кто-нибудь из коллег не разделяет ваше мнение, вы стараетесь его переубедить\n(а) лично\n(б) с помощью коллектива\n\n',
    'Если группа не согласна с вами, вы\n(а) присоединяетесь к большинству\n(б) чаще остаетесь на своих позициях\n\n',
    'Благоприятные климат в коллективе\n(а) определяющий фактор эффективной работы\n(б) фактор важный, но второстепенный\n\n',
    'На общих собраниях вы\n(а) стараетесь вникнуть во все обсуждаемые проблемы\n(б) интересуетесь только тем, что касается вашей группы\n\n',
    'Если решение, принятое группой, не было согласовано с вами, вы\n(а) чувствуете себя отвергнутым\n(б) испытываете раздражение\n\n',
    'Спорите ли с коллегами или с начальством, если уверены, что правы именно вы?\n(а) часто\n(б) в отдельных случаях\n\n',
    'В групповой работе вы\n(а) всегда лидер\n(б) только иногда, в зависимости от решаемой проблемы\n\n',
    'Коллектив способен решить любую задачу\n(а) всегда\n(б) во многих случаях\n\n',
    'Что вам больше нравится?\n(а) симфония\n(б) сольный концерт\n\n',
    'Для вас лучше, когда рабочая группа состоит из ваших друзей?\n(а)да\n(б) нет\n\n',
    'На совещаниях вы более склонны\n(а) стремиться сблизить различные позиции\n(б) знакомиться с новыми подходами к проблемам\n\n',
    'Вы были бы рады, если бы в вашей семье родились пять близнецов?\n(а) да\n(б) нет\n\n',
    'Тот факт, что коллегам нет необходимости обсуждать между собой стоящие задачи (каждый знает и хорошо делает свое дело), – лучший признак хорошей группы\n(а) да\n(б) нет\n\n',
    'Работа в группе – это\n(а) экономия личных усилий\n(б) их увеличение\n\n'
]
questions=[
    Question(question_promts[0], 'б'),
    Question(question_promts[1], 'б'),
    Question(question_promts[2], 'б'),
    Question(question_promts[3], 'б'),
    Question(question_promts[4], 'б'),
    Question(question_promts[5], 'б'),
    Question(question_promts[6], 'б'),
    Question(question_promts[7], 'б'),
    Question(question_promts[8], 'б'),
    Question(question_promts[9], 'б'),
    Question(question_promts[10], 'б'),
    Question(question_promts[11], 'б'),
    Question(question_promts[12], 'б'),
    Question(question_promts[13], 'б'),
    Question(question_promts[14], 'б'),
    Question(question_promts[15], 'б'),
    Question(question_promts[16], 'б'),
    Question(question_promts[17], 'б'),
    Question(question_promts[18], 'б'),
    Question(question_promts[19], 'б'),
    Question(question_promts[20], 'б'),
    Question(question_promts[21], 'б'),
    Question(question_promts[22], 'б'),
    Question(question_promts[23], 'б')
]
def run_test(questions):
    score=0
    for question in questions:
        otvet=input (question.vopros)
        if otvet== question.otvet:
            score+=1
    print ('У Вас' + str(score) + 'из'+ str (len(questions)) + 'баллов.' + 'Наш сотрудник в ближайшее время Вам перезвонит')
run_test(questions)