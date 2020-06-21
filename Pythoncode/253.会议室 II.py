class Solution:
    def minMeetingRooms(self, intervals):
        timeline = []
        for starttime, endtime in intervals:
            timeline.append((starttime, 1))
            timeline.append((endtime, 0))
        timeline.sort(key=lambda x: x[1]) #同一时间点，先结束再开始
        timeline.sort(key=lambda x: x[0])
        notinuse = 0
        for time, status in timeline:
            if status == 0: #会议结束
                notinuse += 1
            else:
                if notinuse == 0:
                    notinuse += 1
                notinuse -= 1
        return notinuse

s = Solution()
s.minMeetingRooms([[0,30],[5,10],[15,20]])