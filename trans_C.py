# _*_ coding:utf-8 _*_
from re import T
from tkinter import *
from tkinter import messagebox
import os
import pyautogui
from time import sleep
import clipboard
import escala
import threading

class Trans_C:
    def __init__(self,n_cifra, original, mudado, text_area, id=None):

        def t_C(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    #B
                    if original.upper() == 'C' and mudado.upper() == 'A':
                        original_cifra = escala.B
                        sub = escala.A
                    
                    if original.upper() == 'C' and mudado.upper() == 'A#':
                        original_cifra = escala.B
                        sub = escala.Ast

                    if original.upper() == 'C' and mudado.upper() == 'B':
                        original_cifra = escala.B
                        sub = escala.C
                   
                    if original.upper() == 'C' and mudado.upper() == 'C#':
                        original_cifra = escala.B
                        sub = escala.Cst

                    if original.upper() == 'C' and mudado.upper() == 'D':
                        original_cifra = escala.B
                        sub = escala.D
                        
                    if original.upper() == 'C' and mudado.upper() == 'D#':
                        original_cifra = escala.B
                        sub = escala.Dst
                        
                    if original.upper() == 'C' and mudado.upper() == 'E':
                        original_cifra = escala.B
                        sub = escala.E
                                  
                    if original.upper() == 'C' and mudado.upper() == 'F':
                        original_cifra = escala.B
                        sub = escala.F

                    if original.upper() == 'C' and mudado.upper() == 'F#':
                        original_cifra = escala.B
                        sub = escala.Fst

                    if original.upper() == 'C' and mudado.upper() == 'G':
                        original_cifra = escala.B
                        sub = escala.G

                    if original.upper() == 'C' and mudado.upper() == 'G#':
                        original_cifra = escala.B
                        sub = escala.Gst


                    with open(f'temporarios/{id}.txt', 'w', encoding='utf-8') as texto:
                        texto.write(text_area)

                    with open(f'temporarios/{id}.txt', 'r', encoding='utf-8') as texto:
                        te = texto.readlines()
                        for i in range(len(te)):
                            contar = 1
                            confere = TRUE
                            if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                cifra = str(te[i])
                                confere = FALSE

                            if confere:
                                cifra = str(te[i])
                                    
                                for x in range(len(original_cifra)):

                                    #exceções
                                    if original.upper() == 'C' and mudado.upper() == 'A':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('C', 'A')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('Dm', 'Bm')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Em', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('F', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('G', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Am', 'F#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'G#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/C#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/F#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/G#')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'A#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('C', 'A#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Dm', 'Cm')
                                                    contar += 1
                                                
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('Em', 'Dm')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('F', 'D#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('G', 'F')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Am', 'Gm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'A°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/D')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/G')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/A')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'B':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('C', 'B')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('Dm', 'C#m')
                                                    contar += 1
                                                
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('Em', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('F', 'E')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('G', 'F#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Am', 'G#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'A#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/D#')

                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/G#')

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/A#')
             
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'C#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('C', 'C#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Dm', 'D#m')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Em', 'Fm')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('F', 'F#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('G', 'G#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Am', 'A#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'C°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/F')

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/A#')

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/C')
                                                    
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'D':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('C', 'D')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('Dm', 'Em')
                                                    contar += 1
                                                
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('Em', 'F#m')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('F', 'G')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'A')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Am', 'Bm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'C#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/F#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/B')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/C#')
                                                    contar += 1 
             
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'D#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('C', 'D#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'Fm')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Em', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('F', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'A#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Am', 'Cm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'D°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/E', '/G')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/A', '/C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/D')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'E':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('C', 'E')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'F#m')
                                                    contar += 1                                       
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('Em', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('F', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'B')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Am', 'C#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'D#°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/E', '/G#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/A', '/C#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/D#')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'F':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('C', 'F')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'Gm')
                                                    contar += 1                                        
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('Em', 'Am')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('F', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'C')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Am', 'Dm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'E°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/A')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/D')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/E')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'F#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('C', 'F#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'G#m')
                                                    contar += 1                                        
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('Em', 'A#m')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('F', 'B')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'C#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Am', 'D#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'F°')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/E', '/A#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/D#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/F')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'G':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 5:
                                                    cifra = cifra.replace('C', 'G')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('Dm', 'Am')
                                                    contar += 1                                       
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('Em', 'Bm')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('F', 'C')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('G', 'D')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('Am', 'Em')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'F#°')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/E', '/B')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/E')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/F#')
                                                    contar += 1

                                                    break
                                                break

                                    elif original.upper() == 'C' and mudado.upper() == 'G#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('C', 'A')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('Dm', 'Bm')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Em', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('F', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('G', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Am', 'F#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('B°', 'G#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/C#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/F#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/G#')
                                                    contar += 1
             
                                                    break
                                                break
                                                
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('A', 'G#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('Bm', 'A#m')
                                                    contar += 1                                       
                                                
                                                if contar == 13:
                                                    cifra = cifra.replace('C#m', 'Cm')
                                                    contar += 1
                                                                                        
                                                if contar == 14:
                                                    cifra = cifra.replace('D', 'C#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 15:
                                                    cifra = cifra.replace('E', 'D#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 16:
                                                    cifra = cifra.replace('F#m', 'Fm')
                                                    contar += 1
                                                    
                                                if contar == 17:
                                                    cifra = cifra.replace('G#°', 'G°')
                                                    contar += 1
                                                
                                                if contar == 18:
                                                    cifra = cifra.replace('/C#', '/C')
                                                    contar += 1

                                                if contar == 19:
                                                    cifra = cifra.replace('/F#', '/F')
                                                    contar += 1

                                                if contar == 20:
                                                    cifra = cifra.replace('/G#', '/G')
                                                    contar += 1
                                                    break
                                                break
                                            
                                    else:
                                        contar = 1
                                        cifra = cifra.replace(str(original_cifra[x]), str(sub[x]))
                                        cifra = cifra.replace('##', '#')
                                        
                                    if mudado.upper() == 'B' and original.upper() == 'A':
                                        cifra = cifra.replace('/F#', '/D#')
                                        cifra = cifra.replace('B#', 'A#')

                            sleep(0.01)
                            

                            try:
                                if original.upper() == 'C' and mudado.upper() == 'C#':
                                    cifra = cifra.replace('/B', '/C')
                                cifra = cifra.replace('##', '#')
                                cifra = cifra.replace('A/A', 'A/C#')
                                cifra = cifra.replace('A9/A', 'A9/C#')
                                cifra = cifra.replace('A#/A#', 'A#/D')
                                cifra = cifra.replace('A#9/A#', 'A#9/D')
                                cifra = cifra.replace('B/B', 'B/D#')
                                cifra = cifra.replace('B9/B', 'B9/D#')
                                cifra = cifra.replace('C/C', 'C/E')
                                cifra = cifra.replace('C9/C', 'C9/E')
                                cifra = cifra.replace('C#/C#', 'C#/F')
                                cifra = cifra.replace('C#9/C', 'C#9/F')
                                cifra = cifra.replace('D/D', 'D/F#')
                                cifra = cifra.replace('D9/D', 'D9/F#')
                                cifra = cifra.replace('D#/D#', 'D#/G')
                                cifra = cifra.replace('D#9/D#', 'D#9/G')
                                cifra = cifra.replace('G/G', 'G/B')
                                cifra = cifra.replace('G#/G#', 'G#/C')
                                cifra = cifra.replace('G#/A#', 'G#/C')
                                cifra = cifra.replace('E/F#', 'E/G#')
                                cifra = cifra.replace('F/G#', 'F/A')
                                cifra = cifra.replace('C#/D#', 'C#/F')
                                cifra = cifra.replace('D/E#', 'D/F#')
                                cifra = cifra.replace('D#/F#', 'D#/G')
                                
                            except: pass
                            with open(fr'Minhas_cifras/{n_cifra}.txt', 'a', encoding='utf-8') as arquivo:
                                arquivo.write(str(cifra))

                except Exception as error:
                    erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}'
            else:
                erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!'
        threading.Thread(target=t_C(self)).start()
