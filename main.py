import values
def main():
    total_fac = int(input("How many military factories are you allocating to these divisions? "))
    div_equip = get_equip()
    equip_costs = values.init_equip_cost()
    if input("Does your division include anything created in the tank designer? (y/n) ") == "y":
        div_equip, equip_costs = get_custom(div_equip, equip_costs)
    div_costs = get_costs(div_equip, equip_costs)
    equip_ratios = get_ratios(div_costs)
    factories_needed = allocate_factories(equip_ratios, total_fac)
    output(factories_needed)
    return

# pull some user-friendly names from our values module, then output our product
def output(facs):
    names = values.get_names()
    fac_names = {}
    for item in facs:
        if item in names:
            fac_names.update({names[item]: facs[item]})
        else: # tank designer stuff already has user friendly names (see get_equip() below to see why the other stuff doesn't)
            fac_names.update({item: facs[item]})
    print("===== Your factories should be allocated as follows =====")
    for fac in fac_names:
        print(f"{round(fac_names[fac], 1)} factories producing {fac}.")
    print("\nThese obviously aren't whole numbers.\nI recommend rounding down for basic stuff that can be easily bought/captured and rounding up for fancy stuff that can be easily sold/kept in reserve.\nGood luck.")
    return

# multiply ratio by our quantity of factories and build a new dictionary out of it, ez pz
def allocate_factories(ratios, facs):
    fac_needed = {}
    for item in ratios:
        fac_needed.update({item: (ratios[item] * facs)})
    return fac_needed

# get the sum cost for one division, then divide each item's cost to get the ratio of factories we need
def get_ratios(costs):
    total_cost = 0.0
    for item in costs:
        total_cost += costs[item]
    ratios = {}
    for item in costs:
        ratios.update({item: (costs[item] / total_cost)})
    return ratios

# iterate through the dict of equipment we've been building and multiply the values corresponding in the cost dict from values.py
def get_costs(equip, costs):
    output = {}
    for item in equip:
        output.update({item: (equip[item] * costs[item])})
    return output

# iterate through tank designer equipment *by role*, updating both the cost dictionary and the division dictionary as needed
def get_custom(div, costs):
    print("Does your division include custom vehicles of any of the following roles?")
    roles = values.init_designed_vehicles()
    for role in roles:
        r = (input(f"{role}? (y/n) "))
        if r == "y":
            q = int(input("How many? "))
            c = float(input("How much does each cost? "))
            div.update({role: q})
            costs.update({role: c})
    return div, costs


# find out what we're building
def get_equip():
    div_equip = {}

    inf_needed = int(input("How much infantry equipment does your division need? "))
    if inf_needed > 0:
        print("Select type of equipment to be produced...\n0: Basic\n1: Inf Equipment 1\n2: Inf Equipment 2\n3: Inf Equipment 3")
        r = input() # we can just plug the user's input directly into the dictionary key string to record what level of equipment we're building!
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