import pandas as pd
sku_file = pd.read_csv(r'D:\peter workspace\amazon_text.txt',sep='\t')
sku_list = sku_file["sku"]
incorrect_skus = sku_list.tolist() 
def preprocess_sku(sku):
	sku = sku.replace('BABA1','BABA')
	sku = sku.replace('ABSTRACT1','ABSTRACT')
	sku = sku.replace('N07_1','N07')
	sku = sku.replace('PLN-TRIP','PLN')

	return sku

def solving(con): 
	c = []
	a = con.split('-')	 
	b = a[-1]
	size=['XS','S','M','L','XL','XXL']
	if b in size:
		return con
	else:
		c.append(con)
	for i in c:
		return i 
	


def dirty_sku():
	clean_sku=[]
	sku_file1=sku_list.apply(preprocess_sku)
	sku_file['correct sku'] =pd.DataFrame(sku_file1.tolist() , columns=['new one'])
	correct_sku_list = sku_file['correct sku']
	con_list = correct_sku_list.apply(solving)
	parent_child = con_list.tolist()
	sku_file['Parent/child'] = parent_child
	Entering_datafile = sku_file.to_csv(r'D:\peter workspace\amazon sku_csv1.csv' , index=False)

	
dirty_sku()







