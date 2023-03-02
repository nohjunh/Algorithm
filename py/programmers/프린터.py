def solution(priorities, location):
  queue = [(idx, prior) for idx, prior in enumerate(priorities)]
  answer = 0
  while True:
    cur = queue.pop(0)
    if any(cur[1] < qData[1] for qData in queue):
      queue.append(cur)
    else:
      answer += 1
      if cur[0] == location:
        return answer