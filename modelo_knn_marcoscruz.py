#!/usr/bin/env python
# coding: utf-8

# In[4]:


class knn_classificacao:
    def __init__(self,k,no_class,data):
        self.k = k 
        self.no_class = no_class
        self.data = data 

    def calculo_distancia(self,usuario_desconhecido,usuario_conhecido):
        investimento_usuario_conhecido = usuario_conhecido[2]
        investimento_usuario_desconhecido = usuario_desconhecido[2]
        termos = 0 
        for iconhecido, idesconhecido in zip(investimento_usuario_conhecido,investimento_usuario_desconhecido):
            termos +=  (iconhecido - idesconhecido)**2 
        termos = termos**0.5
        return termos 

    def classificar_um (self,usuario_desconhecido):
        classes = []
        distancias = []
        for i in range (len(self.data)):
            distancias.append (self.calculo_distancia(usuario_desconhecido,self.data[i]))
            classes.append (self.data[i][1])
        classes_distancias=list(zip(classes,distancias))
        classes_distancias_organizado = sorted(classes_distancias, key=lambda x: x[1])

        contador = 0
        maior = 0
        n_conservador = 0
        n_moderado = 0
        n_agressivo = 0 
        maior_nome = ''

        for contador in range (self.k):
            if  classes_distancias_organizado [contador][0] == 'Conservador':
                n_conservador = n_conservador + 1
            elif classes_distancias_organizado [contador][0] == 'Moderado':
                n_moderado = n_moderado + 1
            elif classes_distancias_organizado [contador][0] == 'Agressivo':
                n_agressivo = n_agressivo + 1



        if (n_conservador >= n_moderado) and (n_conservador >= n_agressivo):
            maior = n_conservador
            maior_nome = 'Conservador'

        elif (n_moderado >= n_conservador) and (n_moderado >= n_agressivo):
            maior = n_moderado
            maior_nome = 'Moderado'

        else:
            maior = n_agressivo
            maior_nome = 'Agressivo'

        return maior_nome , maior 
    
    def classificar (self):
        respota_dicionario = {}
        for i in range (len(self.no_class)):
            respota_dicionario[self.no_class[i][0]] = self.classificar_um(self.no_class[i])
        return respota_dicionario

