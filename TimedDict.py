import threading
import time


class Node:
    def __init__(self, key, time):
        self.key = key
        self.time = time
        self.prev = self.next = None


class HandleQueue(threading.Thread):
    def __init__(self, timedDict):
        super(HandleQueue, self).__init__()
        self.TimedDict = timedDict

    def run(self):
        while self.TimedDict.start.next != self.TimedDict.end:
            cur = time.time()
            if cur - self.TimedDict.start.next.time > self.TimedDict.time:
                self.TimedDict.delete(self.TimedDict.start.next.key)
            if self.TimedDict.start.next != self.TimedDict.end:
                time.sleep(min(0.25, max(0, self.TimedDict.time - (cur - self.TimedDict.start.next.time))))
            if not threading.main_thread().is_alive():
                break


class TimedDict:

    def __init__(self, time=100):
        self.time = time
        self.dic = {}  # key, (val, node())
        self.start = Node(-1, 0)
        self.end = Node(-1, 0)
        self.start.next = self.end
        self.end.prev = self.start
        self.__handleQueue = HandleQueue(self)

    def __len__(self):
        return len(self.dic)

    def __repr__(self):
        output = ['{']
        beg = self.start.next
        while beg != self.end:
            output.append(str(f'{beg.key.__repr__()}: {self.dic[beg.key][0].__repr__()}, '))
            beg = beg.next
        if len(output) > 1:
            output[-1] = output[-1][:-2]
        output.append('}')
        return ''.join(output)

    def __contains__(self, item):
        return item in self.dic

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.dic.get(item, (None, ))[0]

    def delete(self, key):
        if key in self.dic:
            node = self.dic[key][1]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.dic[key]

    def put(self, key, val):
        if key in self.dic:
            self.delete(key)
        node = Node(key, time.time())
        self.dic[key] = (val, node)
        prev = self.end.prev
        prev.next = node
        node.prev = prev
        node.next = self.end
        self.end.prev = node
        if not self.__handleQueue.is_alive():
            self.__handleQueue = HandleQueue(self)
            self.__handleQueue.start()

    def get(self, key):
        if key in self.dic:
            return self.dic[key][0]
        return None

    def keys(self):
        return [i for i in self.dic]

    def values(self):
        return [self.dic[i][0] for i in self.dic]

    def clear(self):
        self.dic.clear()
        self.start.next = self.end
        self.end.prev = self.start

    def get_first_key(self):
        if self.start.next != self.end:
            return self.start.next.key
        return None

    def get_last_key(self):
        if self.start.next != self.end:
            return self.end.prev.key
        return None


if __name__ == '__main__':
    d = TimedDict(5)
    for i in range(3):
        d[i] = i ** 2
    ls = [0]





