# -*- coding:utf-8 -*-


# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
#
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
#
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
            
        if newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        
        
        if newInterval.start > intervals[-1].end:
            return intervals + [newInterval]
            
        tmp = list(filter(lambda i: intervals[i].end>=newInterval.start, range(len(intervals))))
        need_merge = list(filter(lambda i: intervals[i].start<=newInterval.end, tmp))
        
        if need_merge:
        
            min_idx = need_merge[0]
            max_idx = need_merge[-1]
            # need_merge = intervals[min_idx, max_idx+1]
            new_item = Interval(min(intervals[min_idx].start, newInterval.start), max(intervals[max_idx].end, newInterval.end))
            return intervals[:min_idx] + [new_item] + intervals[max_idx+1:]
        
        else:
            idx = tmp[0]
            return intervals[:idx] + [newInterval] + intervals[idx:]
            
