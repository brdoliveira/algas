import matplotlib.pyplot as plt
from use_db import *

def show_plot_data() -> None:
    """
    Função responsável por criar um gráfico com o valores que estão no banco de dados e plotá-lô.

    Args:
        none
    Returns:
        none
    """
    result : list = get_inserts_db('id,value,time_used')
    list_id : list = []
    list_noise_value : list = []
    list_time_used: list = []

    for id, value,time in result:
        list_id.append(id)
        list_noise_value.append(value)
        list_time_used.append(time)

    graph1 = plt.subplot(121)
    graph1.set_xlabel("Nº de registros")
    graph1.set_ylabel("Ruido(dBA)")
    graph1.plot(list_id,list_noise_value,'r')
    graph1.set_title("Correlação entre o ruido e o tempo")
    graph1.axhline(y = 65, color = 'black', linestyle = '-')

    graph2 = plt.subplot(122)
    graph2.set_ylabel("Tempo (ms)")
    graph2.set_xlabel("Nº de registros")
    graph2.plot(list_id,list_time_used,'black')
    graph2.set_title("Tempo gasto na execução")

    plt.show()

def show_plot_machine() -> None:
    """
    Função responsável por criar um gráfico com o valores que estão no banco de dados e plotá-lô.

    Args:
        none
    Returns:
        none
    """
    result : list = get_inserts_data_machine_db()
    list_value_machine : list = []
    list_name_machine : list = []

    for name, value in result:
       list_name_machine.append(name)
       list_value_machine.append(value)
    
    plt.xlabel("Nome das maquinas")
    plt.ylabel("Tempo gasto pelas maquinas")
    plt.plot(
        list_name_machine,
        list_value_machine,
        marker="o"
    )
    plt.title("Tempo gasto por maquina")

    plt.show()

show_plot_data()
show_plot_machine()