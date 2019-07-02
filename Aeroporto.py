#./bin/python3
#coding: utf-8

import simpy
import dados_da_simulação as rawData

class Aviao:
  def __init__(self, env, nome, tempo_chegada, tempo_hangar, porte):
    self.env = env
    self.nome = nome
    self.t_chegada = tempo_chegada
    self.t_hangar = tempo_hangar
    self.porte = porte
    self.t_pouso_decolagem = 10
    self.t_embarque = 30
    self.t_desembarque = 15
    self.log = ''
    if (porte == 1):
      self.t_pouso_decolagem = 20
      self.t_embarque = 45
      self.t_desembarque = 30

class Aeroporto:
  def __init__(self, env, plataformas, hangares, pistaPp, pistaGp):
    self.plataformas = plataformas
    self.hangares = hangares
    self.pistaPp = pistaPp
    self.pistaGp = pistaGp
    self.log = ''

  def embarque(self):

  def desembarque(self):
    
  def pouso(self, aviao):
    self.log += 'Aviao {} chegou em {}.\n'.format()
    yield self.env.timeout(aviao.tempo_chegada)
    if (aviao.porte == 0):
      with self.pistaPp.request() as pistaPP:
        yield pistaPP
        yield self.pistaPp.get(1)
        yield self.env.timeout(aviao.t_pouso_decolagem)
        
    else:
      with self.pistaGp.request() as pistaGP:
        yield pistaGP
        yield self.pistaGp.get(1)
        yield self.env.timeout(aviao.t_pouso_decolagem)

  def decolagem(self):

  def preparando(self):

def parseData():
  data = []
  for i in range(0, len(rawData.chegadas)):
    data.append((rawData.chegadas[i], rawData.permanencia_hangar[i], rawData.tipos_voos[i]))
  return data

if __name__ == '__main__':
  data = parseData()
  env = simpy.Environment()
  plataformas = simpy.Resource(env, capacity=5)
  hangares = simpy.Resource(env, capacity=3)
  pistaPp = simpy.Resource(env, capacity=2)
  pistaGp = simpy.Resource(env, capacity=1)
  avioes = []
  planeId = 0
  for item in data:
    avioes.append(Aviao(env, planeId, data[i][0], data[i][1], data[i][2]))
    planeId += 1

