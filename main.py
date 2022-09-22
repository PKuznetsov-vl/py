import json
import PySAM.Pvwattsv8 as PVWatts
import PySAM.Grid as Grid
import PySAM.Utilityrate5 as UtilityRate
import PySAM.Thermalrate as ThermalRate
import PySAM.Battery as Batt
import PySAM.Fuelcell as Fuel
import PySAM.Cashloan as Cashloan
import PySAM.Singleowner as Single

pv = PVWatts.new()
grid = Grid.from_existing(pv)
ur = UtilityRate.from_existing(pv)
cl = Single.from_existing(pv)


if __name__ == '__main__':
    print('tst')
    # dir = "./jsons"
    file_names = ["untitled_1_battery", "untitled_1_grid", "untitled_1_utilityrate5", "untitled_1_thermalrate"]
    modules = [pv, grid, ur, cl]

    for f, m in zip(file_names, modules):
        print('try')
        with open(dir + f + ".json", 'r') as file:
            data = json.load(file)
            for k, v in data.items():
                if k != "number_inputs":
                    m.value(k, v)

    for m in modules:
        m.execute()
        print('ex')
