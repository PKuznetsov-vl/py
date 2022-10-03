import json
import os

import PySAM.Pvwattsv8 as PVWatts
import PySAM.Grid as Grid
import PySAM.Utilityrate5 as UtilityRate
import PySAM.Thermalrate as ThermalRate
import PySAM.Battery as Batt
import PySAM.Fuelcell as Fuel
import PySAM.Cashloan as Cashloan
import PySAM.Singleowner as Single

pv = PVWatts.new()
batt = Batt.from_existing(pv)
fuelcell = Fuel.from_existing(pv)
grid = Grid.from_existing(pv)
sl = Single.from_existing(pv)
ur = UtilityRate.from_existing(pv)
tl = ThermalRate.from_existing(pv)

if __name__ == '__main__':

    jsons_path = "./jsons/"
    file_names = [f for f in os.listdir(jsons_path)
                  if os.path.isfile(os.path.join(jsons_path, f))]
    print(file_names)
    file_names = ['untitled__1__pvwattsv8.json',  'untitled__1__utilityrate5.json', 'untitled__1__singleowner.json']
    print(file_names)
    # , ,
    modules = [pv, ur, sl]

    for f, m in zip(file_names, modules):

        with open(jsons_path + f, 'r') as file:
            data = json.load(file)
            for k, v in data.items():
                if k != "number_inputs":
                    m.value(k, v)

    for m in modules:
        m.execute()
        print('ex')
print('ac_annual: ', pv.Outputs.ac_annual)
print('ur_ec_tou_mat: ', ur.ElectricityRates.ur_ec_tou_mat)
#print('cl.Outputs.npv: ', tl.Outputs.npv)
