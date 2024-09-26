import unittest
from graph_state_generation.graph_state import graph_state, graph_node 
from graph_state_generation.mappers import linear_mapper
from graph_state_generation.schedulers import greedy_stabiliser_measurement_scheduler 


class WeightedMapperTest(unittest.TestCase):

    def test_small_instance(self): 
        graph = graph_state.GraphState(3) 

        graph[0].append(*[1, 2])
        graph[1].append(*[0])
        graph[2].append(*[0])

        mapper = linear_mapper.LinearMapper(graph)
        
        sched = greedy_stabiliser_measurement_scheduler.GreedyStabiliserMeasurementSchedulerLeft(graph, mapper) 



if __name__ == '__main__':
    unittest.main()
