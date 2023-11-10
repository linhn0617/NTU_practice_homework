import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

data_a = pd.read_csv('a_lvr_land_a.csv')
data_b = pd.read_csv('b_lvr_land_a.csv')
data_e = pd.read_csv('e_lvr_land_a.csv')
data_f = pd.read_csv('f_lvr_land_a.csv')
#將第一行的英文翻譯刪除
data_a = data_a.iloc[1:]
data_b = data_b.iloc[1:]
data_e = data_e.iloc[1:]
data_f = data_f.iloc[1:]
#新增城市名的欄位
data_a["city"] = "Taipei"
data_b["city"] = "Taichung"
data_e['city'] = 'Kaohsiung'
data_f['city'] = 'New Taipei'
#合併四個城市的資料表 axis=0 為直向合併
all_data = pd.concat([data_a,data_b,data_e,data_f],axis=0) 
all_data = all_data.drop(columns = "移轉編號")
#將欄位名稱轉換成英文，方便之後的資料分析
columns_mapping = {'鄉鎮市區':'towns',
'交易標的':'transaction_sign',
'土地位置建物門牌':'house_number',
'土地移轉總面積平方公尺':'land_area_square_meter', 
'都市土地使用分區':'use_zoning', 
'非都市土地使用分區':'land_use_district',
'非都市土地使用編定':'land_use',
'交易年月日':'tx_dt', 
 '交易筆棟數':'transaction_pen_number', 
 '移轉層次':'shifting_level', 
 '總樓層數':'total_floor_number', 
 '建物型態':'building_state', 
 '主要用途':'main_use', 
 '主要建材':'main_materials',
 '建築完成年月':'complete_date', 
 '建物移轉總面積平方公尺':'building_area_square_meter', 
 '建物現況格局-房':'room_number', 
 '建物現況格局-廳':'hall_number', 
 '建物現況格局-衛':'health_number', 
'建物現況格局-隔間':'compartmented_number', 
 '有無管理組織':'manages', 
 '總價元':'total_price', 
 '單價元平方公尺':'unit_price', 
 '車位類別':'berth_category', 
 '車位移轉總面積平方公尺':'berth_area_square_meter',
'車位總價元':'berth_price', 
 '備註':'note', 
 '編號':'serial_number', 
 '主建物面積':'main_building_area', 
 '附屬建物面積':'auxiliary_building_area', 
 '陽台面積':'balcony_area', 
 '電梯':'elevator'}

analysis_columns = ['city','towns','main_use','use_zoning','total_price','building_area_square_meter',
                    'main_building_area','tx_dt','unit_price','room_number','hall_number','health_number']
columns_type = {'total_price': 'int','unit_price':'float','building_area_square_meter':'float',
                'main_building_area': 'float','room_number': 'int','hall_number': 'int','health_number': 'int'}

analysis_data  = all_data.rename(columns = columns_mapping)
#取出主要用途為“住家用”且都市土地使用分區為“住”的資料並刪除nan值
analysis_data = analysis_data.loc[(analysis_data.main_use=='住家用')&(analysis_data.use_zoning=='住'),analysis_columns].dropna()
analysis_data.head(5)
#將欄位進行數據類型轉換
analysis_data = analysis_data.astype(columns_type)
#將交易年月日欄位值的後四個數字刪除，並建立交易年欄位
analysis_data["tx_dt_year"] = analysis_data["tx_dt"].apply(lambda x: int(x[:-4])) 
#1.交易年月日(tx_dt_year)，限制在112年
#2.建物現況格局-房(room_number)，限制在2間
#3.建物現況格局-廳(hall_number)，限制在1到2廳
#4.建物現況格局-衛浴（health_number），限制在2間
#5.最後運用.reset_index()重新定義索引
analysis_data = analysis_data.loc[(analysis_data['tx_dt_year'] == 112)&
                                  (analysis_data['room_number'] == 2)&
                                  (analysis_data['health_number'] == 2)&
                                  (analysis_data['hall_number'] >= 1)&
                                  (analysis_data['hall_number'] <= 2) ]
analysis_data = analysis_data.reset_index(drop=True)
analysis_data.head(5)
#將平方公尺換算成坪
analysis_data["building_area_square_feet"] = analysis_data.building_area_square_meter*0.3025
analysis_data["main_building_area_square_feet"] = analysis_data.main_building_area*0.3025
analysis_data["unit_price_square_feet"] = analysis_data.unit_price/0.3025

#找出影響新北市總價、單價元坪的因子
New_Taipei_data = analysis_data.loc[analysis_data.city =='New Taipei']
corr_data = New_Taipei_data[["total_price","building_area_square_meter","main_building_area","unit_price",
                             "room_number","hall_number","health_number","tx_dt_year","building_area_square_feet",
                            "main_building_area_square_feet","unit_price_square_feet"]]
correlation = corr_data.corr()[['total_price','unit_price_square_feet']]
print(correlation)
#以城市(city)為x軸，以單價元坪(unit_price_square_feet)為y軸畫出boxplot，並找出單價元坪(unit_price_square_feet)中位數最高的城市，結論是台北市
analysis_data.boxplot(column=['unit_price_square_feet'],by='city',figsize=(12,10))
#對新北市的資料做圖，先將地區(twons)做編碼再進行，再以地區(twon)為x軸，以單價元坪(unit_price_square_feet)為y軸畫出boxplot。
le = LabelEncoder()
New_Taipei_data.loc[:, 'town_label_encoding'] = le.fit_transform(New_Taipei_data['towns'])
fig = plt.figure(figsize = (18,8))
sns.boxplot(data = New_Taipei_data, x = 'town_label_encoding', y = 'unit_price_square_feet')

encoded_values = [1,2,4,5,6,8,10,11]
# 使用le.inverse反向查詢區域的名稱
# 可以看出『板橋區』的每坪單價最高
le.inverse_transform(encoded_values)