class Computer:
    # users is the list of users
    # each user has a field that is a list of all the times that they are free
    # times are stored as a double value, number of minutes from midnight of the day, ex 11:15 am is stored as 675
    def __init__(self, users):
        self.times = []
        for u in users:
            times.append(u.getTime())


    def possibleTimes(self, minLen):
        out = []
        works = True
        for i in times:
            rest = times[times.index(i)::]
            temp = []
            for j in range(len(rest) - 1):
                current = rest[j]
                future = rest[j + 1]
                if (current + 1) == future:
                    if current in temp:
                        pass
                    else:
                        temp.append(current)
                    if future in temp:
                        pass
                    else:
                        temp.append(future)
                else:
                    break
            out.append(temp)
        for key in out:
            if len(key) < minLen:
                out.remove(key)
        out = remove_duplicates(out)
        return out
    def remove_duplicates(data):
        for key in data:
            for ele in data:
                if ele != key:
                    if set(key) > set(ele):
                        data.remove(ele)
        return data



    def longestUniqueSubwithBoundaries(self, earliest_time, latest_time, minLen):
        for key in self.times:
            if key < earliest_time:
                self.times.remove(key)
            if key > latest_time:
                self.times.remove(key)

        possibleTimes(self, minLen)
