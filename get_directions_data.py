def calculate_fare (a):
    """ calculate fare from list with zone """

    ### parameters to calculate fare
    zone = ['mi_12','mi_12_mi_3','mi_3','mi_3_mi_4','mi_4','mi_5','mi_6','mi_7','mi_8','mi_9']
    
    dict_zone_rename  =    {
    'mi_12':'mi_0',
    'mi_12_mi_3':'mi_1',
    'mi_3':'mi_2',
    'mi_3_mi_4':'mi_3',
    'mi_4':'mi_4',
    'mi_5':'mi_5',
    'mi_6':'mi_6',
    'mi_7':'mi_7',
    'mi_8':'mi_8',
    'mi_9':'mi_9',
    }

    dict_zone_tariffa = {
    'mi_0, mi_3': {'1':[ 'Mi1-Mi3', ['#ff81de','#4b0082'] ]},            
    'mi_0, mi_4': {'2':[ 'Mi1-Mi4', ['#ff81de','#4b0082','#0000ff'] ]},
    'mi_0, mi_5': {'3':[ 'Mi1-Mi5', ['#ff81de','#4b0082','#0000ff','#008000'] ]},
    'mi_0, mi_6': {'4':[ 'Mi1-Mi6', ['#ff81de','#4b0082','#0000ff','#008000','#ffff00'] ]},
    'mi_0, mi_7': {'5':[ 'Mi1-Mi7', ['#ff81de','#4b0082','#0000ff','#008000','#ffff00','#ff8000'] ]},
    'mi_0, mi_8': {'6':[ 'Mi1-Mi8', ['#ff81de','#4b0082','#0000ff','#008000','#ffff00','#ff8000','#ff0000'] ]},
    'mi_0, mi_9': {'7':[ 'Mi1-Mi9', ['#ff81de','#4b0082','#0000ff','#008000','#ffff00','#ff8000','#ff0000','#ff0000'] ]}, ### check mi9
    'mi_1, mi_4': {'8':[ 'Mi3-Mi4', ['#4b0082','#0000ff'] ]},
    'mi_1, mi_5': {'9':[ 'Mi3-Mi5', ['#4b0082','#0000ff','#008000'] ]},
    'mi_1, mi_6': {'10':['Mi3-Mi6', ['#4b0082','#0000ff','#008000','#ffff00'] ]},
    'mi_1, mi_7': {'11':['Mi3-Mi7', ['#4b0082','#0000ff','#008000','#ffff00','#ff8000'] ]},
    'mi_1, mi_8': {'12':['Mi3-Mi8', ['#4b0082','#0000ff','#008000','#ffff00','#ff8000','#ff0000'] ]},
    'mi_1, mi_9': {'13':['Mi3-Mi9', ['#4b0082','#0000ff','#008000','#ffff00','#ff8000','#ff0000','#ff0000'] ]},
    'mi_3, mi_5': {'14':['Mi4-Mi5', ['#0000ff','#008000'] ]},
    'mi_3, mi_6': {'15':['Mi4-Mi6', ['#0000ff','#008000','#ffff00'] ]},
    'mi_3, mi_7': {'16':['Mi4-Mi7', ['#0000ff','#008000','#ffff00','#ff8000'] ]},
    'mi_3, mi_8': {'17':['Mi4-Mi8', ['#0000ff','#008000','#ffff00','#ff8000','#ff0000'] ]},
    'mi_3, mi_9': {'18':['Mi4-Mi9', ['#0000ff','#008000','#ffff00','#ff8000','#ff0000','#ff0000'] ]},
    'mi_5, mi_6': {'19':['Mi5-Mi6', ['#008000','#ffff00'] ]},
    'mi_5, mi_7': {'20':['Mi5-Mi7', ['#008000','#ffff00','#ff8000'] ]},
    'mi_5, mi_8': {'21':['Mi5-Mi8', ['#008000','#ffff00','#ff8000','#ff0000'] ]},
    'mi_5, mi_9': {'22':['Mi5-Mi9', ['#008000','#ffff00','#ff8000','#ff0000','#ff0000'] ]},
    'mi_6, mi_7': {'23':['Mi6-Mi7', ['#ffff00','#ff8000'] ]},
    'mi_6, mi_8': {'24':['Mi6-Mi8', ['#ffff00','#ff8000','#ff0000'] ]},
    'mi_6, mi_9': {'25':['Mi6-Mi9', ['#ffff00','#ff8000','#ff0000','#ff0000'] ]},
    'mi_7, mi_8': {'26':['Mi7-Mi8', ['#ff8000','#ff0000'] ]},
    'mi_7, mi_9': {'27':['Mi7-Mi9', ['#ff8000','#ff0000','#ff0000'] ]},
    'mi_8, mi_9': {'28':['Mi8-Mi9', ['#ff0000','#ff0000'] ]}
    }


    for n in a:
        if n == 'mi_999':
            return (90,'err_data','err_data','err_data','err_data')
        elif n == 'mi_n':
            return (100,'err_outstibm','err_outstibm','err_outstibm','err_outstibm')
    
    # rinomina i vettori per ottenere una sequenza confrontabile
    a_rename = [dict_zone_rename.get(n, n) for n in a]
    zone_rename = [dict_zone_rename.get(n, n) for n in zone]
    # compelta il vettore con le zone mancanti
    a_compl = [i for i in zone_rename if (i >= min(a_rename) and i <= max(a_rename))]
    # torna ai nomi originali
    inv_dict_zone_rename= {v: k for k, v in dict_zone_rename.items()}
    a_def = [inv_dict_zone_rename.get(n, n) for n in a_compl]
    ## esclude le zone tecniche
    n = 0
    if 'mi_12_mi_3' in a_def:
        n += 1
    if 'mi_3_mi_4' in a_def:
        n += 1
    else:
        pass
    fare = len(a_def) - n
    if 'mi_12' in a_def:
        fare += 1
    if fare == 2 and 'mi_12' in a_def:
        fare = 3
    elif fare == 1:
        fare = 2
    else:
        fare

    list_minmax = [min(a_rename), max(a_rename)]
    #print(list_minmax)
    #se le due zone sono mi_12, returna tar_id 1
    if list_minmax[0] == 'mi_0' and list_minmax[1] == 'mi_0':
        tar_id = '1'
    elif list_minmax[0] == 'mi_0' and list_minmax[1] == 'mi_1':
        tar_id = '1'
    #se le due zone sono mi_3, returna tar_id  8
    elif list_minmax[0] == 'mi_2' and list_minmax[1] == 'mi_2':
        tar_id = '8'
    #se le due zone sono mi_3_mi_4, returna tar_id 8
    elif list_minmax[0] == 'mi_3' and list_minmax[1] == 'mi_3':
        tar_id = '8'
    #negli altri casi in cui le due zone sono uguali, usa la tariffa tra quella zona e la successiva
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_1':
        tar_id = '8'
    elif list_minmax[0] == 'mi_1' and list_minmax[1] == 'mi_2':
        tar_id = '8'
    elif list_minmax[0] == 'mi_1' and list_minmax[1] == 'mi_3':
        tar_id = '8'
    elif list_minmax[0] == 'mi_2' and list_minmax[1] == 'mi_3':
        tar_id = '8'
    elif list_minmax[0] == 'mi_3' and list_minmax[1] == 'mi_4':
        tar_id = '14'
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_4':
        tar_id = '14'
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_5':
        tar_id = '19'
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_6':
        tar_id = '23'
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_7':
        tar_id = '26'
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_8':
        tar_id = '28'
    elif list_minmax[0] == list_minmax[1] and list_minmax[0] == 'mi_9':
        tar_id = '28'

    else:
        #se la zona minore e' mi_3, trasformala in mi_12_mi_3
        if list_minmax[0] == 'mi_2':
            list_minmax[0] = 'mi_1'
        #se la zona minore e' mi_4, trasformala in mi_3_mi_4
        elif list_minmax[0] == 'mi_4':
            list_minmax[0] = 'mi_3'
        #se la zona maggiore e' mi_3, trasformala in mi_3_mi_4
        if list_minmax[1] == 'mi_2':
            list_minmax[1] = 'mi_3'

        tar_id = list((dict_zone_tariffa[', '.join(list_minmax)]).keys())[0]

    if fare == 2:
        price = round((0.90 + (0.4*fare)),1)
    elif fare in (3,4,5):
        price = round((1.00 + (0.4*fare)),1)
    elif fare in (6,7,8):
        price = round((1.10 + (0.4*fare)),1)
    elif fare in (9,10,11):
        price = round((1.20 + (0.4*fare)),1)
    elif fare in (12,13,14):
        price = round((1.30 + (0.4*fare)),1)
    elif fare in (15,16,17):
        price = round((1.40 + (0.4*fare)),1)
    elif fare in (18,19):
        price = round((1.50 + (0.4*fare)),1)
####
##  attenzione il costo dei biglietti nella pagina di dettaglio e determinato da un dizionario nel client alla pagina directiondetailspagets
####

    if fare <= 4:
        duration = (45 + (15*fare))
    else:
        duration = (45 + (15*4) + (30*(fare-4)))    
    for k,v in dict_zone_tariffa.items() :
        if list(v.keys())[0] == tar_id:
            zone_id = v [tar_id][0]
            zone_color = v [tar_id][1][::-1]


    return (price,duration,tar_id,zone_id,zone_color)


def find_element_in_list(l,item):
    "se non trova item in list restituisce l'item più simile"
    import Levenshtein    
    import operator
    simil =  {}
    if item in l:
        return (item,1)
    else:
        for i in l:
            simil[i] = Levenshtein.ratio(i, item)
    return (max(simil.items(), key=operator.itemgetter(1))[0],max(simil.items(), key=operator.itemgetter(1))[1] )


def verify_stops_in_list (l,departure_stop,arrival_stop,num_stops):
    find_elem = lambda l, elem: [[i for i, x in enumerate(l) if x == e] for e in elem]
    if departure_stop not in l or arrival_stop not in l:
        return False
    #elif l.index(departure_stop) > l.index(arrival_stop):
    #    return False
    #elif (l.index(arrival_stop) - l.index(departure_stop) < (num_stops - 1)) or (l.index(arrival_stop) - l.index(departure_stop) > (num_stops + 1)):
    #    return False
    elif (len (find_elem (l,[departure_stop])[0]) == 1 
    and len (find_elem (l,[arrival_stop])[0]) == 1
    and num_stops - 1 <=  l.index(arrival_stop) - l.index(departure_stop) <= num_stops +1 ):
        return True
    else:
        for i in (find_elem (l,[departure_stop])[0]):
            for z in (find_elem (l,[arrival_stop])[0]):
                if  num_stops - 1 <= (z-i) <= num_stops + 1 :
                    return True
                else:
                    continue
        return False
    

def stops_index (l,departure_stop,arrival_stop,num_stops):
    find_elem = lambda l, elem: [[i for i, x in enumerate(l) if x == e] for e in elem]
    if len (find_elem (l,[departure_stop])[0]) == 1 and len (find_elem (l,[arrival_stop])[0]) == 1:
        return (l.index(departure_stop),l.index(arrival_stop))
    else:
        
        for i in (find_elem (l,[departure_stop])[0]):
            for z in (find_elem (l,[arrival_stop])[0]):
                if  num_stops - 1 <= (z-i) <= num_stops + 1 :
                    return (i,z)
                else:
                    continue
        return False

    
def convert_dt (dt):
    import re
    import datetime
    import pytz
    dt = dt.replace("PLUS", "+")
    dt_list = dt.split('T')
    date = dt_list[0]
    time = dt_list[1]
    time_n = re.sub(":00$", "00", time)
    t = datetime.datetime.strptime("%s %s" %(date,time_n), '%Y-%m-%d %H:%M:%S.%f%z')
    datetime_utc = t.astimezone(pytz.utc)
    if datetime_utc < datetime.datetime.utcnow().replace(tzinfo=pytz.UTC):
        datetime_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
    else:
        datetime_utc
    epoch_utc = datetime.datetime(1970,1,1, tzinfo=pytz.utc) 
    second_since_epoch =  int((datetime_utc - epoch_utc).total_seconds())
    second_since_epoch = second_since_epoch
    return second_since_epoch



def get_directions_data(origin,destination,departure_time):
    """ Fetches data from Google Directions API """

    from requests import get
    import json
    from contextlib import closing
    import csv
    import codecs


    comuni = {
    'Abbiategrasso':'45.3975061114103,8.92061680061559',
    'Agrate Brianza':'45.5771726105425,9.35531594292263',
    'Aicurzio':'45.6403946108076,9.4103906925686',
    'Albairate':'45.4193509412437,8.94067843115342',
    'Albiate':'45.6570339244807,9.25345240667014',
    'Arconate':'45.5409704137492,8.85263226610741',
    'Arcore':'45.6237514127895,9.3228053210888',
    'Arese':'45.5520533451732,9.07664822564332',
    'Arluno':'45.5055680270407,8.94717611826747',
    'Assago':'45.4092210588382,9.12915034325293',
    'Baranzate':'45.5262250602251,9.11291231623465',
    'Bareggio':'45.4854440801184,9.00644070115624',
    'Barlassina':'45.6555789222674,9.12940164415795',
    'Basiano':'45.5714904175387,9.46756595799559',
    'Basiglio':'45.3608715686494,9.15755834539551',
    'Bellinzago Lombardo':'45.5418256428011,9.44534989670628',
    'Bellusco':'45.6173181421996,9.42334326118685',
    'Bernareggio':'45.6455666703037,9.40422668120269',
    'Bernate Ticino':'45.4789125501443,8.81956044837768',
    'Besana in Brianza':'45.7025533025141,9.28315757393411',
    'Besate':'45.3125135771632,8.96985593948435',
    'Biassono':'45.6295568379091,9.27381941185445',
    'Binasco':'45.3310998646773,9.10190946908058',
    'Boffalora sopra Ticino':'45.4691187343698,8.83267935352773',
    'Bollate':'45.5426407718326,9.12225312939977',
    'Bovisio-Masciago':'45.6119893711422,9.1416130346167',
    'Bregnano':'45.6971189421022,9.06084903469789',
    'Bresso':'45.5358802730231,9.19255916902201',
    'Briosco':'45.7114731171994,9.24233931232091',
    'Brugherio':'45.5532400135935,9.29764790493649',
    'Bubbiano':'45.3282240341868,9.01675234636928',
    'Buccinasco':'45.4194262917869,9.11504970969049',
    'Burago di Molgora':'45.5977604165959,9.38258590080237',
    'Buscate':'45.5413500550623,8.81465894699135',
    'Busnago':'45.616321065434,9.46448618993593',
    'Bussero':'45.5255261053925,9.37565813455632',
    'Busto Arsizio':'45.6153487686066,8.86450971107459',
    'Busto Garolfo':'45.5480347744637,8.88008883315979',
    'Cabiate':'45.6757839141337,9.16833738385768',
    'Calusco d\'Adda':'45.6841752830204,9.47087261581036',
    'Calvignasco':'45.3329363689938,9.02015253604091',
    'Cambiago':'45.5716173536737,9.42146448564755',
    'Camparada':'45.6556739203092,9.31970922819963',
    'Canegrate':'45.569003390896,8.92657643629471',
    'Cantù':'45.7368709872547,9.12718081585001',
    'Caponago':'45.5672079122697,9.37268627613481',
    'Carate Brianza':'45.6729863829118,9.24083252343191',
    ###'Carimate':'45.6971937374886,9.10750839835772',
    'Carnate':'45.6527159987589,9.37547342616283',
    'Caronno Pertusella':'45.5968769851163,9.04530751091759',
    'Carpiano':'45.3427033633818,9.27199771679447',
    'Carugate':'45.5484877382928,9.3351975451675',
    'Casalmaiocco':'45.3522982319515,9.37412915443182',
    'Casarile':'45.3172239438612,9.10600828313041',
    'Casatenovo':'45.69880999904,9.30982786271278',
    'Casorate Primo':'45.311356960351,9.01981630465802',
    'Casorezzo':'45.5243047500698,8.90585009850253',
    'Cassano d\'Adda':'45.5245529196227,9.51305876008482',
    'Cassina de\' Pecchi':'45.5214281996718,9.36256220121482',
    'Cassinetta di Lugagnano':'45.4238969327586,8.90603148990133',
    'Castano Primo':'45.5559674973453,8.77285255272056',
    'Castellanza':'45.6131271179275,8.89398637917861',
    'Cavenago di Brianza':'45.5832772525502,9.41441407852556',
    'Ceriano Laghetto':'45.6251642051812,9.07959514006101',
    'Cermenate':'45.7028172551938,9.09271869409912',
    'Cernusco Lombardone':'45.6947849597799,9.39710629412056',
    'Cernusco sul Naviglio':'45.5209311614163,9.33055890427804',
    'Cerro al Lambro':'45.3323470028473,9.33786698822785',
    'Cerro Maggiore':'45.5914754180923,8.95733426211283',
    'Cesano Boscone':'45.4458234211803,9.09036981770502',
    'Cesano Maderno':'45.6304465489834,9.14087238627908',
    'Cesate':'45.5953075483716,9.07802230024788',
    'Cinisello Balsamo':'45.5515632381298,9.21743047312617',
    'Cisliano':'45.4429562167451,8.98399947340676',
    'Cogliate':'45.6459467834418,9.0814848988639',
    'Cologno Monzese':'45.5275109862779,9.28283908397883',
    'Colturano':'45.38039901789,9.33605736074482',
    'Comazzo':'45.4413263437678,9.46443235975717',
    'Concorezzo':'45.5917956795184,9.33332786972816',
    'Corbetta':'45.4697408998658,8.91849346924913',
    'Cormano':'45.5448621677081,9.17137581846153',
    'Cornaredo':'45.4899186235201,9.03472576400363',
    'Cornate d\'Adda':'45.6440026256389,9.46603557474397',
    'Correzzana':'45.6660342784763,9.30349241326974',
    'Corsico':'45.4358323688212,9.10920392078842',
    'Cuggiono':'45.5055839547537,8.82140752603509',
    'Cusago':'45.448814034784,9.03720363146626',
    'Cusano Milanino':'45.5473351405431,9.18228894538789',
    'Dairago':'45.5689298362877,8.8647968360453',
    'Desio':'45.6194584066083,9.20761406270332',
    'Dresano':'45.3714630824542,9.35879815652626',
    'Figino Serenza':'45.7106218118915,9.12973014239584',
    'Gaggiano':'45.4086186043588,9.03102214922039',
    'Garbagnate Milanese':'45.5797834581904,9.08043694307647',
    'Gessate':'45.545525744947,9.43610828474254',
    'Giussano':'45.69722074884,9.20762134431959',
    'Gorgonzola':'45.5363232434331,9.40391662185131',
    'Grezzago':'45.5901568211822,9.4939041027301',
    'Gudo Visconti':'45.3713812486685,8.9955372652024',
    'Inveruno':'45.5111729921981,8.85306527915855',
    'Inzago':'45.5374899790845,9.47945289152931',
    'Lacchiarella':'45.3253072958361,9.13609932597045',
    'Lainate':'45.5630560970312,9.02884596087957',
    'Lazzate':'45.6733538250405,9.08452455874874',
    'Legnano':'45.5940358358024,8.91040864771954',
    'Lentate sul Seveso':'45.6682043925006,9.13301049875583',
    'Lesmo':'45.6449488143678,9.3091488187892',
    'Limbiate':'45.6036392529375,9.12355059888681',
    'Liscate':'45.480635931187,9.40922664181429',
    'Lissone':'45.6061330901823,9.23538578893553',
    'Locate di Triulzi':'45.359781722639,9.22158525821501',
    'Macherio':'45.6420217497388,9.26734744948935',
    'Magenta':'45.4681298711086,8.88079874171203',
    'Magnago':'45.5780273502682,8.8083636273969',
    'Marcallo con Casone':'45.4840020819934,8.87155057139604',
    'Mariano Comense':'45.6940350350689,9.1824564542041',
    'Masate':'45.5675080245122,9.46385102230308',
    'Meda':'45.6621341674637,9.15922573155362',
    'Mediglia':'45.3950964242861,9.3328545779013',
    'Melegnano':'45.356178834489,9.32033460742717',
    'Melzo':'45.5015718023465,9.41920728112631',
    'Merate':'45.6943726324965,9.42377251918498',
    'Merlino':'45.4326504789902,9.43004931521045',
    'Mesero':'45.5003403905935,8.85796279225043',
    'Mezzago':'45.6279873035285,9.44247962392547',
    'Milano':'45.468212191837644,9.175879955291748',
    'Misinto':'45.6648898008333,9.07516737170056',
    'Monticello Brianza':'45.7030922932573,9.30576278276598',
    'Monza':'45.5777375994998,9.27312481497008',
    'Morimondo':'45.3541993950111,8.95459481966937',
    'Motta Visconti':'45.2876233473867,8.99279577533038',
    'Muggiò':'45.5934566898936,9.22552319562476',
    'Mulazzano':'45.3737852220407,9.39914420732764',
    'Nerviano':'45.5561072984257,8.9806805425044',
    'Nosate':'45.54753920679,8.72525458549277',
    'Nova Milanese':'45.5896773684623,9.19722346914139',
    'Novate Milanese':'45.5322851182175,9.13391721830098',
    'Novedrate':'45.6952471281005,9.1301094498454',
    'Noviglio':'45.3567387367828,9.05121084282353',
    'Olgiate Molgora':'45.729163324475,9.40375424908697',
    'Opera':'45.3741536676787,9.211805734257',
    'Origgio':'45.5993502337926,9.01808901997317',
    'Ornago':'45.5983455776804,9.42103925920136',
    'Osnago':'45.6786472325048,9.38729879684285',
    'Ossona':'45.5042569260142,8.90033425495052',
    'Ozzero':'45.3659069941126,8.92549105338476',
    'Paderno d\'Adda':'45.6783213283114,9.43906810285427',
    'Paderno Dugnano':'45.5645291776422,9.16114448547571',
    'Pantigliate':'45.4335374914707,9.35204855172878',
    'Parabiago':'45.5524733239398,8.94627991834551',
    'Paullo':'45.4166069205055,9.39787369718987',
    'Pero':'45.5087825230241,9.08596614000066',
    'Peschiera Borromeo':'45.4317484832456,9.31139703642161',
    'Pessano con Bornago':'45.5484810306907,9.38413503416741',
    'Pieve Emanuele':'45.3396590484907,9.20329799088526',
    'Pioltello':'45.4863482110705,9.32843838678042',
    'Pogliano Milanese':'45.5374094419206,8.99450760876989',
    'Pozzo d\'Adda':'45.5720670539394,9.49911084836111',
    'Pozzuolo Martesana':'45.5146446739695,9.46352925181308',
    'Pregnana Milanese':'45.5101122350615,9.00268544924311',
    'Renate':'45.7280674084415,9.27992163101531',
    'Rescaldina':'45.622295972255,8.94696143035787',
    'Rho':'45.5237845162555,9.04368897883358',
    'Robbiate':'45.6836681551098,9.43845504810748',
    'Robecchetto con Induno':'45.5323080772566,8.76512695285185',
    'Robecco sul Naviglio':'45.4401333195494,8.88760935935682',
    'Rodano':'45.4721206458311,9.35501160067282',
    'Roncello':'45.6020689390999,9.45329679549189',
    'Ronco Briantino':'45.6667098059096,9.40396598129601',
    'Rosate':'45.3526408792136,9.01660726759622',
    'Rovellasca':'45.6661242483626,9.05460950270282',
    'Rozzano':'45.3815577270394,9.15805538521564',
    'San Donato Milanese':'45.4164870870497,9.26145787560918',
    'San Giorgio su Legnano':'45.5736226596728,8.92017292676097',
    'San Giuliano Milanese':'45.3916053831387,9.28677464514333',
    'Santo Stefano Ticino':'45.481069500601,8.91789576158285',
    'San Vittore Olona':'45.5859150453102,8.94337630816063',
    'San Zenone al Lambro':'45.3275048761234,9.35635604112577',
    'Saronno':'45.6255050161086,9.03105488942077',
    'Sedriano':'45.4873873107038,8.97671524753941',
    'Segrate':'45.4809819883183,9.2985518875986',
    'Senago':'45.5793661683622,9.13269326906792',
    'Seregno':'45.6460225450372,9.20315079659012',
    'Sesto San Giovanni':'45.5409671094362,9.23844937882483',
    'Settala':'45.44431194027,9.38570742198796',
    'Settimo Milanese':'45.4801085225643,9.05457162721417',
    'Seveso':'45.6479944342083,9.14003522357412',
    'Solaro':'45.616836794312,9.08001357430165',
    'Sordio':'45.339385879332,9.36379737817019',
    'Sovico':'45.6458203966571,9.26165471405914',
    'Sulbiate':'45.6339760823897,9.42034986243206',
    'Tavazzano con Villavesco':'45.3264361060065,9.4027789917988',
    'Treviglio':'45.515408515783,9.58852895863556',
    'Trezzano Rosa':'45.5830458621819,9.48894907033893',
    'Trezzano sul Naviglio':'45.4204104347872,9.06708622306902',
    'Trezzo sull\'Adda':'45.6074179014402,9.52202710600221',
    'Tribiano':'45.4149324584382,9.37640274032207',
    'Triuggio':'45.6590104983894,9.26836988057268',
    'Truccazzano':'45.4838930550946,9.46886795950557',
    'Turbigo':'45.5282616256607,8.73881878487308',
    'Uboldo':'45.6140972299607,9.00463417869362',
    'Usmate Velate':'45.6503052695235,9.36112277026741',
    'Vanzaghello':'45.578085983145,8.78753843622511',
    'Vanzago':'45.5250185276229,8.99550103429449',
    'Vaprio d\'Adda':'45.5754851718209,9.52570392643159',
    'Varedo':'45.5962709400647,9.15337408445129',
    'Vedano al Lambro':'45.6087794721451,9.2700207850602',
    'Veduggio con Colzano':'45.731525160214,9.26855466833012',
    'Verano Brianza':'45.6867483857749,9.22740864252724',
    'Verderio':'45.6687973731166,9.43940890654324',
    'Vermezzo':'45.3969080565819,8.97520231487859',
    'Vernate':'45.3172673289862,9.06139198006784',
    'Vignate':'45.4940977657031,9.37477519935266',
    'Villa Cortese':'45.5657591204401,8.89111480730062',
    'Villasanta':'45.6031800454544,9.30417343948458',
    'Vimercate':'45.6103606201696,9.37137654591474',
    'Vimodrone':'45.5155140010103,9.28513232055388',
    'Vittuone':'45.4907971606956,8.94741471780569',
    'Vizzolo Predabissi':'45.3614245067054,9.34612755223102',
    'Zelo Buon Persico':'45.4119950462218,9.43263631605883',
    'Zelo Surrigone':'45.386763487073,8.98289615431074',
    'Zibido San Giacomo':'45.3660747160643,9.11151891128206',
    'San Donato M3':'45.4292064010295,9.25623390785034',
    'Milano Cascina Gobba M2':'45.5114424010218,9.26051020785954',
    'Sesto Marelli M1':'45.523477101023,9.22796150787429',
    'Rho Fiera Milano M1':'45.5198398010336,9.08710730793072',
    'Milano Linate Aeroporto':'45.4614943546954,9.27881493135738',
    'Cinisello Monza Bettola':'45.5562482183217,9.24932473010538'
    }


    url = 'https://maps.googleapis.com/maps/api/directions/json?'


    params = {
    'mode' : 'transit',
    'alternatives' : 'true',
    'origin' : comuni[origin],
    'destination' : comuni[destination],
    'language' : 'it',
    'departure_time': convert_dt(departure_time),
    'key' : 'use a valid key'
    }

    response = get(url, params=params)
    if response.raise_for_status() is None:
        todos = json.loads(response.text)
    else:
        return []
   

    n_alt = len(todos["routes"])
    n_alt_transit = []
    cont_alt_transit = 0
    data =[]

    for i in range (0, n_alt):
        if "departure_time" in todos["routes"][i]["legs"][0]:
            n_alt_transit.append(i)
            data.append({})
            data[cont_alt_transit]["duration"] = todos["routes"][i]["legs"][0]["duration"]
            data[cont_alt_transit]["distance"] = todos["routes"][i]["legs"][0]["distance"]
            data[cont_alt_transit]["arrival_time"] = todos["routes"][i]["legs"][0]["arrival_time"]
            data[cont_alt_transit]["departure_time"] = todos["routes"][i]["legs"][0]["departure_time"]
            data[cont_alt_transit]["fare"] = {}
            data[cont_alt_transit]["steps"] = []
            new_step = 0
            for r in  range(0,len (todos["routes"][i]["legs"][0]["steps"])):
                if (todos["routes"][i]["legs"][0]["steps"][r]["travel_mode"]) == 'TRANSIT':
                    data[cont_alt_transit]["steps"].append (todos["routes"][i]["legs"][0]["steps"][r]["transit_details"])
                    new_step += 1
            cont_alt_transit += 1
        else:
            pass ### TODO verificare se pass funziona bene o se necessario il continue

    ### file esterno che consente di ricavae la seqeunza di fermate visto che l'api direction non la restituisce
    agency_all_url = 'https://www.dropbox.com/scl/fi/oqg2o1y1gbdzz8j9kce28/list_app_20230919.csv?rlkey=0jnxa421fdwi4em3xrmfx91a5&dl=1'

    
    #create and inizialize nested dictionary
    keys_alt = (list(range(0,len(n_alt_transit))))
    data_zone =  {key:{}   for key in keys_alt}
    for keys_alt in (list(range(0,len(n_alt_transit)))):
        for keys_step in (list(range(0,len (data [keys_alt]["steps"])))):
            data_zone[keys_alt][keys_step] = []

    agencies = []
    print (agencies)
    with closing(get(agency_all_url)) as read_file:       
        for i in range (0, len(n_alt_transit)):
            for z in range (0,len (data [i]["steps"])):
                d_row = {}
                reader = csv.reader(codecs.iterdecode(read_file.iter_lines(), 'utf-8'), delimiter=',')
                for tx in reader:
                    if (data [i]["steps"][z]["line"]["agencies"][0]["name"].lower() == tx[0].lower()
                    and data [i]["steps"][z]["line"]["short_name"].lower() == tx[1].lower() 
                    and verify_stops_in_list (tx[3].split('||'), find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["departure_stop"]["name"].lower())[0], find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["arrival_stop"]["name"].lower())[0],  (data [i]["steps"][z]["num_stops"])) ):
                        rate = find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["departure_stop"]["name"].lower())[1] + find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["arrival_stop"]["name"].lower())[1]       
                        start = stops_index (tx[3].split('||'), find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["departure_stop"]["name"].lower())[0], find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["arrival_stop"]["name"].lower())[0],  (data [i]["steps"][z]["num_stops"]))[0]
                        end = stops_index (tx[3].split('||'), find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["departure_stop"]["name"].lower())[0], find_element_in_list(tx[3].split('||'),data[i]["steps"][z]["arrival_stop"]["name"].lower())[0],  (data [i]["steps"][z]["num_stops"]))[1] + 1

                        d_row [rate] = tx[4].split('||')[start:end] 
                        data_zone[i][z] = d_row
                    if tx[0].lower() not in agencies:
                        agencies.append(tx[0].lower())                        

    print (agencies)
                    

    for k, v in data_zone.items():
        a=[]
        for k1,v1 in v.items():
            if not v1:
                a.append(["mi_999"])
            else:
                a.append (v1[max(v1)])
        a=list(set().union(*a))


        data_zone[k] = a
        data[k]["fare"]['price'] = calculate_fare (a)[0]
        data[k]["fare"]['duration'] = calculate_fare (a)[1]
        data[k]["fare"]['id'] = calculate_fare (a)[2]
        data[k]["fare"]['zone_id'] = calculate_fare (a)[3]
        data[k]["fare"]['zone_color'] = calculate_fare (a)[4]

        
    for i in range (0, len(data)):
        for z in range (0,len (data [i]["steps"])):
            if 'short_name' not in data [i]["steps"][z]["line"]:
                data [i]["steps"][z]["line"]['short_name'] = data [i]["steps"][z]["line"]['name']
            if (data [i]["steps"][z]["line"]["agencies"][0]["name"].lower() not in agencies):
                data[i]["fare"]['price'] = 99  
                data[i]["fare"]['zone_id'] = 'err_no_agency'
                data[i]["fare"]['duration'] = 'err_no_agency'
                data[i]["fare"]['zone_color'] = 'err_no_agency'
                data[i]["fare"]['id'] = 'err_no_agency'
            ### pag 34 regolamento tariffario     
            elif ((origin == 'Verderio' or origin == 'Robbiate' or origin == 'Paderno d\’Adda' 
                    or origin == 'Olgiate Molgora' or origin == 'Monticello Brianza' or origin == 'Merate' 
                    or origin == 'Casatenovo' or origin == 'Treviglio' or origin == 'Rovellasca' or origin == 'Mariano Comense' 
                    or origin == 'Cermenate' or origin == 'Cantù' or origin == 'Uboldo' or origin == 'Origgio' 
                    or origin == 'Saronno' or origin == 'Busto Arsizio' or  origin == 'Caronno Pertusella' or origin == 'Castellanza'
                    ## non nella lista ma fa riferimento alal stazione merate-cernusco
                    or origin == 'Cernusco Lombardone' 
                    or destination == 'Verderio' or destination == 'Robbiate' or destination == 'Paderno d\’Adda' 
                    or destination == 'Olgiate Molgora' or destination == 'Monticello Brianza' or destination == 'Merate' 
                    or destination == 'Casatenovo' or destination == 'Treviglio' or destination == 'Rovellasca' 
                    or destination == 'Mariano Comense' or destination == 'Cermenate' or destination == 'Cantù' 
                    or destination == 'Uboldo' or destination == 'Origgio' or destination == 'Saronno' or destination == 'Busto Arsizio' 
                    or destination == 'Caronno Pertusella' or destination == 'Castellanza'
                    ## non nella lista ma fa riferimento alal stazione merate-cernusco
                    or destination == 'Cernusco Lombardone' 
                    )  
                    and data [i]["steps"][z]["line"]["agencies"][0]["name"].lower() == 'trenord'):
                data[i]["fare"]['price'] = 100  
                data[i]["fare"]['id'] = 'err_outstibm'
                data[i]["fare"]['zone_id'] = 'err_outstibm'
                data[i]["fare"]['duration'] = 'err_outstibm'
                data[i]["fare"]['zone_color'] = 'err_outstibm'    
            elif (data [i]["steps"][z]["line"]["agencies"][0]["name"].lower()) == 'autoguidovie s.p.a.':
                data [i]["steps"][z]["line"]["agencies"][0]["name"] = 'AGI'
            elif (data [i]["steps"][z]["line"]["agencies"][0]["name"].lower()) == 'movibus s.r.l.':
                data [i]["steps"][z]["line"]["agencies"][0]["name"] = 'MOVIBUS'
            elif (data [i]["steps"][z]["line"]["agencies"][0]["name"].lower()) == 'net srl':
                data [i]["steps"][z]["line"]["agencies"][0]["name"] = 'NET'
            elif (data [i]["steps"][z]["line"]["agencies"][0]["name"].lower()) == 'pmt srl':
                data [i]["steps"][z]["line"]["agencies"][0]["name"] = 'PMT'
                        
    data_sort = sorted(data, key = lambda i: (i["fare"]['price'],i["duration"]['value'])) 
    #print (data_sort)                    
    client_json = json.dumps(data_sort)
    return client_json



def get_directions_by_parameter (request):
    """ HTTP Cloud Function
    Arg: request (flask.Request)
    """
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure_time = request.args.get('departure_time')
    
    print('************')
    print (origin)
    print (destination)
    print (departure_time)
    print('************')


    directions = get_directions_data(origin,destination,departure_time)
    
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Content-Type':'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    # END CORS
    return (directions, 200, headers)
