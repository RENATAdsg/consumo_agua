#Entrada de dados, Saudação e pedidos.

print("Olá, seja bem_vindo(a)")
imovél=input("Digite qual seu Imovél(ex: Casa, comercial ou apartamento):"). lower()
consumo_agua=float(input("Digite o consumo mensal de agua em M³(Metros cúbicos):"))

#Processamento de dados 
if imovél == "comercial":
    print("Tarifa comercial aplicada, consulte o plano corporativo.")

elif consumo_agua <10 and imovél == "apartamento":
    print("Consumo econômico, excelente controle de água!")

elif (imovél == "apartamento" or imovél == "casa") and consumo_agua <= 25:
    print("Consumo moderado, dentro do padrão residencial.")

else:
    print("Consumo excessivo, adote medidas de economia e verifique vazamentos.")    

print("Agradecemos pela preferência em nosso sistema!")
