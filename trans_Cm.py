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


class Trans_Cm:
    def __init__(self,n_cifra, original, mudado, text_area, id=None):

        def t_Cm(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    
                    if original == 'Cm' and mudado == 'Am':
                        original_cifra = escala.A
                        sub = escala.Ast
                    
                    if original == 'Cm' and mudado == 'A#m':
                        original_cifra = escala.A
                        sub = escala.B

                    if original == 'Cm' and mudado == 'Bm':
                        original_cifra = escala.A
                        sub = escala.C
                   
                    if original == 'Cm' and mudado == 'C#m':
                        original_cifra = escala.A
                        sub = escala.Cst

                    if original == 'Cm' and mudado == 'Dm':
                        original_cifra = escala.A
                        sub = escala.D
                        
                    if original == 'Cm' and mudado == 'D#m':
                        original_cifra = escala.A
                        sub = escala.Dst
                        
                    if original == 'Cm' and mudado == 'Em':
                        original_cifra = escala.A
                        sub = escala.E
                                  
                    if original == 'Cm' and mudado == 'Fm':
                        original_cifra = escala.A
                        sub = escala.F

                    if original == 'Cm' and mudado == 'F#m':
                        original_cifra = escala.A
                        sub = escala.Fst

                    if original == 'Cm' and mudado == 'Gm':
                        original_cifra = escala.A
                        sub = escala.G

                    if original == 'Cm' and mudado == 'G#m':
                        original_cifra = escala.A
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

                                    if original == 'Cm' and mudado == 'Am':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'Am')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('D#', 'C')
                                                    contar += 1
                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('Fm', 'Dm')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('G', 'E')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('G#', 'F')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('A#', 'G')
                                                    contar += 1
                                                    
                                                if contar == 6:
                                                    cifra = cifra.replace('/G', '/E')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/B', '/G#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/A')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/B')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('D', 'B')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'D°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'C')
                                                    contar +=1
             
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'A#m':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('Cm', 'A#m')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('D#', 'C#')
                                                    contar += 1
                                                                                       
                                                if contar == 12:
                                                    cifra = cifra.replace('Fm', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'F')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('G#', 'F#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('A#', 'G#')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('/G', '/F')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('/B', '/A')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/C', '/A#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/D', '/C')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('D', 'C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('F°', 'D#°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'C#')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'Bm':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Cm', 'Bm')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('D#', '2re')
                                                    contar += 1
                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Fm', 'Em')
                                                    contar += 1
                                                                                        
                                                if contar == 7:
                                                    cifra = cifra.replace('G', 'F#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('G#', 'sol')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('A#', 'A')
                                                    contar += 1
                                                    
                                                if contar == 5:
                                                    cifra = cifra.replace('/G', '/F#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/A#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/B')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/D', '/C#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('D', 'C#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'E°')
                                                    contar += 1
                                                    
                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'D')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'C#m':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 8:
                                                    cifra = cifra.replace('Cm', 'C#m')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('D#', 'E')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('Fm', 'F#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('G#', 'A')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('A#', 'B')
                                                    contar += 1
                                                    
                                                if contar == 5:
                                                    cifra = cifra.replace('/G', '/G#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/C')
                                                    contar += 1
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('/C', '/C#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/D', '/D#')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('D', 'D#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'F#°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'E')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'Dm':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('Cm', 'Dm')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('D#', 'F')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('Fm', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 8:
                                                    cifra = cifra.replace('G', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('G#', 'A#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('A#', 'C')
                                                    contar += 1
                                                    
                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/A')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/B', '/C#')
                                                    contar += 1
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('/C', '/D')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('/D', '/E')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('D', 'E')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'G°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'F')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'D#m':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('Cm', 'D#m')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('D#', 'fast')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('Fm', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 8:
                                                    cifra = cifra.replace('G', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('G#', 'B')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('A#', 'C#')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('/G', '/A#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/D')
                                                    contar += 1
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('/C', '/D#')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('/D', '/F')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('D', 'F')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'G#°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'F#')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'Em':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Cm', '3mim')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('D#', '5sol')
                                                    contar += 1
                                                                                       
                                                if contar == 11:
                                                    cifra = cifra.replace('Fm', '6lam')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('G', '7si')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('G#', '1do')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('A#', '2re')
                                                    contar += 1
                                                    
                                                if contar == 10:
                                                    cifra = cifra.replace('/G', '/B')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/D#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/E')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/D', '/F#')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('D', 'F#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'A°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'G')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'Fm':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('Cm', 'Fm')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('D#', '5sol#')
                                                    contar += 1
                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('Fm', '6la#m')
                                                    contar += 1
                                                                                        
                                                if contar == 10:
                                                    cifra = cifra.replace('G', 'C')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('G#', 'C#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('A#', '2re#')
                                                    contar += 1
                                                    
                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/C')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/E')
                                                    contar += 1
                                                
                                                if contar == 7:
                                                    cifra = cifra.replace('/C', '/F')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/D', '/G')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('D', 'G')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'A#°')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Eb', 'G#')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'F#m':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Cm', 'F#m')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('D#', 'A')
                                                    contar += 1
                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('Fm', 'Bm')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('G', 'dosust')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('G#', '2re')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('A#', 'E')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('/G', '/C#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/F')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/F#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/D', '/G#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('D', '5#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('F°', 'B°')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('Eb', 'A')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'Gm':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 12:
                                                    cifra = cifra.replace('Cm', 'Gm')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('D#', 'A#')
                                                    contar += 1
                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Fm', '1dom')
                                                    contar += 1
                                                                                        
                                                if contar == 9:
                                                    cifra = cifra.replace('G', '2re')
                                                    contar += 1
                                                                                                                               
                                                if contar == 8:
                                                    cifra = cifra.replace('G#', '2re#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('A#', 'F')
                                                    contar += 1
                                                    
                                                if contar == 6:
                                                    cifra = cifra.replace('/G', '/2re')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/B', '/F#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/C', '/5sol')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/D', '/A')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('D', 'A')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('F°', 'C°')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Eb', 'A#')
                                                    contar += 1

                                                    break
                                                break

                                    elif original == 'Cm' and mudado == 'G#m':
                                        
                                        if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                            cifra = str(te[i])
                                            confere = FALSE
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('Cm', '5sol#m')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('D#', 'B')
                                                    contar += 1
                                                                                       
                                                if contar == 12:
                                                    cifra = cifra.replace('Fm', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 8:
                                                    cifra = cifra.replace('G', '2re#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 7:
                                                    cifra = cifra.replace('G#', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('A#', 'F#')
                                                    contar += 1
                                                    
                                                if contar == 1:
                                                    cifra = cifra.replace('/G', '/2re#')
                                                    contar += 1

                                                if contar == 13:
                                                    cifra = cifra.replace('/B', '/G')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/G#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/D', '/6la#')
                                                    contar += 1

                                                if contar ==10:
                                                    cifra = cifra.replace('D', 'A#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('F°', 'C#°')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('Eb', 'B')
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

                                    if mudado.upper() == 'C':
                                        cifra = cifra.replace('#', '')
                                        
                                    if mudado.upper() == 'A#' and original.upper() == 'A':
                                        cifra = cifra.replace('/D#', '/D')
                                        cifra = cifra.replace('/A#', '/A')
                                    if mudado.upper() == 'B' and original.upper() == 'A':
                                        cifra = cifra.replace('/F#', '/D#')
                                        cifra = cifra.replace('/E#', '/D#')
                                    if mudado.upper() == 'C#' and original.upper() == 'A':
                                            cifra = cifra.replace('C#9/F#', 'C#9/F')
                                    if mudado.upper() == 'C' and original.upper() == 'A':
                                            cifra = cifra.replace('Fm', 'Dm')

                            sleep(0.01)


                            try:
                                cifra = cifra.replace('fast', 'F#')
                                cifra = cifra.replace('Bb', 'A#')
                                cifra = cifra.replace('Eb', 'D#')
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
                                cifra = cifra.replace('3°', 'E°')
                                cifra = cifra.replace('4#', 'F#')
                                cifra = cifra.replace('5#', 'G#')
                                cifra = cifra.replace('12mm', 'C')
                                cifra = cifra.replace('m2', 'F')
                                cifra = cifra.replace('11m', 'Cm')
                                cifra = cifra.replace('dost', 'C#')
                                cifra = cifra.replace('dosust', 'C#')
                                cifra = cifra.replace('1do', 'C')
                                cifra = cifra.replace('2re', 'D')
                                cifra = cifra.replace('3mi', 'E')
                                cifra = cifra.replace('4fa', 'F')
                                cifra = cifra.replace('5sol', 'G')
                                cifra = cifra.replace('6la', 'A')
                                cifra = cifra.replace('7si', 'B')
                                
                                
                            except: pass
                            with open(fr'Minhas_cifras/{n_cifra}.txt', 'a', encoding='utf-8') as arquivo:
                                arquivo.write(str(cifra))

                except Exception as error:
                    erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}'
            else:
                erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!'
        threading.Thread(target=t_Cm(self)).start()
