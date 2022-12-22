f = open("input.txt",'r')
Dic = {}

def eval_Dic(root):
  if(not isinstance(root['count'], int)):
    root['count'] = int(eval(str(eval_Dic(Dic[root['val1']]))+' '+ root['operation'] +' '+str(eval_Dic(Dic[root['val2']]))))
  return root['count']
for i in f:
  temp = {"count":'',"val1":'',"val2":'',"operation":'',}
  lis = i.split()
  if(lis[1].isdigit()):
    temp["count"] = int(lis[1])
  else:
    temp["val1"] = lis[1]
    temp["val2"] = lis[3]
    temp["operation"] = lis[2]
  Dic[lis[0][:-1]] = temp
print(eval_Dic(Dic['root']))
