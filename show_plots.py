import matplotlib.pyplot as plt
from use_db import *

def show_plot_value() -> None:
    """
    Função responsável por criar um gráfico com o valores que estão no banco de dados e plotá-lô.

    Args:
        none
    Returns:
        none
    """
    result : list = get_inserts('id,value,memory_used,time_used')
    list_id : list = []
    list_noise_value : list = []
    list_memory_used : list = []
    list_time_used: list = []

    for id, value,memory,time in result:
        list_id.append(id)
        list_noise_value.append(value)
        list_memory_used.append(memory)
        list_time_used.append(time)

    graph1 = plt.subplot(212)
    graph1.set_xlabel("Nº de registros")
    graph1.set_ylabel("Ruido(dBA)")
    graph1.plot(list_id,list_noise_value,'r')
    graph1.set_title("Correlação entre o ruido e o tempo")
    graph1.axhline(y = 65, color = 'black', linestyle = '-')

    graph2 = plt.subplot(221)
    graph2.set_ylabel("Tempo (ms)")
    graph2.plot(list_id,list_time_used,'black')
    graph2.set_title("Tempo gasto na execução")

    graph3 = plt.subplot(222)
    graph3.set_ylabel("Memória(kb)")
    graph3.plot(list_id,list_memory_used,'black')
    graph3.set_title("Gasto na execução")
    plt.show()

show_plot_value()