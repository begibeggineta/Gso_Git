#Bergþór Ingi Birgirsson
#GSÖ2
#25.1.2017
Text = input("veldu hvað txt skjalið á að heita")
F = open(Text+".txt","w+")

F.write("Hello my honey Hello my baby hello my night time gaaal")
F.close()
F = open(Text+".txt","+w")
innhald = input("Hvað viltu skrifa inn í texta skjalið")
for i in range(0,3):
    F.write(innhald +"\n")
F.close()