import matplotlib.pyplot as plt
from .db_ops import fetch_select_where

def plt_construct(x, y, dev_source, dev_cible):
    plt.figure(figsize=(10,5))
    plt.rcParams.update({"grid.linestyle": "-",
                         "grid.linewidth": 0.5,
                         "lines.linewidth": 2, })


    plt.plot(x, y, color='blue', linestyle='dashed', linewidth=2,
             marker='o', markerfacecolor='blue', markersize=9)
    plt.grid(True)

    plt.xlabel("Dates",fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel("Rate\n{}".format(dev_source+'->'+dev_cible),rotation=0,fontdict={'family':'serif','color':'darkred','size':10,'position':(0.0,1.0)})
    plt.title("CON-AR. Xchange Graph")

    return plt

def format_data(dev_source,dev_cible):
    currency_pair = fetch_select_where("date", "table_resultat",
                                       "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))

    amounts = fetch_select_where("cours", "table_resultat",
                                 "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))

    out_days = [item for t in currency_pair for item in t]
    data = [item for t in amounts for item in t]


    datam = [] # Amount list
    rate = [] # Rate
    for r in amounts:
        rate.append(r)

    for i in data:
        datam.append(i)
    dict_data = {}
    for date in range(len(out_days)):
        dict_data[out_days[date]] = float(datam[date])
    date_ = list(dict_data.keys())
    amount_ = list(dict_data.values())

    return date_,amount_
