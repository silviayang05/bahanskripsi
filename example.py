from vrptw_base import VrptwGraph
from basic_aco import BasicACO


if __name__ == '__main__':
    file_path = './solomon-100/rc101.txt'
    ants_num = 50
    max_iter = 100
    beta = 2
    tau = 0.1
    show_figure = True

    graph = VrptwGraph(file_path)
    basic_aco = BasicACO(graph, ants_num=ants_num, beta=beta, tau=tau,
                         whether_or_not_to_show_figure=show_figure, max_iter=max_iter)

    basic_aco.run_basic_aco()