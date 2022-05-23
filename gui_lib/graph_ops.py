import matplotlib.pyplot as plt
from .db_ops import fetch_select_where

def plt_construct(x, y, dev_source, dev_cible):
    plt.figure(figsize=(10,5))
    plt.rcParams.update({"grid.linestyle": "-",
                         "grid.linewidth": 0.5,
                         "lines.linewidth": 2, })

    #bar_plot=plt.bar(x,y,width=0.1)
    plt.plot(x, y, color='blue', linestyle='dashed', linewidth=2,
             marker='o', markerfacecolor='blue', markersize=9)
    plt.grid(True)
    #plt.hist(x,rwidth=0.1)
    plt.xlabel("Dates",fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel("Rate\n{}".format(dev_source+'->'+dev_cible),rotation=0,fontdict={'family':'serif','color':'darkred','size':10,'position':(0.0,1.0)})
    plt.title("CON-AR. Xchange Graph")

    # fig, ax = plt.subplots()
    #ax.hlines([1, 3, 5], -3, 5, color="green")
    #ax.set_title('matplotlib.axes.Axes.hlines Example')

    # for idx, rect in enumerate(bar_plot):
    #
    #     height = rect.get_height()
    #     plt.text(rect.get_x() + rect.get_width() / 2., 1.00 * height,
    #             'Rate: '+rate[idx]+'\n'+'Amount: '+amounts[idx],
    #             ha='center', va='bottom', rotation=0,fontdict={'color':'grey'})
    return plt

def format_data(dev_source,dev_cible):
    currency_pair = fetch_select_where("date", "table_resultat",
                                       "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))

    amounts = fetch_select_where("cours", "table_resultat",
                                 "devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))
    #amounts_ = fetch_select_where("cours", "table_resultat","devise_source = '{}' and devise_cible = '{}'".format(dev_source, dev_cible))
    out_days = [item for t in currency_pair for item in t]
    data = [item for t in amounts for item in t]

    #data_am = [str(item) for t in amounts_ for item in t]
    datam = [] # Amount list
    rate = [] # Rate
    for r in amounts:
        rate.append(r)
    # for i in data:
    #     datam.append(i.replace('.', ','))
    for i in data:
        datam.append(i)
    dict_data = {}
    for date in range(len(out_days)):
        dict_data[out_days[date]] = float(datam[date])
    date_ = list(dict_data.keys())
    amount_ = list(dict_data.values())
    print(date_)
    print(amount_)

    return date_,amount_ #, data_am
#format_data('EUR','INR')