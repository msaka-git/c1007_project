import matplotlib.pyplot as plt
from .db_ops import fetch_select_where

def plt_construct(x, y, dev_source, dev_cible, rate,amounts):
    plt.figure(figsize=(10,5))
    bar_plot=plt.bar(x,y,width=0.1)
    plt.xlabel("Dates",fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel("Amount\n{}".format(dev_source+'->'+dev_cible),rotation=0,fontdict={'family':'serif','color':'darkred','size':10,'position':(0.0,1.0)})
    plt.title("CON-AR. Xchange Graph")
    for idx, rect in enumerate(bar_plot):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.00 * height,
                'Rate: '+rate[idx]+'\n'+'Amount: '+amounts[idx],
                ha='center', va='bottom', rotation=0,fontdict={'color':'grey'})
    return plt

def format_data(dev_source,dev_cible):
    currency_pair = fetch_select_where("date", "table_resultat",
                                       "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))

    amounts = fetch_select_where("montant,cours", "table_resultat",
                                 "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))
    amounts_ = fetch_select_where("montant", "table_resultat",
                                 "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))
    out_days = [item for t in currency_pair for item in t]
    data = [item.split(',')[0] for t in amounts for item in t if isinstance(item,str)]
    data_am = [str(item) for t in amounts_ for item in t]
    print(data_am)
    datam = []
    rate = []
    for r in amounts:
        rate.append(str(r[1]))
    for i in data:
        datam.append(i.replace('.', ''))
    dict_data = {}
    for date in range(len(out_days)):
        dict_data[out_days[date]] = float(datam[date])
    date_ = list(dict_data.keys())
    amount_ = list(dict_data.values())

    return date_,amount_,rate, data_am
