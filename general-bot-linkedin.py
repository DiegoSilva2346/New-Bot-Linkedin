from selenium.webdriver.support.ui import WebDriverWait     
from selenium import webdriver    
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By          
from selenium.webdriver.common.keys import Keys
import time         
import random        
from email_password import login       



class Linkedin:
    def __init__(self,username,password,direccion_url,numero_de_recruiter,numero_python_developer,numero_java_developer,numero_php_developer):
        self.username=username
        self.password=password         
        self.options=webdriver.ChromeOptions()      
        self.options.add_argument('--start-maximized')   
        self.options.add_argument('--disable-extensions')   
        self.driver_path="C:/escritorio/Python/bot/chromedriver.exe"    
        self.direccion_url=direccion_url        
        self.bot=webdriver.Chrome(self.driver_path,chrome_options=self.options)         
        self.numero_de_recruiter=numero_de_recruiter        
        self.numero_python_developer=numero_python_developer        
        self.numero_java_developer=numero_java_developer    
        self.numero_php_developer=numero_php_developer

    
    def login(self):           

        
       
        self.bot.get(self.direccion_url)
        time.sleep(random.uniform(6,9.5))
        email=self.bot.find_element_by_id("username")
        email.send_keys(self.username)        
        time.sleep(random.uniform(3,8))
        password=self.bot.find_element_by_id("password")
        password.send_keys(self.password)
        time.sleep(random.uniform(1.6,3.9))
        password.send_keys(Keys.RETURN)          

    
  
    

    
    def select_recruiter(self,url,numero_invitaciones):   
      numero_invitaciones=int(numero_invitaciones)
      contador=0          
      contador_de_pagina=1          
      self.bot.get(url)           
      time.sleep(random.uniform(5,9))
      while contador!= numero_invitaciones or contador_de_pagina!=101:          
              
       try:             
        lista_personas=self.bot.find_elements_by_xpath("//button[text()='Conectar']")     
        print(lista_personas)         
        print(len(lista_personas))         

        elige_recruiter=random.randint(0,len(lista_personas))        
        print(elige_recruiter)       
       
        


               
        time.sleep(random.uniform(1,4)) 
               
        print(lista_personas)     
              
        self.bot.execute_script("arguments[0].click();",lista_personas[elige_recruiter])#Conectar      
                
        time.sleep(random.uniform(0.7,2))        
               
        enviar=self.bot.find_element_by_xpath("//span[text()='Enviar']").click()#enviar
                 
        contador=contador+1           
        print("contador=" +str(contador))          
        print("numero_invitaciones="+str(numero_invitaciones))          
        if contador==numero_invitaciones or contador_de_pagina==101:      
          break 
          
         
         
         
       except:          
            contador_de_pagina=contador_de_pagina+1         
            self.bot.get(url+"&page="+str(contador_de_pagina))       
            time.sleep(random.uniform(3,6))  
    def go_a_recruiter(self):        
        time.sleep(random.uniform(6,10))       
        numero=self.numero_de_recruiter         
        load.select_recruiter("https://www.linkedin.com/search/results/people/?keywords=recruiter&origin=SWITCH_SEARCH_VERTICAL",numero)    
        numero=self.numero_python_developer     
        load.select_recruiter("https://www.linkedin.com/search/results/people/?keywords=python%20developer&origin=SWITCH_SEARCH_VERTICAL",numero)    
        numero=self.numero_java_developer          
        load.select_recruiter("https://www.linkedin.com/search/results/people/?keywords=java%20developer&origin=GLOBAL_SEARCH_HEADER",numero)     
        numero=self.numero_php_developer            
        load.select_recruiter("https://www.linkedin.com/search/results/people/?keywords=php%20developer&origin=GLOBAL_SEARCH_HEADER",numero)    





load=Linkedin(login()[0],login()[1],"https://www.linkedin.com/uas/login",2,2,1,1)
load.login()
load.go_a_recruiter()         
