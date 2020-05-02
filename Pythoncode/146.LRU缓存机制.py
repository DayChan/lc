class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =  capacity
        self.key2node = {}
        self.headnode = {}
        self.headnode["value"] = None
        self.headnode["next"] = None
        self.tailnode = {}
        self.tailnode["value"] = None
        self.tailnode["prev"] = None
        self.headnode["prev"] = self.tailnode
        self.tailnode["next"] = self.headnode


    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        self.key2node[key]["prev"]["next"] = self.key2node[key]["next"]
        self.key2node[key]["next"]["prev"] = self.key2node[key]["prev"]
        self.key2node[key]["prev"] = self.headnode["prev"]
        self.key2node[key]["next"] = self.headnode
        self.headnode["prev"]["next"] = self.key2node[key]
        self.headnode["prev"] = self.key2node[key]
        return self.key2node[key]["value"]


    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            self.key2node[key]["prev"]["next"] = self.key2node[key]["next"]
            self.key2node[key]["next"]["prev"] = self.key2node[key]["prev"]
            self.key2node.pop(key)
        node = {}
        node["key"] = key
        node["value"] = value
        node["prev"] = self.headnode["prev"]
        node["next"] = self.headnode
        self.headnode["prev"]["next"] = node
        self.headnode["prev"] = node
        self.key2node[key] = node
        if len(self.key2node) > self.capacity:
            delkey = self.tailnode["next"]["key"]
            self.key2node[delkey]["prev"]["next"] = self.key2node[delkey]["next"]
            self.key2node[delkey]["next"]["prev"] = self.key2node[delkey]["prev"]
            self.key2node.pop(delkey)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

c = LRUCache(3)