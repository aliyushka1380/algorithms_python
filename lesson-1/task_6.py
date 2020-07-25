"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:
    def __init__(self):
        self.user_tasks = []
        self.unresolved_tasks = []
        self.resolved_tasks = []
        self.current_tasks = []

    def is_empty(self):
        return self.user_tasks == []

    def to_queue(self, item):
        self.user_tasks.insert(0, item)

    def resolve_task(self, item):
        self.resolved_tasks.insert(0, item)

    def to_unresolved(self, item):
        self.unresolved_tasks.insert(0, item)

    def size(self):
        return len(self.user_tasks)

    def from_task(self):
        return self.user_tasks.pop()

    def from_resolved(self):
        return self.resolved_tasks.pop()

    def show_tasks_resolved(self):
        return self.resolved_tasks

    def to_current(self, item):
        self.current_tasks.insert(0, item)


    def my_actions(self):
        print('Команды: 1 - Задача решена, 2 - Отправить на доработку, 3 - Оставить в списке задач')
        count = 1
        while len(self.user_tasks) != 0:
            actual_task = self.from_task()
            print(f"Задача {count} - {actual_task}")

            command = int(input('Введите команду: '))
            if command == 1:
                self.resolve_task(actual_task)
            elif command == 2:
                self.to_unresolved(actual_task)
            else:
                self.to_current(actual_task)
            count += 1
            print(f"Количество непросмотренных задач - {len(self.user_tasks)}")


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('Приготовить ужин')
    qc_obj.to_queue('Помыть полы')
    qc_obj.to_queue('Пересадить цветы')
    qc_obj.to_queue('Протереть пыль')

    print(qc_obj.is_empty())  # -> False. Очередь пустая

    print(qc_obj.size())  # -> 4
    print(f'Все задачи: {qc_obj.user_tasks}')

    print(qc_obj.my_actions())

    print(f'Текущие задачи: {qc_obj.current_tasks}')
    print(f'Задачи на доработку :{qc_obj.unresolved_tasks}')
    print(f'Решенные задачи: {qc_obj.resolved_tasks}')