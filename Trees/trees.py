class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        g_l = self.get_level()
        prefix = (g_l*3)*" "+"|---" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        l = 0
        p = self.parent
        while p:
            l += 1
            p = p.parent
        return l


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("TUF Gaming"))
    laptop.add_child(TreeNode("Surface 8 Pro"))
    laptop.add_child(TreeNode("ROG"))

    mobile = TreeNode("Mobiles")
    mobile.add_child(TreeNode("IQOO 7"))
    mobile.add_child(TreeNode("Xiaomi 6"))
    mobile.add_child(TreeNode("Samsung S22 Ultra"))

    refrigerators = TreeNode("Refrigerators")
    refrigerators.add_child(TreeNode("Whirlpool"))
    refrigerators.add_child(TreeNode("Samsung"))
    refrigerators.add_child(TreeNode("Haier"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(refrigerators)
    root.print_tree()


print(build_tree())


#Q1

class TreeNode:
    def __init__(self, data, position):
        self.data = data
        self.children = []
        self.parent = None
        self.position = position

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, info):
        g_l = self.get_level()
        prefix = (g_l*3)*" "+"|---" if self.parent else ""
        if info == "name":
            print(prefix + self.data)
        elif info == "both":
            print(prefix + self.data + f" ( {self.position} )")
        elif info == "designation":
            print(prefix + self.position)
        if self.children:
            for child in self.children:
                child.print_tree(info)

    def get_level(self):
        l = 0
        p = self.parent
        while p:
            l += 1
            p = p.parent
        return l


def build_tree():
    root = TreeNode("Electronics", "CEO")

    laptop = TreeNode("Laptops", "CTO")
    laptop.add_child(TreeNode("TUF Gaming", "DEV"))
    laptop.add_child(TreeNode("Surface 8 Pro", "DEV"))
    laptop.add_child(TreeNode("ROG", "DEV"))

    mobile = TreeNode("Mobiles", "MANAGER")
    mobile.add_child(TreeNode("IQOO 7", "TESTER"))
    mobile.add_child(TreeNode("Xiaomi 6", "TESTER"))
    mobile.add_child(TreeNode("Samsung S22 Ultra", "TESTER"))

    refrigerators = TreeNode("Refrigerators", "HR")
    refrigerators.add_child(TreeNode("Whirlpool", "RECRUITER"))
    refrigerators.add_child(TreeNode("Samsung", "RECRUITER"))
    refrigerators.add_child(TreeNode("Haier", "RECRUITER"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(refrigerators)
    root.print_tree("both")


print(build_tree())
 #Q2

 class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        g_l = self.get_level()
        if g_l <= level:
            prefix = (g_l*3)*" "+"|---" if self.parent else ""
            print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def get_level(self):
        l = 0
        p = self.parent
        while p:
            l += 1
            p = p.parent
        return l


def build_tree():
    root = TreeNode("Countries")

    india = TreeNode("India")

    ts = TreeNode("Telangana")

    tn = TreeNode("Tamil Nadu")

    india.add_child(ts)
    india.add_child(tn)

    ts.add_child(TreeNode("Hyderabad"))
    ts.add_child(TreeNode("Warangal"))
    ts.add_child(TreeNode("Karimnagar"))

    tn.add_child(TreeNode("Karaikal"))
    tn.add_child(TreeNode("Madras"))
    tn.add_child(TreeNode("Salem"))

    usa = TreeNode("USA")

    ws = TreeNode("Washington")

    co = TreeNode("Colorado")

    ws.add_child(TreeNode("Telvadu"))
    ws.add_child(TreeNode("Gurtuledu"))
    ws.add_child(TreeNode("Marchipoya"))

    co.add_child(TreeNode("Boom"))
    co.add_child(TreeNode("King Kong"))
    co.add_child(TreeNode("Mission Impossible"))

    usa.add_child(ws)
    usa.add_child(co)

    root.add_child(india)
    root.add_child(usa)
    root.print_tree(0)


build_tree()
