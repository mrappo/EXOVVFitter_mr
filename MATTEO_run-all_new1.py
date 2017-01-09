import os,commands
import sys
from optparse import OptionParser
import ConfigParser 
from datetime import datetime





def timenow(form=0):
    if form:
       timenow=datetime.strftime(datetime.now(), '%d-%m-%Y_%H:%M:%S')   
    else:
       timenow=datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')
    return timenow
    
    
    




def writeConfiguration(mass,channel,sample,category, process_mode,jetalgo,interpolate,luminosity,ntuple_dir,ntuple_used,mean_shift,sigma_scale_factor,reweight_for_T,reweight_for_V):
    m=str(mass)
    filename="Data_configuration_"+m+"_"+sample+"_"+timenow(1)
    f = open(filename, 'w')
    f.write("Parametri utilizzati per la valutazione del Background\n\n")
    f.write(timenow(0))
    f.write("\nchannel:\t%s\t\t\t tipo di dato: %s" % (channel,type(channel)))
    f.write("\nsample :\t%s\t\t\t tipo di dato: %s" % (sample,type(sample)))
    f.write("\ncategory :\t%s\t\t\t tipo di dato: %s" % (category,type(category)))
    f.write("\nprocess_mode :\t%s\t\t\t tipo di dato: %s" % (process_mode, type(process_mode)))
    f.write("\njetalgo :\t%s\t\t\t tipo di dato: %s" % (jetalgo, type(jetalgo)))
    f.write("\ninterpolate :\t%s\t\t\t tipo di dato: %s" % (interpolate, type(interpolate)))
    f.write("\nluminosity :\t%s\t\t\t tipo di dato: %s" % (luminosity, type(luminosity)))
    f.write("\nntuple_dir :\t%s\t\t\t tipo di dato: %s" % (ntuple_dir, type(ntuple_dir)))
    f.write("\nntuple_used :\t%s\t\t\t tipo di dato: %s" % (ntuple_used,type(ntuple_used)))
    f.write("\nmean_shift :\t%s\t\t\t tipo di dato: %s" % (mean_shift, type(mean_shift)))
    f.write("\nsigma_scale_factor :\t%s\t\t\t tipo di dato: %s" % (sigma_scale_factor, type(sigma_scale_factor)))
    f.write("\nreweight_for_T :\t%s\t\t\t tipo di dato: %s" % (reweight_for_T, type(reweight_for_T)))
    f.write("\nreweight_for_V :\t%s\t\t\t tipo di dato: %s" % (reweight_for_V, type (reweight_for_V)))
    f.closed







parser = OptionParser()

#parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="mu")
#parser.add_option('-s', action="store",type="string",dest="sample",default="BulkGraviton")
#parser.add_option('--category', action="store",type="string",dest="category",default="HP")
#parser.add_option('--type', action="store",type="string",dest="type",default="")
#parser.add_option('--jetalgo', action="store",type="string",dest="jetalgo",default="jet_mass_pr")
#parser.add_option('--interpolate', action="store_true",dest="interpolate",default=False)
parser.add_option('--batchMode', action="store_true",dest="batchMode",default=False)
#parser.add_option('--luminosity',action="store",type="float",dest="luminosity",default="2300.")
(options, args) = parser.parse_args()

currentDir = os.getcwd();









config = ConfigParser.ConfigParser()
config.read("infile.cfg")
channel = config.get("SectionOne","channel")
sample = config.get("SectionOne","sample")
category = config.get("SectionOne","category")
process_mode = config.get("SectionOne","process_mode")
jetalgo = config.get("SectionOne","jetalgo")
interpolate = config.getboolean("SectionOne","interpolate")
batchMode = config.getboolean("SectionOne","batchMode")
luminosity = config.getfloat("SectionOne","Luminosity")
ntuple_dir = config.get("SectionOne","Ntuple_dir")
ntuple_used = config.get("SectionOne","Ntuple_used")
mean_shift= config.getfloat("SectionOne","Mean_Shift")
sigma_scale_factor = config.getfloat("SectionOne","Sigma_Scale_Factor")
reweight_for_T = config.getfloat("SectionOne","Reweight_for_T")
reweight_for_V = config.getfloat("SectionOne","Reweight_for_T")
print timenow(0)
print "\nchannel:\t%s\t\t\t tipo di dato: %s" % (channel,type(channel))
print "\nsample :\t%s\t\t\t tipo di dato: %s" % (sample,type(sample))
print "\ncategory :\t%s\t\t\t tipo di dato: %s" % (category,type(category))
print "\nprocess_mode :\t%s\t\t\t tipo di dato: %s" % (process_mode, type(process_mode))
print "\njetalgo :\t%s\t\t\t tipo di dato: %s" % (jetalgo, type(jetalgo))
print "\ninterpolate :\t%s\t\t\t tipo di dato: %s" % (interpolate, type(interpolate))
print "\nbatchMode :\t%s\t\t\t tipo di dato: %s" % (batchMode, type(batchMode))
print "\nluminosity :\t%s\t\t\t tipo di dato: %s" % (luminosity, type(luminosity))
print "\nntuple_dir :\t%s\t\t\t tipo di dato: %s" % (ntuple_dir, type(ntuple_dir))
print "\nntuple_used :\t%s\t\t\t tipo di dato: %s" % (ntuple_used,type(ntuple_used))
print "\nmean_shift :\t%s\t\t\t tipo di dato: %s" % (mean_shift, type(mean_shift))
print "\nsigma_scale_factor :\t%s\t\t\t tipo di dato: %s" % (sigma_scale_factor, type(sigma_scale_factor))
print "\nreweight_for_T :\t%s\t\t\t tipo di dato: %s" % (reweight_for_T, type(reweight_for_T))
print "\nreweight_for_V :\t%s\t\t\t tipo di dato: %s" % (reweight_for_V, type (reweight_for_V))




#lumi_float_value=options.luminosity_value;
lumi_str_value= str("%.0f"%luminosity);

masses = [1200]
#masses = [600,700,750,800,900,1000,1200,1400]
#masses = [650,700,750,800,900,1000,1200,1400,2000,3000,4000]
#masses = [800,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500]
#masses = [800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
#          3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,4100,4200,4300,4400,4500] #use this one only for the interpolation mode!

#masses = [3000,3500,4000,4500]
for m in masses:
   
   writeConfiguration(m,channel,sample,category, process_mode,jetalgo,interpolate,luminosity,ntuple_dir,ntuple_used,mean_shift,sigma_scale_factor,reweight_for_T,reweight_for_V)
   
   if (interpolate==False and options.batchMode==True):

      fn = "Job/Job_%s_%s_%d"%(channel,category,m)
      outScript = open(fn+".sh","w");
 
      outScript.write('#!/bin/bash');
      outScript.write("\n"+'cd '+currentDir);
      outScript.write("\n"+'eval `scram runtime -sh`');
      outScript.write("\n"+'export PATH=${PATH}:'+currentDir);
      outScript.write("\n"+'echo ${PATH}');
      outScript.write("\n"+'ls');
#      cmd = "python g1_exo_doFit_class.py -b -c %s --mass %i --category %s --sample %s_lvjj --jetalgo %s --interpolate True > log/%s_M%i_%s_%s.log" %(options.channel,m,options.category,options.sample,options.jetalgo,options.sample,m,options.channel,options.category)
      cmd = "python MATTEO_g1_nw1.py -b -c %s --mass %i --category %s --sample %s --jetalgo %s --luminosity %f --ndir %s --nus %s --rfv %f --rft %f --ssf %f --ms %f --prom %s> log/%s_M%i_%s_%s_lumi_%s.log" %(channel,m,category,sample,jetalgo,luminosity,ntuple_dir,ntuple_used,reweight_for_V,reweight_for_T,sigma_scale_factor,mean_shift,process_mode,sample,m,channel,category,lumi_str_value)

      outScript.write("\n"+cmd);
#      outScript.write("\n"+'rm *.out');
      outScript.close();

      os.system("chmod 777 "+currentDir+"/"+fn+".sh");
      os.system("bsub -q cmscaf1nd -cwd "+currentDir+" "+currentDir+"/"+fn+".sh");

   elif (interpolate==True and not options.batchMode==True):
      cmd = "python MATTEO_g1_nw1.py -b -c %s --interpolate True --mass %i --category %s --sample %s --jetalgo %s --luminosity %f --ndir %s --nus %s --rfv %f --rft %f --ssf %f --ms %f --prom %s> log/%s_M%i_%s_%s_lumi_%s.log" %(channel,m,category,sample,jetalgo,luminosity,ntuple_dir,ntuple_used,reweight_for_V,reweight_for_T,sigma_scale_factor,mean_shift,process_mode,sample,m,channel,category,lumi_str_value)
      print cmd
      os.system(cmd)

   else:   
      cmd = "python MATTEO_g1_nw1.py -b -c %s --mass %i --category %s --sample %s --jetalgo %s --luminosity %f --ndir %s --nus %s --rfv %f --rft %f --ssf %f --ms %f --prom %s> log/%s_M%i_%s_%s_lumi_%s.log" %(channel,m,category,sample,jetalgo,luminosity,ntuple_dir,ntuple_used,reweight_for_V,reweight_for_T,sigma_scale_factor,mean_shift,process_mode,sample,m,channel,category,lumi_str_value)
      print cmd
      os.system(cmd)

#python run-all.py --channel mu -s Wprime_WZ --jetalgo Mjsoftdrop --category HP
#python run-all.py -c mu -s BulkG_WW --category HPW
