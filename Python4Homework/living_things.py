class LivingThing:
    def __init__(self, sci_name, habitat):
        self.habitat = habitat
        self.sci_name = sci_name

    def set_habitat(self, habitat):
        self.habitat = habitat

    def get_habitat(self):
        return self.habitat

    def get_name(self):
        return self.sci_name


class Animal(LivingThing):
    def __init__(self, sci_name, habitat, is_carnivore):
        super().__init__(habitat, sci_name)
        self.is_carnivore = bool(is_carnivore)

    def get_is_carnivore(self):
        return self.is_carnivore


class Wolf(Animal):
    def __init__(self, sci_name, habitat, is_carnivore, pack_leader_no):
        super().__init__(sci_name, habitat, is_carnivore)
        self.pack_leader = pack_leader_no

    def get_pack_leader(self):
        return self.pack_leader


class Caribou(Animal):
    def __init__(self, sci_name, habitat, is_carnivore):
        super().__init__(sci_name, habitat, is_carnivore)


class Plant(LivingThing):
    def __init__(self, sci_name, habitat):
        super().__init__(sci_name, habitat)


class Flower(Plant):
    def __init__(self, sci_name, habitat, colour):
        super().__init__(sci_name, habitat)
        self.colour = colour

    def get_colour(self):
        return self.colour


class Dandelion(Flower):
    def __init__(self, sci_name, habitat, colour):
        super().__init__(sci_name, habitat, colour)

    def grow(self):
        if self.colour == "Yellow":
            self.colour = "White"
            return self.colour

        elif self.colour == "White":
            self.colour = "Green"
            return self.colour

        elif self.colour == "Green":
            self.colour = "Yellow"
            return self.colour

        else:
            return "Dunno"

    def blow(self):
        if self.colour == "White":
            self.colour = "Green"
            return self.colour
        else:
            return "Not ready"


class Rose(Flower):
    def __init__(self, sci_name, habitat, colour, thorns):
        super().__init__(sci_name, habitat, colour)
        self.thorns = bool(thorns)

    def get_thorns(self):
        return self.thorns


class Tree(Plant):
    def __init__(self, sci_name, habitat, no_branches):
        super().__init__(sci_name, habitat)
        self.no_branches = no_branches

    def grow(self, new_branches):
        self.no_branches += new_branches

    def cut(self, cut_branches):
        if self.no_branches-cut_branches >= 0:
            self.no_branches -= cut_branches
        else:
            print("No more branches")

    def get_no_branches(self):
        return self.no_branches


class Maple(Tree):
    def __init__(self, sci_name, habitat, no_branches):
        super().__init__(sci_name, habitat, no_branches)
