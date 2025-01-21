from oxrse_unit_conv.si import *
from oxrse_unit_conv.meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)

# meter_sq
kilometer_sq = Unit(name='kilometer_sq', abbr='km_sq', si=meter_sq, to_si_fun=lambda n: n * 1_000_000)
km_sq = kilometer_sq

# meter_cu
kilometer_cu = Unit(name='kilometer_cu', abbr='km_cu', si=meter_cu, to_si_fun=lambda n: n * 1_000_000_000)
km_cu = kilometer_cu
# kilogram

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# ampere

# kelvin

# mole

# candela
