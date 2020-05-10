print('########################### REPUBLICA AGREGADOS ####################################')
print('==================== INTERNET =============================')
internet = float(input('Valor da internet :R$ '))
qts_internet= int(input('Quantos entrarão na conta de INTERNET ? '))
contapercap=internet/qts_internet
print(f'===========>>>>>>>>>>> Valor da internet para cada membro: R${contapercap:.2f}')
print()
print('==================== CONTA DE ÁGUA ===========================')
agua_cons= float(input('Valor da água em relação ao consumo: R$ '))
agua_tarifa=float(input('Valor da agua em tarifas fixas: R$ '))
total_agua=agua_cons+agua_tarifa
obs=int(input('Quantos membros terão desconto no consumo por dias ausentes na republica: '))
contaagua_pout_tot=0
if obs==1:
        print('OK...vamos calcular esse desconto; só preciso de algumas informações...')
        dias_leitura = int(input('A leitura da conta equivale a quantos dias de consumo: '))
        qtd_div_aguacons = int(input('Quantos membros vao rachar a conta sem esse desconto e sem as taxas fixas: '))
        people_out = str(input(f'Nome da pessoa que tera desconto: '))
        dias_cons = int(input(f'Quantos dias {people_out} consumiu: '))
        tarifa_pcap = agua_tarifa/qtd_div_aguacons
        valor_percapcons=agua_cons/qtd_div_aguacons
        print(f'=============> R${valor_percapcons:.2F} Valor do consumo percapita')
        days_out=dias_leitura-dias_cons
        valor_desc=(valor_percapcons/dias_leitura)*days_out
        print(f'=============> R${valor_desc:.2F} valor do desconto para {people_out}')
        percap_membro_out=valor_percapcons-valor_desc
        print(f'=============> R${percap_membro_out+tarifa_pcap:.2f} Valor per capita para {people_out}. '
              f'Inclui R${percap_membro_out:.2f} dos dias consumidos e R${tarifa_pcap:.2f} de taxas fixas per capita.')
        percap_aposdesc=(valor_desc/(qtd_div_aguacons-obs))+valor_percapcons
        print(f'=============> R$ {percap_aposdesc+tarifa_pcap:2f}. Valor per capita para o restante da casa, '
              f'incluindo o desconto concedido e a tarifa fixa de R${tarifa_pcap:.2f} cada.')
if obs>1:
    print('OK...vamos calcular esse desconto; só preciso de algumas informações...')
    dias_leitura = int(input('A leitura da conta equivale a quantos dias de consumo: '))
    qtd_div_aguacons = int(input('Quantos membros vao rachar a conta sem esse desconto e sem as taxas fixas: '))
    tarifa_pcap = agua_tarifa / qtd_div_aguacons
    valor_totaldesc=0
    for c in range(1,obs+1):
        people_out=str(input(f'Nome do {c}º que tera desconto: '))
        dias_cons = int(input(f'Quantos dias {people_out} consumiu: '))
        valor_percapcons = agua_cons / qtd_div_aguacons
        days_out = dias_leitura - dias_cons
        valor_desc=(valor_percapcons/dias_leitura)*days_out
        valor_totaldesc=valor_totaldesc+valor_desc
        percap_membro_out = valor_percapcons - valor_desc
        percap_aposdesc = (valor_totaldesc / (qtd_div_aguacons - obs)) + valor_percapcons
        print(f'================> R${valor_desc:.2f} de desconto para {people_out}!\n==================> '
              f'R${percap_membro_out+tarifa_pcap:.2f} Valor per capita para {people_out}'
              f'incluindo R${percap_membro_out:.2f} de consumo e R${tarifa_pcap:.2f} das taxas fixas percap')
    print('************************************************Restante da Casa***************************************************')
    print(f'===============> R$ {valor_percapcons:.2f} Valor per capita antes do desconto.\n=================> R${valor_totaldesc:.2f} Valor total do desconto.')
    print(f'===============> R$ {percap_aposdesc+tarifa_pcap:.2f} Valor per capita para o estante da casa após os descontos!'
          f'incluindo R${percap_aposdesc:.2f} de valor percap referente a consumo + R${tarifa_pcap:.2f} das tarifas fixas percapita!')

if obs==0:
    qtd_div_aguaconstarifa=int(input('Quantidade de membros que vão dividir essa conta: '))
    contapercap=(total_agua)/qtd_div_aguaconstarifa
    print(f'=====================> R${total_agua:.2f} É o valor da conta de água, incluindo consumo e taxas fixas.'
          f'\n====================> R${contapercap:.2f} é o valor percapita.')
print()
print('============================= CONTA DE ENERGIA =================================')
luz_cons=float(input('Valor da luz - incluidino possiveis acrescimos ou não:' ))
acresc_luz=' '
while acresc_luz not in 'SN':
    acresc_luz=str(input('Possui acrescimo [SIM/NAO]? ')).strip().upper()[0]
if acresc_luz in 'S':
    valor_acres=float(input('Valor acrescimo: '))
    people_out2=int(input('Quantidade de membros que pagarão esse acrescimo: '))
    valor_acres_pcap=valor_acres/people_out2
    luz_sem_acresc=luz_cons-valor_acres
    print(f'==============> O valor da luz descontando o acrescimo de {valor_acres:.2f} é R${luz_sem_acresc:.2f}!',end='')
    luz_sem_acresc_pcap=int(input(' Dividir esse valor para quantos membros da republica ?' ))
    luz_sem_acresc_pcap_valor=luz_sem_acresc/luz_sem_acresc_pcap
    desc_cons = str(input('Algum membro tera desconto por dias ausentes na republica [SIM/NÃO] ? ')).strip().upper()[0]
    if desc_cons in 'S':
        membros_desc=int(input('Quantos membros terão desconto: '))
        dias_leitura=int(input('Nº de dias equivalentes a leitura dessa conta: '))
        if membros_desc==1:
            nome_membro_desc=str(input(f'Nome do membro que requeriu desconto: '))
            dias_cons=int(input(f'Quantidade de dias que {nome_membro_desc} consumiu: '))
            days_out2=dias_leitura-dias_cons
            luz_membro_desc_valor=(luz_sem_acresc_pcap_valor/dias_leitura)*days_out2
            print(f'=============> Desconto de R$ {luz_membro_desc_valor:.2f} para {nome_membro_desc}')
            novo_percap_comdesc = luz_sem_acresc_pcap_valor - luz_membro_desc_valor
            print(f'=============> Valor per capita para {nome_membro_desc} é de R${novo_percap_comdesc:.2f}!')
            desc_total=0
            desc_total += luz_membro_desc_valor
            print(f' ================>Total do desconto: RS {desc_total:.2f}! Devera ser dividido por {luz_sem_acresc_pcap - membros_desc} membros!')
            desc_div_resto = desc_total / (luz_sem_acresc_pcap - membros_desc)
            novo_percap_semdesc = luz_sem_acresc_pcap_valor + desc_div_resto
            print(
                f'================>  Valor per capita para os {luz_sem_acresc_pcap - membros_desc} membros: R${novo_percap_semdesc:.2f}')
        if membros_desc>1:
            desc_total=0
            desc_div_resto=0
            for c in range(1,membros_desc+1):
                nome_membros_des=str(input(f'Nome do {c}º membro que requeriu o desconto: '))
                dias_cons=int(input(f'Quantidade de dias que {nome_membros_des} consumiu: '))
                days_out2=dias_leitura-dias_cons
                luz_membro_desc_valor=(luz_sem_acresc_pcap_valor/dias_leitura)*days_out2
                print(f'=============> Desconto de R$ {luz_membro_desc_valor:.2f} para {nome_membros_des}')
                novo_percap_comdesc = luz_sem_acresc_pcap_valor - luz_membro_desc_valor
                print(f'=============> Valor per capita para {nome_membros_des} é de R${novo_percap_comdesc:.2f}!')
                desc_total+=luz_membro_desc_valor
            print(f' ================>Total do desconto: RS {desc_total:.2f}! Devera ser dividido por {luz_sem_acresc_pcap-membros_desc} membros!')
            desc_div_resto=desc_total/(luz_sem_acresc_pcap-membros_desc)
            novo_percap_semdesc=luz_sem_acresc_pcap_valor+desc_div_resto
            print(f'================> Novo valor per capita para os {luz_sem_acresc_pcap-membros_desc} membros: R${novo_percap_semdesc:.2f}')
    if desc_cons=='N':
        print(f'==============> O valor da energia descontado do acrescimo é R${luz_sem_acresc_pcap_valor:.2f} cada!'
              f'\nO valor para o membro que pagara o acrescimo é {valor_acres_pcap + luz_sem_acresc_pcap_valor:.2f}')
elif acresc_luz in 'N':
    luz_sem_acresc_pcap=int(input( f'Dividir R${luz_cons:.2f} para quantos membros ? '))
    luz_sem_acresc_pcap_valor=luz_cons/luz_sem_acresc_pcap

    desc_cons=str(input('Algum membro tera desconto por dias ausentes na republica [SIM/NÃO] ? ')).strip().upper()[0]
    if desc_cons in 'S':
        membros_desc=int(input('Quantos membros terão desconto: '))
        dias_leitura=int(input('Nº de dias equivalentes a leitura dessa conta: '))
        if membros_desc==1:
            nome_membro_desc=str(input(f'Nome do membro que requeriu desconto: '))
            dias_cons=int(input(f'Quantidade de dias que {nome_membro_desc} consumiu: '))
            days_out2=dias_leitura-dias_cons
            luz_membro_desc_valor=(luz_sem_acresc_pcap_valor/dias_leitura)*days_out2
            print(f'=============> Desconto de R$ {luz_membro_desc_valor:.2f} para {nome_membro_desc}')
            novo_percap_comdesc = luz_sem_acresc_pcap_valor - luz_membro_desc_valor
            print(f'=============> Valor per capita para {nome_membro_desc} é de R${novo_percap_comdesc:.2f}!')
            desc_total=0
            desc_total += luz_membro_desc_valor
            print(f' ================>Total do desconto: RS {desc_total:.2f}! Devera ser dividido por {luz_sem_acresc_pcap - membros_desc} membros!')
            desc_div_resto = desc_total / (luz_sem_acresc_pcap - membros_desc)
            novo_percap_semdesc = luz_sem_acresc_pcap_valor + desc_div_resto
            print(
                f'================> Novo valor per capita para os {luz_sem_acresc_pcap - membros_desc} membros: R${novo_percap_semdesc:.2f}')
        if membros_desc>1:
            desc_total=0
            desc_div_resto=0
            for c in range(1,membros_desc+1):
                nome_membros_des=str(input(f'Nome do {c}º membro que requeriu o desconto: '))
                dias_cons=int(input(f'Quantidade de dias que {nome_membros_des} consumiu: '))
                days_out2=dias_leitura-dias_cons
                luz_membro_desc_valor=(luz_sem_acresc_pcap_valor/dias_leitura)*days_out2
                print(f'=============> Desconto de R$ {luz_membro_desc_valor:.2f} para {nome_membros_des}')
                novo_percap_comdesc = luz_sem_acresc_pcap_valor - luz_membro_desc_valor
                print(f'=============> Valor per capita para {nome_membros_des} é de R${novo_percap_comdesc:.2f}!')
                desc_total+=luz_membro_desc_valor
            print(f' ================>Total do desconto: RS {desc_total:.2f}! Devera ser dividido por {luz_sem_acresc_pcap-membros_desc} membros!')
            desc_div_resto=desc_total/(luz_sem_acresc_pcap-membros_desc)
            novo_percap_semdesc=luz_sem_acresc_pcap_valor+desc_div_resto
            print(f'================> Novo valor per capita para os {luz_sem_acresc_pcap-membros_desc} membros: R${novo_percap_semdesc:.2f}')
    if desc_cons=='N':
        print(f'=====================> Valor per capita da conta de luz: R$ {luz_sem_acresc_pcap_valor:.2f}')




