inp = input('Привет, здесь я приготовил краткий рассказ о своей жизни, желаешь его увидеть? :"Да" ')
MyName = 'Меня зовут Воронцов Арсений.'
mycity = 'Я живу в Великом Новгороде.'
myage = 'Мне 17 лет и в данный момент учусь в'
myStudyBuilding = 'строительном колледже.'
DopPer = 'В нашем колледже пары длятся'
lengthPair =  1.5
forLengthP = 'часа.'
turnLength = 'Перемена в колледже составляет - 10 минут, а большая - '
turnBigLength = 30
street = 'В своём городке, я живу на улице Зелинского.'
population = 'Население нашего города составляет примерно 200.000 человек.'
specialty = ' Я обучаюсь по специальности информационные системы по отраслям.'
profession = 'С самого детсва я мечтал стать программистом и по этому проблем с выбором специальности у меня не было.'
trueProfession = 'На своём данном этапе я пытаюсь разобраться и выбрать чем я именно буду заниматься в мире IT ведь выбор велик.'
goodbye = 'Спасибо за внимание!'
if inp=='Да' or inp=='да':   
    print(MyName, mycity, myage,myStudyBuilding,DopPer,lengthPair,forLengthP,'\n',turnLength,turnBigLength,'.',street,population,specialty,profession,trueProfession,goodbye )
else:
    print("Ваш выбор :)")