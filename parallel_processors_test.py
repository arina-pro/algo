from unittest import TestCase
from parallel_processors import ParallelProcessor

class TestDistribute_processors(TestCase):

   def test_distribute_processors(self):
       test_cases = [
           {'input': {'processor_count': 2, 'timings': [1, 1]}, 'output':[(0, 0), (1, 0)]},
           {'input': {'processor_count': 2, 'timings': [1,2,3,4,5]}, 'output': [(0,0),(1,0),(0,1),(1,2),(0,4)]},
           {'input': {'processor_count': 4, 'timings': [1]*20}, 'output': [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1),(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(3,3),(0,4),(1,4),(2,4),(3,4)]}
       ]

       for i, case in enumerate(test_cases):
           processes = case['input']['timings']
           do_it = DistributedProcesses(**case['input'])
           result = do_it.distribute_processors()
           self.assertEqual(len(processes), len(result))
           self.assertEqual(case['output'], result)
           print(f"Test case {i} success")


if __name__ == '__main__':
    unittest.main()
