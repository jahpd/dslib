from optparse import OptionParser
import math

parser = OptionParser()
parser.add_option("-r", "--reflections", help="number of reflections", type="int", dest="refl")
parser.add_option("-m", "--milisseconds", help="millisecconds reflections", type="float", dest="ms")
parser.add_option("-d", "--decay", help="decay reflections (0..100)", type="float", dest="decay")

(options, args) = parser.parse_args()

# Abre um arquivo com os delays
external = open("_delay~.pd", "w")

# Cria objetos iniciais
external.write("#N canvas 375 123 450 300 10;")
external.write("#X obj 0 0 inlet~;")
external.write("#X obj 0 200 outlet~;")
obj = 2
for n in range(0, options.refl):
  # cria delays
  delwrite = "#X obj %d %d delwrite~ \$0-delay_%d %d;" % (n*160, 35, n, options.ms*(options.refl-n))
  delread = "#X obj %d %d delread~ \$0-delay_%d %d;" % (n*160, 100, n, options.ms*(options.refl-n))
  if n == 0:
    r = "#X obj %d %d *~ %f;" % (80, 70, options.decay/100.0)
  else:
    r = "#X obj %d %d *~ %f;" % (80+(n*140), 70, options.decay/100.0)
  external.write(delwrite)
  external.write(delread)
  external.write(r)
  obj += 3
  

c = "#X connect 0 0 2 0;\n"
external.write(c)

#cc = "#X connect %d 0 1 0;" % (options.refl-1)
#external.write(cc)

#X connect 0 0 2 0;
#X connect 3 0 4 0;
#X connect 4 0 5 0;
#X connect 6 0 7 0;
#X connect 7 0 1 0;
offset = 0
for n in range(0, obj-1):
  c = "#X connect %d 0 %d 0;" % (n+2, n+3)
  print "connecting %d ->  %d" % (n+2, n+3)
  external.write(c)
  offset += 1
  #external.write(ccc)


c = "#X connect %d 0 1 0;\n" % (obj-1)
cc = "#X connect %d 0 2 0;\n" % (obj-1)
external.write(c)
external.write(cc)
external.close()
