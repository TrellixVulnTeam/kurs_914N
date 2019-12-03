class mt:
    result_word = str()     # результирующее слово
    amount_of_steps = 0     # кол-во шагов для достижения целей
    tuple_alfabet = ('a', 'b', 'c')     # кортеж с литерами принадлежащим алфавиту
    state = 1     # номер состояния, 2, 3 и т.д, позже first_condition , second,
                  # тем самым меняя указатели на функции
    direction = '>'         # направление, в которое двигаемся , может быть >, <, stop
    letter = '1'            # буква, которую мы сейчас рассматриваем
    cursor = 1              # курсор , то что бегает по строке
    second_ribbon = str()

    all_new_letter = ('!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*')   # дополнительный алфавит который я добавил

    def first_condition(self, multitape):
        """
            Функция состояния, условие - что делаем с символом на котором стоит,
            пример :
                if self.letter == '1':       # если заданный символ один (функция получает символ)
                    self.letter = '0'       # меняем букву, если прописано, то изменяем если не прописано то остается как было

                    self.direction = '>'    # изменяем направление движения, если прописано то изменяем, если нет, то остается как и было

                    self.number_of_state = self.second_condition            # в какое состояние переходим, 1 - функция называет first, 2 - second,
                                                                       # сколько состояний столько и методов состояний
                                                                       # если прописано, то изменяем если не прописано то остается как было

            Порядок именно такой, вначале идут то что меняется 100% и на что, допустим direction = '>' ,
            и только потом то, что меняется в зависимости от литеры.
        """
        pass

    def second_condition(self, multitape):
        pass

    def third_condition(self, multitape):
        pass

    def fourth_condition(self, multitape):
        pass

    def fifth_condition(self, multitape):
        pass

    def sixth_condition(self, multitape):
        pass

    def seventh_condition(self, multitape):
        pass

    def eighth_condition(self, multitape):
        pass

    def ninth_condition(self, multitape):
        pass

    def tenth_condition(self, multitape):
        pass

    def heart(self, word, cursor, bot, multitape):
        """
            Сердце машины, то есть её работа, всё прописано тут, как она идет по состояниям, что возвращаем и т.д.

            Подробное описание:
                    При передачи слова в данную функцию, мы ставим текущее состояние на первое
                (меняем указатель переменной на функцию первого состояни), ставим головку в
                нужное место (курсор), далее преобразуем слово которое ввел пользователь
                из строки в список, для того чтоб можно было изменять в нем элементы, ибо
                строки в Python константны.
                    После всех приготовлений, переходим в цикл, который и будет выполнять
                всю работу по перемещению головки и захода в состояния.
                    Вначале мы берем из списка литеру на которой стоит головка(курсор),
                если не получается это сделать(ошибка) то это скорее всего из-за того что мы
                вышли за прописанные пределы (по умолчанию, слово веденное пользователем обрамляеся
                двумя L слева и справа, иногда требуется дойти до константы дальше, и для этого придумано
                выкидывание исключения, и если это произошло, просто добавляем константу L в конец списка,
                ВОЗМОЖНО кастыль:( ). После того как взяли нужную литеру переходи в состояние, на котором
                стоим, в нем проделываем нужные махинации и возвращаемся сюда. Тут, меняем литеру если её
                изменяли в состоянии, и с помозью условия и проверки переменной self.direction двигаемся
                либо, вправо влево, или останавливаемся, движения происходят увеличением или уменьшением
                переменной self.cursor. Если мт закончила свою работу, удаляем лишние L из списка,
                преобразовываем список в строку и возвращаем новое слово.
        """
        self.state = self.first_condition     # привязываем первое состояние к номеру состояния,
                                              # или же на каком состоянии мы стартуем
        self.cursor = cursor    # с какой позиции стартовать, мт не всегда стартует с первой позиции
        word = list(word)   # преобразуем строку в список
        while True:     # бесконечный цикл, это и есть некая головка, которая будет ходить по литерам
            self.amount_of_steps += 1

            try:
                self.letter = word[self.cursor]      # получаем литеру на которой стоит головка
            except IndexError:  # если произошел выход за строку
                word.append('L')

            self.state()      # проводим определенные операции с этой литерой
            word[self.cursor] = self.letter     # меняем символ который заменили в состоянии

            # записываем логи в файлы
            if bot is False:    # если пользователь ввёл слово, записываем логи
                if multitape is True:   # для многоленточной
                    with open('multitape_log.txt', 'a') as f:
                        to_file = '\n\n' + str(self.amount_of_steps) + '\t' + ''.join(word) + '\n'
                        if self.second_ribbon:
                            to_file += '\t' + self.second_ribbon
                        else:
                            to_file += '\tL'
                        f.write(to_file)
                else:   # для одноленточной
                    with open('log.txt', 'a') as f:
                        f.write('\n\n' + str(self.amount_of_steps) + '\t' + ''.join(word) + '\n')

            # двигаемся в какую-либо сторону
            if self.direction == '>':
                self.cursor += 1
            elif self.direction == '<':
                self.cursor -= 1
            else:   # если self.direction == 'stop', останавливаем машину
                self.result_word = ''.join(word).replace('L', '')   # выходим из машины, соединяем полученное на выходе слово в строку и чистим от L
                return
