# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:35:32 2019

@author: Ram Teja Chowdary
"""

import numpy as np
#Generate population
inputs=[4,-2,7,5,11,1]
num_pop=8
size_pop=len(inputs)
pop_size=(num_pop,size_pop)
new_pop=np.random.uniform(low=-10.0,high=10.0,size=pop_size)
print("Newly Generated population is.....")
print(new_pop)
#Fitness
def cal_fit(pop,inp):
    fitness=np.dot(pop,np.transpose(inp))
    return fitness
fitness=cal_fit(new_pop,inputs)
print('Fitness...')
print(fitness)

#create data frame or table having [w1,w2,w3,.....]
data={'w1':new_pop[:,0],
      'w2':new_pop[:,1],
      'w3':new_pop[:,2],
      'w4':new_pop[:,3],
      'w5':new_pop[:,4],
      'w6':new_pop[:,5],
      'fitness':fitness}
pop=['p1','p2','p3','p4','p5','p6','p7','p8']
import pandas as pd
data1=pd.DataFrame(data,index=pop)
print(data1)
#Select best population with fitness
print("Best Fitness Value",np.max(fitness))
i=np.argmax(fitness)
print('Population with Best Fitness',new_pop[i,:])

###Selection using Rank Method
mat_pol=4
def select_rank(new_pop,mat_pol,fitness):
    selected_pop=[]
    for i in range(mat_pol):
        idx=np.argmax(fitness)
        selected_pop.append(list(new_pop[idx,:]))
        fitness[idx]=-999999999
    return selected_pop
select_pop=select_rank(new_pop,mat_pol,fitness)
print('Best Four Population....')
print(select_pop)

#select using random method
mat_pol=4
def select_random(new_pop,mat_pol,fitness):
    selected_pop=[]
    for i in range(mat_pol):
        idx=np.random.randint(0,7)
        selected_pop.append(list(new_pop[idx,:]))
    return selected_pop
select_pop=select_random(new_pop,mat_pol,fitness)
print('Best Four Population....')
print(select_pop)
select_pop=np.array(select_pop)
#cross-over
def crossover(select_pop, offspring_size):
     offspring = np.empty(offspring_size)
     # The point at which crossover takes place between two parents. Usually, it is at the center.
     crossover_point = offspring_size[1]//2
 
     for k in range(offspring_size[0]):
         # Index of the first parent to mate.
         parent1_idx = k%select_pop.shape[0]
         # Index of the second parent to mate.
         parent2_idx = (k+1)%select_pop.shape[0]
         # The new offspring will have its first half of its genes taken from the first parent.
         offspring[k, 0:crossover_point] = select_pop[parent1_idx, 0:crossover_point]
         # The new offspring will have its second half of its genes taken from the second parent.
         offspring[k, crossover_point:] = select_pop[parent2_idx, crossover_point:]
     return offspring
offspring_crossover=crossover(select_pop,(num_pop-select_pop.shape[0],6)) 
print('Best Four child....')
print(offspring_crossover)

#mutation
def mutation(offspring_crossover):

    # Mutation changes a single gene in each offspring randomly.

    for idx in range(offspring_crossover.shape[0]):

        # The random value to be added to the gene.

        random_value = np.random.uniform(-1.0, 1.0, 1)

        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value

    return offspring_crossover
sel_mut=mutation(offspring_crossover)
print('After Mutation')
print(sel_mut)
 
 
 
 
 
 
    