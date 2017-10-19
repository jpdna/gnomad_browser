import re
for line in open("oct10_chrALL.vep.txt.chr22.data"):
  line = line.rstrip()
  line_list = line.split("\t")
  alts = line_list[4].split(",")
  count_hets = []
  count_hom = []
  for a in alts:
    count_hets.append(0)
    count_hom.append(0)
  ac = re.match("AC=(.*?);", line_list[7])
  #print(ac.group(1))
  
  for geno in line_list[9:]: 
    gt = geno.split(":")[0]
    gt = gt.replace("|","/")
    gt_1 = gt.split("/")[0]
    gt_2 = gt.split("/")[1]
    #print gt_1 + " XXX " + gt_2 
    if( gt_1 == gt_2 and gt_1 != "." and gt_1 != "0"):
      #print "### gt_1: " + gt_1 + " gt_2: " + gt_2 + " This is a Hom"
      gt_alt_index = int(gt_1) - 1
      count_hom[gt_alt_index] = count_hom[gt_alt_index] + 1
    else:
      if(gt_1 != "." and int(gt_1) > 0 and gt_1 != gt_2):
        gt1_alt_index = int(gt_1) - 1
        count_hets[gt1_alt_index] = count_hets[gt1_alt_index] + 1
        #print "### gt_1 is a het " + gt_1 + "/" + gt_2 
      if (gt_2 != "." and int(gt_2) > 0 and gt_1 != gt_2):
        gt2_alt_index = int(gt_2) - 1
        count_hets[gt2_alt_index] = count_hets[gt2_alt_index] + 1
        #print "### gt_2 is a het " + gt_1 + "/" + gt_2

  
  hom_ALL_string = "Hom_ALL=" + ",".join(str(x) for x in count_hom)
  het_ALL_string = "Het_ALL=" + ",".join(str(x) for x in count_hets)
  ac_ALL_string = "AC_ALL=" + ac.group(1)

  new_info = line_list[7] + ";" + hom_ALL_string + ";" + het_ALL_string + ";" + ac_ALL_string
  
  #print "\t".join(line_list[0:6]) + "\t" + new_info + "\t" + "\t".join(line_list[9:])  
  print "\t".join(line_list[0:7]) + "\t" + new_info 
  #print line_list[0:6].join("\t") + "\t" + new_info

   
   
 
         
       
 

    
    
    
