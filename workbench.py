from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri import reachability_graph
from pm4py.visualization.transition_system import visualizer as ts_visualizer

log = xes_importer.apply('./data/ArtificialPatientTreatmentOriginal.xes')

net, initial_marking, final_marking = alpha_miner.apply(log)

ts = reachability_graph.construct_reachability_graph(net, initial_marking)

gviz = ts_visualizer.apply(ts, parameters={ts_visualizer.Variants.VIEW_BASED.value.Parameters.FORMAT: "svg"})

# ts_visualizer.view(gviz)
# TODO add save path
ts_visualizer.save(gviz)
