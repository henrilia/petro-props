from petro_props.real_gas import real_gas
from petro_props.read_input import read_composition_and_props

T = float(input("T [degC] = ")) + 273
p = float(input("p [bar] = "))
filepath = input("path to excel input = ")
mw, T_c, p_c, y = read_composition_and_props(filepath)
real_gas_rho = real_gas.calculate_density(T, p, mw, T_c, p_c, y)
print(f"Real gas: rho = {real_gas_rho}")
