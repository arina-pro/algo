import heapq


class ParallelProcessor:
    def __init__(self, n, tasks, timings):
        self.num_p = n
        self.timings = timings

    def distribute_p(self):
        p = [(0, cpu) for cpu in range(self.num_p)]
        output = []
        for timing in self.timings:
            timing_cpu = heapq.heappop(p)
            output.append(timing_cpu)
            heapq.heappush(p, (timing_cpu[0] + timing, timing_cpu[1]))
            heapq.heapify(p)
        return output


if __name__ == '__main__':
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    pp = ParallelProcessor(line1[0], line1[1], line2)
    output = pp.distribute_p()
    for i in output:
        print(i[1], i[0])