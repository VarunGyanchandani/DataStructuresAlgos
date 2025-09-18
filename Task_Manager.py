# task_manager.py
from typing import List, Dict, Tuple
import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap: List[Tuple[int, int, int]] = []  # (-priority, -taskId, taskId)
        self.task_map: Dict[int, Tuple[int, int]] = {}  # taskId -> (userId, priority)

        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId = heapq.heappop(self.heap)
            if taskId not in self.task_map:
                continue
            userId, curPriority = self.task_map[taskId]
            if -priority == curPriority:
                del self.task_map[taskId]
                return userId
        return -1



taskManager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
taskManager.add(4, 104, 5)
taskManager.edit(102, 8)
print(taskManager.execTop())  # 3
taskManager.rmv(101)
taskManager.add(5, 105, 15)
print(taskManager.execTop())  # 5
