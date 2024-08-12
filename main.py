import values
def main():
    total_fac = int(input("How many military factories are you allocating to these divisions? "))
    div_equip = get_equip()
    equip_costs = get_costs(div_equip)
    equip_ratios = get_ratios(equip_costs)
    factories_needed = allocate_factories(equip_ratios, total_fac)
    output(factories_needed)
    return

def output(facs):
    print("Your factories should be allocated as follows...")
    for fac in facs:
        print(f"{round(facs[fac], 1)} factories producing {fac}.")
    print("Good luck.")
    return


def allocate_factories(ratios, facs):
    fac_needed = {}
    for item in ratios:
        fac_needed.update({item: (ratios[item] * facs)})
    return fac_needed


def get_ratios(costs):
    total_cost = 0.0
    for item in costs:
        total_cost += costs[item]
    ratios = {}
    for item in costs:
        ratios.update({item: (costs[item] / total_cost)})
    return ratios


def get_costs(equip):
    costs = values.init_equip_cost()
    output = {}
    for item in equip:
        output.update({item: (equip[item] * costs[item])})
    return output


def get_equip():
    div_equip = {}

    inf_needed = int(input("How much infantry equipment does your division need? "))
    if inf_needed > 0:
        print("Select type of equipment to be produced...\n0: Basic\n1: Inf Equipment 1\n2: Inf Equipment 2\n3: Inf Equipment 3")
        r = input()
        div_equip.update({f"inf{r}": inf_needed})
    
    trucks_needed = int(input("How many trucks does your division need? "))
    if trucks_needed > 0:
        div_equip.update({"truck": trucks_needed})
    
    ac_needed = int(input("How many armored cars does your division need? "))
    if ac_needed > 0:
        print("Select type of armored car to be produced...\n0: Inter-War Armored Car\n1: Basic Armored Car 2\n2: Improved Armored Car\n3: Anti-Tank Armored Car")
        r = input()
        div_equip.update({f"ac{r}": ac_needed})
    
    mrart_needed = int(input("How much motorized rocket artillery does your division need? "))
    if mrart_needed > 0:
        div_equip.update({"mrart": mrart_needed})
    
    mech_needed = int(input("How much mechanized does your division need? "))
    if mech_needed > 0:
        print("Select type of mech to be produced...\n1: Mechanized Equipment 1\n2: Mechanized Equipment 2\n3: Mechanized Equipment 3")
        r = input()
        div_equip.update({f"mech{r}": mech_needed})
    
    amech_needed = int(input("How much amphibious mech does your division need? "))
    if amech_needed > 0:
        print("Which kind of amtrack are you building?\n1: Basic Amphibious Tractor\n2: Improved Amphibious Tractor")
        r = input()
        div_equip.update({f"amech{r}": amech_needed})
    
    art_needed = int(input("How much artillery does your division need? "))
    if art_needed > 0:
        print("Which kind of artillery?\n1: Artillery\n2: Improved Artillery\n3: Advanced Artillery")
        r = input()
        div_equip.update({f"art{r}": art_needed})

    rart_needed = int(input("How much rocket artillery does your division need? "))
    if rart_needed > 0:
        print("Which kind of rocket artillery?\n1: Rocket Artillery\n2: Advanced Rocket Artillery")
        r = input()
        div_equip.update({f"rart{r}": rart_needed})
    
    at_needed = int(input("How much anti-tank does your division need? "))
    if at_needed > 0:
        print("Which kind of anti-tank?\n1: Anti-Tank\n2: Improved Anti-Tank\n3: Advanced Anti-Tank")
        r = input()
        div_equip.update({f"at{r}": at_needed})
    
    aa_needed = int(input("How much anti-air does your division need? "))
    if aa_needed > 0:
        print("Which kind of anti-air?\n1: Anti-Air\n2: Improved Anti-Airk\n3: Advanced Anti-Air")
        r = input()
        div_equip.update({f"aa{r}": aa_needed})
    
    supp_needed = int(input("How much support equipment does your division need? "))
    if supp_needed > 0:
        div_equip.update({"supp": trucks_needed})
    
    return div_equip


main()