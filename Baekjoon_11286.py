#11286 절댓값 힙

#그냥 딕셔너리 만들고 힙에서 빼주는 방식으로 진행. 이게 과연 옳은가?
#다른 방법 찾아라..

import heapq
import sys

def cmd_0(storage) :
    if not storage :
        return 0
    else :
        return heapq.heappop(storage)[1]

storage = []

for i in range(int(sys.stdin.readline())) :
    cmd = int(sys.stdin.readline())

    if cmd == 0 :
        print(cmd_0(storage))
    else :
        heapq.heappush(storage,(abs(cmd),cmd))

