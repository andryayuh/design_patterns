"""
- directly instantiating an object causes dependency on its concrete class
- dependency inversion principle - depend upon abstractions not concrete classes
    - higher and lower level components should depnd on abstractions
    PizzaStore
        |
        |
        V
        Pizza
    ^           ^
    |           |
    |           |
    |       ChicagoStyleVeggiePizza
    NYStyleCheesePizza
"""