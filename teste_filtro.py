import numpy as np
from itertools import combinations, permutations
import streamlit as st

class Armstrong_Modulator():
    def __init__(self, f1, df1, f4, df4, f0):
        self.f1 = f1
        self.df1 = df1
        self.f4 = f4
        self.df4 = df4
        self.f0 = f0

    def n_value(self):
        N = self.df4/self.df1
        print(f"Valor de N: {N}")
        return N

    def possibilities_mult(self):
        N = self.n_value()
        all_poss = list(set(x for tup in ([i, N//i]
                for i in range(1, int(N**0.5)+1) if N % i == 0) for x in tup))

        comb_2_2 = list(permutations(all_poss, 2))
        possibilities = []
        for poss in comb_2_2:
            if poss[0]*poss[1] == N:
                possibilities.append(poss)
            else:
                continue

        return possibilities

    def f2_f3_f0(self):
        possibilities = self.possibilities_mult()
        response = []
        response_f0_r = []
        for possible_poss in possibilities:
            f2 = self.f1*possible_poss[0]
            f3 = self.f4/possible_poss[1]
            f0_r = abs(f2-f3)
            if f0_r >= self.f0[0] and f0_r <= self.f0[1]:
                response.append(possible_poss)
                response_f0_r.append(f0_r)
            else:
                continue

        for i in range(len(response)):
            st.write(f"Possibilidade {i+1}: N1 = {int(response[i][0])}; \t N2 = {int(response[i][1])}; \t f0 = {int(response_f0_r[i])} Hz")

            print(f"Possibilidade {i+1}: N1 = {response[i][0]}; \t N2 = {response[i][1]}; \t f0 = {response_f0_r[i]} Hz")
       # print(f"As possiveis respostas são: {response}")
       # print(f"os f0 são: {response_f0_r}")
        return response












