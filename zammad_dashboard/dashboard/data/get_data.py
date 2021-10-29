import pandas as pd
import shlex
import subprocess
import json


def all_tickets():
    df = pd.DataFrame()
    page = 1

    while True:
        cmd =  '''curl -u noreply.std@ufrpe.br:OCeania@49 https://servicosdigitais.ufrpe.br/api/v1/tickets?expand=true&page=''' + str(page) + '''&per_page=100'''

        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        process.wait()

        df_aux = pd.DataFrame(json.loads(stdout.decode()))

        if len(df_aux.columns) > 52:
            df_aux.drop(columns=df_aux.columns[-1], axis=1, inplace=True)

        
        if df_aux.empty:    
            break

        df = df.append(df_aux, ignore_index=True)

        print("[GETTING PAGE: " + str(page) + "]")
        page += 1

    return df


def all_users():
    df = pd.DataFrame()
    page = 1

    while True:
        cmd =  '''curl -u noreply.std@ufrpe.br:OCeania@49 https://servicosdigitais.ufrpe.br/api/v1/users?expand=true&page=''' + str(page) + '''&per_page=100'''

        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        process.wait()

        df_aux = pd.DataFrame(json.loads(stdout.decode()))

        if len(df_aux.columns) > 52:
            df_aux.drop(columns=df_aux.columns[-1], axis=1, inplace=True)

        
        if df_aux.empty:    
            break

        df = df.append(df_aux, ignore_index=True)

        print("[GETTING PAGE: " + str(page) + "]")
        page += 1

    return df



def cleaning_data():
    
    #df_tickets = all_tickets()
    #df_tickets.to_csv('all_tickets.csv', header=True)
    df_tickets = pd.read_csv('zammad_dashboard/dashboard/data/all_tickets.csv', header=0, dtype='object')

    ###################################### consertando os dados ##################################################
    df_tickets['close_at'] = pd.to_datetime(df_tickets['close_at'])
    df_tickets['created_at'] = pd.to_datetime(df_tickets['created_at'])
    df_tickets['first_response_at'] = pd.to_datetime(df_tickets['first_response_at'])

    estados = {"closed":"Fechado",
                  "open":"Aberto",
                  "resolvido":"Resolvido",
                  "new":"Novo",
                  "aguardando resposta":"Aguardando Resposta",
                  "pendente":"Pendente",
                  "retorno":"Retorno",
                  }

    df_tickets['state'] = df_tickets['state'].map(estados)


    
    tempo_medio_fechar_chamado_hora = (df_tickets.loc[df_tickets['state'] == "Fechado", 'close_at'] - df_tickets.loc[df_tickets['state'] == "Fechado", 'created_at']).astype('timedelta64[h]').median()
    

    ########################################################################################
    df_first_response_at = df_tickets.copy()
    df_first_response_at = df_first_response_at.dropna(axis=0, subset=['first_response_at'])
    tempo_medio_primeiro_contato_minuto = (df_first_response_at['first_response_at'] - df_first_response_at['created_at']).astype('timedelta64[m]').median()


    ########################################################################################
    df_created = df_tickets.copy()
    df_created.drop(columns=df_created.columns.difference(['created_at', 'state']).tolist(), axis=1, inplace=True)
    df_created.set_index('created_at', inplace=True)

    df_created.index = df_created.index.date
    df_created = df_created.loc[df_created.index >= pd.to_datetime("2021-10-6").date()]
    df_created.index.name = 'created_at'
    
    df_created['qnt'] = [1] * len(df_created.index)
    df_created = df_created.groupby(['created_at', 'state']).sum()
    df_created = df_created.reset_index(level=[1])

    media_fechar_chamado_dia = df_created.loc[df_created['state'] == "Fechado", 'qnt'].median()
    media_aberto_chamado_dia = df_created.loc[df_created['state'] == "Aberto", 'qnt'].median()

    #df_users = all_users()
    #df_users.to_csv('all_users.csv', header=True)
    df_users = pd.read_csv('zammad_dashboard/dashboard/data/all_users.csv', header=0, dtype='object')

    categorias = {"Docente                       \n":"Docente",
                  "Docente": "Docente",
                   'Discente':'Discente',
                   'Técnico Administrativo':'Técnico Administrativo',
                   'Não especificado':'Não especificado',
                   'Discente / Estagiário':'Discente / Estagiário',
                   'TERCERIZADO':'TERCERIZADO',
                   'Terceirizado - Construcel':'Terceirizado - Construcel',
                  }

    df_users['categoria'] = df_users['categoria'].map(categorias)

    ###########################################################################################
    df_joined = df_tickets.set_index('customer').join(df_users.set_index('login'), lsuffix='_left')

    return {'tempo-medio-fechar-chamado-hora': tempo_medio_fechar_chamado_hora,
        'tempo-medio-primeiro-contato-minuto': tempo_medio_primeiro_contato_minuto,
        'media-fechar-chamado-dia': media_fechar_chamado_dia,
        'media-aberto-chamado-dia': media_aberto_chamado_dia,
        'df-created': df_created,
        'df-joined': df_joined,
        }