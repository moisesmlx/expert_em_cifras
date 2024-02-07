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


class Trans_Fst:
    def __init__(self, n_cifra, original, mudado, text_area, id=None):

        def t_Fst(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    #B
                    if original.upper() == 'F#' and mudado.upper() == 'A':
                        original_cifra = escala.B
                        sub = escala.A
                    
                    if original.upper() == 'F#' and mudado.upper() == 'A#':
                        original_cifra = escala.B
                        sub = escala.Ast

                    if original.upper() == 'F#' and mudado.upper() == 'B':
                        original_cifra = escala.B
                        sub = escala.C
                   
                    if original.upper() == 'F#' and mudado.upper() == 'C':
                        original_cifra = escala.B
                        sub = escala.Cst

                    if original.upper() == 'F#' and mudado.upper() == 'C#':
                        original_cifra = escala.B
                        sub = escala.D
                        
                    if original.upper() == 'F#' and mudado.upper() == 'D':
                        original_cifra = escala.B
                        sub = escala.Dst
                        
                    if original.upper() == 'F#' and mudado.upper() == 'D#':
                        original_cifra = escala.B
                        sub = escala.E
                                  
                    if original.upper() == 'F#' and mudado.upper() == 'E':
                        original_cifra = escala.B
                        sub = escala.F

                    if original.upper() == 'F#' and mudado.upper() == 'F':
                        original_cifra = escala.B
                        sub = escala.Fst

                    if original.upper() == 'F#' and mudado.upper() == 'G':
                        original_cifra = escala.B
                        sub = escala.G

                    if original.upper() == 'F#' and mudado.upper() == 'G#':
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
                                    if original.upper() == 'F#' and mudado.upper() == 'A':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('F#', 'A')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('G#m', 'Bm')
                                                    contar += 1
                                                
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('A#m', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('B', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('C#', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('D#m', 'F#m')
                                                    contar += 1
                                                    
                                                if contar == 3:
                                                    cifra = cifra.replace('F°', 'G#°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/C#')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/D#', '/F#')
                                                    contar += 1
                                                
                                                if contar == 2:
                                                    cifra = cifra.replace('/F', '/G#')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'A#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('F#', 'A#')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('G#m', 'Cm')
                                                    contar += 1                                        
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('A#m', 'Dm')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('B', 'D#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('C#', 'F')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('D#m', 'Gm')
                                                    contar += 1
                                                    
                                                if contar == 2:
                                                    cifra = cifra.replace('F°', 'A°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/D')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/D#', '/G')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/F', '/A')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'B':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('F#', 'A')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('G#m', 'Bm')
                                                    contar += 1
                                                
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('A#m', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('B', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('C#', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('D#m', 'F#m')
                                                    contar += 1
                                                    
                                                if contar == 3:
                                                    cifra = cifra.replace('F°', 'G#°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/C#')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/D#', '/F#')
                                                    contar += 1
                                                
                                                if contar == 2:
                                                    cifra = cifra.replace('/F', '/G#')
                                                    contar += 1
             
                                                    #break
                                                break
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('A', 'B')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Bm', 'C#m')
                                                    contar += 1
                                                
                                                
                                                if contar == 12:
                                                    cifra = cifra.replace('C#m', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 16:
                                                    cifra = cifra.replace('D', 'E')
                                                    contar += 1
                                                                                                                               
                                                if contar == 14:
                                                    cifra = cifra.replace('E', 'F#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 15:
                                                    cifra = cifra.replace('F#m', 'G#m')
                                                    contar += 1
                                                    
                                                if contar == 17:
                                                    cifra = cifra.replace('G#°', 'A#°')
                                                    contar += 1

                                                if contar == 18:
                                                    cifra = cifra.replace('/C#', '/D#')
                                                    contar += 1
                                                
                                                if contar == 19:
                                                    cifra = cifra.replace('/F#', '/G#')
                                                    contar += 1
                                                
                                                if contar == 20:
                                                    cifra = cifra.replace('/G#', '/A#')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'C':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:


                                            while TRUE:
                                                if contar == 5:
                                                    cifra = cifra.replace('F#', 'C')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('G#m', 'Dm')
                                                    contar += 1
                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('A#m', 'Em')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('B', 'F')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('C#', 'G')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('D#m', 'Am')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('F°', 'B°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/E')

                                                if contar == 10:
                                                    cifra = cifra.replace('/D#', '/A')

                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/B')
                                                    
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'C#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('F#', 'C#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('G#m', 'D#m')
                                                    contar += 1
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('A#m', 'Fm')
                                                    contar += 1
                                                                                        
                                                if contar == 7:
                                                    cifra = cifra.replace('B', 'F#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('C#', 'G#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('D#m', 'A#m')
                                                    contar += 1
                                                    
                                                if contar == 2:
                                                    cifra = cifra.replace('F°', 'C°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/F')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/D#', '/A#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/C')
                                                    contar += 1 
             
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'D':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('F#', 'D')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('G#m', 'Em')
                                                    contar += 1
                                                
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('A#m', 'F#m')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('B', 'G')
                                                    contar += 1
                                                                                                                               
                                                if contar == 6:
                                                    cifra = cifra.replace('C#', 'A')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('D#m', 'Bm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('F°', 'C#°')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A#', '/F#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D#', '/B')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/F', '/C#')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'D#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('F#', 'D#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('G#m', 'Fm')
                                                    contar += 1                                       
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('A#m', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('B', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('C#', 'A#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('D#m', 'Cm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('F°', 'D°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/G')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D#', '/C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/F', '/D')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'E':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('F#', 'E')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('G#m', 'F#m')
                                                    contar += 1                                        
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('A#m', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('B', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 6:
                                                    cifra = cifra.replace('C#', 'B')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 7:
                                                    cifra = cifra.replace('D#m', 'C#m')
                                                    contar += 1
                                                    
                                                if contar == 1:
                                                    cifra = cifra.replace('F°', 'D#°')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A#', '/G#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D#', '/C#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/F', '/D#')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'F':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('F#', 'F')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('G#m', 'Gm')
                                                    contar += 1                                        
                                                
                                                if contar == 2:
                                                    cifra = cifra.replace('A#m', 'Am')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('B', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('C#', 'C')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('D#m', 'Dm')
                                                    contar += 1
                                                    
                                                if contar == 3:
                                                    cifra = cifra.replace('F°', 'E°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/A')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/D#', '/D')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/E')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'G':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('F#', 'G')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('G#m', 'Am')
                                                    contar += 1                                       
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('A#m', 'Bm')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('B', 'C')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('C#', 'D')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('D#m', 'Em')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('F°', 'F#°')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/B')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/D#', '/E')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/F#')
                                                    contar += 1

                                                    break
                                                break

                                    elif original.upper() == 'F#' and mudado.upper() == 'G#':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('F#', 'G#')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('G#m', 'A#m')
                                                    contar += 1                                       
                                                
                                                if contar == 2:
                                                    cifra = cifra.replace('A#m', 'Cm')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('B', 'C#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('C#', 'D#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('D#m', 'Fm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('F°', 'G°')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A#', '/C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/D#', '/F')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/G')
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
                                cifra = cifra.replace('F#/C', 'F#/A#')
                                cifra = cifra.replace('A#/D#', 'A#/D')
                                cifra = cifra.replace('F#/A##', 'F#/A#')
                                cifra = cifra.replace('G/C#', 'G/B')
                                cifra = cifra.replace('B/G', 'B/D#')
                                cifra = cifra.replace('B9/G', 'B9/D#')
                                cifra = cifra.replace('Eb', 'D#')
                                cifra = cifra.replace('Bb', 'A#')
                                cifra = cifra.replace('G/D', 'G/B')
                                cifra = cifra.replace('/D##', '/D#')
                                cifra = cifra.replace('/B#', '/B')
                                cifra = cifra.replace('B#', 'F#')
                                cifra = cifra.replace('B9/A', 'B9/D#')
                                cifra = cifra.replace('B/A', 'B/D#')
                                cifra = cifra.replace('F#/E', 'F#/A#')
                                cifra = cifra.replace('C9/A', 'C9/E')
                                cifra = cifra.replace('C/A', 'C/E')
                                cifra = cifra.replace('/E#', '/E')
                                
                            except: pass
                            with open(fr'Minhas_cifras/{n_cifra}.txt', 'a', encoding='utf-8') as arquivo:
                                arquivo.write(str(cifra))

                except Exception as error:
                    erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}'
            else:
                erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!'
        
        threading.Thread(target=t_Fst(self)).start()
