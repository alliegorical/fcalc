def init_equip_cost():
    equip_cost = {
        "inf0": 0.43,
        "inf1": 0.5,
        "inf2": 0.58,
        "inf3": 0.69,
        "truck": 2.5,
        "ac0": 4.0,
        "ac1": 6.0,
        "ac2": 8.0,
        "ac3": 9.0,
        "mrart": 12.0,
        "mech1": 8.0,
        "mech2": 10.0,
        "mech3": 12.0,
        "amech1": 8.0,
        "amech2": 10.0,
        "art1": 3.5,
        "art2": 4.0,
        "art3": 4.5,
        "rart1": 4.0,
        "rart2": 5.0,
        "at1": 4.0,
        "at2": 5.0,
        "at3": 6.0,
        "aa1": 4.0,
        "aa2": 5.0,
        "aa3": 6.0,
        "supp": 4.0
    }
    return equip_cost

def get_names():
    names = {
        "inf0": "Basic Infantry Equipment",
        "inf1": "Infantry Equipment 1",
        "inf2": "Infantry Equipment 2",
        "inf3": "Infantry Equipment 3",
        "truck": "Motorized",
        "ac0": "Interwar Armored Car",
        "ac1": "Basic Armored Car",
        "ac2": "Improved Armored Car",
        "ac3": "Anti-Tank Armored Car",
        "mrart": "Motorized Rocket Artillery",
        "mech1": "Mechanized Equipment 1",
        "mech2": "Mechanized Equipment 2",
        "mech3": "Mechanized Equipment 3",
        "amech1": "Basic Amphibious Tractor",
        "amech2": "Improved Amphibious Tractor",
        "art1": "Towed Artillery",
        "art2": "Improved Artillery",
        "art3": "Advanced Artillery",
        "rart1": "Towed Rocket Artillery",
        "rart2": "Advanced Rocket Artillery",
        "at1": "Towed Anti-Tank",
        "at2": "Improved Anti-Tank",
        "at3": "Advanced Anti-Tank",
        "aa1": "Towed Anti-Air",
        "aa2": "Improved Anti-Air",
        "aa3": "Advanced Anti-Air",
        "supp": "Support Equipment"
    }
    return names

def init_designed_vehicles(): #don't think i'll need this...
    designs = [
        "Light Tank",
        "Medium Tank",
        "Heavy Tank",
        "Modern Tank",
        "Amphibious Tank",
        "Tank Destroyer",
        "Self Propelled Artillery",
        "Self Propelled Anti-Air",
        "Flame Tank"
    ]
    return designs