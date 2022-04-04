
sequenceDiagram
    Alice->>John: Hello John, how are you?
    activate John
    John-->>Alice: Great!
    deactivate John

sequenceDiagram
    participant O as Outside
    participant M as Machine
    participant D as Drive
    participant F as FuelTank
    participant E as Engine
    O->>M: call(Machine)
    M->>F: FuelTank()
    F->>M: fill(40)
    M->>E: Engine(tank)
    D->>E: start()
    E->>F: consume(5)
    D->>E: is_running()
    E->>D: True
    D->>E: use_energy()
    E->>F: consume(10)
    D->>E: is_running()
    E->>D: True
    D->>E: use_energy()
    E->>F: consume(10)
    D->>E: is_running()
    E->>D: True
    D->>E: use_energy()
    E->>F: consume(10)
    D->>E: is_running()
    E->>D: True
    D->>E: use_energy()
    E->>F: consume(10)
    D->>E: is_running()
    E->>D: False
