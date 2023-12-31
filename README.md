# Тестовое Задание

## Машинное Состояние (Machine State)

### Описание задачи 

В пустом проекте реализовать паттерн "Машина состояний" ссылаясь на продукт "Авторежиссер"

Должны быть реализованы следующие классы:

State (или Scene) - абстрактный класс состояния (сцены)
Содержит некоторое поле name

Содержит список переходов типа Transition (см. п.2)

Содержит метод update(), выводящий значение поля name в консоль

Реализовать несколько наследников (например: PresentationState, AuditoryState, SpeakerState). 

В каждом из них изменить метод update() как угодно, чтоб можно было отличить какой именно класс используется
Transition - абстрактный класс перехода
Содержит поле nextState, содержащее состояние, в которое должна перейти система
Содержит метод needTransit(), возвращающий True или False в зависимости от того, нужен ли переход (в текущей реализации можно возвращать True с каким-то рандомным шансом) 

Реализовать несколько наследников (например: TimeTransition, PresentationTransition). В каждом из них изменить метод needTransit(), поменяв вероятности

StateMachine (или AutoDirector) - класс авторежиссера (самой машины состояний)

Содержит поле currentState - текущее состояние системы
Содержит метод run() - запускающий бесконечный цикл. В каждой итерации цикла нужно вызывать метод update() текущего состояния и проходиться по всем переходам текущего состояния. Если какой-либо из переходов в методе needTransit() вернул истину - сменить текущее состояние

# Как должно работать

<!-- #вставить гиф -->
![](images/anime.gif)


### Решение 

Решением является файл [main.py](main.py)

### Запуск

Для запуска необходимо выполнить команду:

```bash
git clone https://github.com/brazenoptimist/test_task.git
cd test_task
pip3 install -r requirements.txt
python3 main.py
```

P.S не судите строго это мой первый опыт работы с паттерном "Машина состояний"