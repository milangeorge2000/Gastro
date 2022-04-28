from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
from flask_cors import CORS
from flask_ngrok import run_with_ngrok



model = pickle.load(open('gastro.pkl','rb'))

app = Flask(__name__)

run_with_ngrok(app)




@app.route('/')
def home():
    return "hello"





@app.route('/predict',methods=['GET','POST'])
def predict():
    temp_array = list()
    request_data = request.get_json()

    d1 = request_data["S1"]
    arr = [0]*162
    if(d1 == "abdominal_pain__bloating"):
        arr[0] = 1
       
    elif(d1 == "abdominal_pain__burning_sensation"):
        arr[1] = 1
        
    elif(d1 == "abdominal_pain__cramps"):
        arr[2] = 1
   
    elif(d1 == "abdominal_pain__na"):
        arr[3] = 1
   
    elif(d1 == "abdominal_pain__sharp"):
        arr[4] = 1
      
    elif(d1 == "abdominal_tenderness__na"):
        arr[5] = 1
       
    elif(d1 == "abdominal_tenderness__severe"):
        arr[6] = 1
     
    elif(d1 == "abnormal_drowsiness__na"):
        arr[7] = 1
       
    elif(d1 == "bloating__na"):
        arr[8] = 1
       
    elif(d1 == "bloody_stools__na"):
        arr[9] = 1
       
    elif(d1 == "burping__na"):
        arr[10] = 1
        
    elif(d1 == "constipation__na"):
        arr[11] = 1
       
    elif(d1 == "cramps__low"):
        arr[12] = 1
       
    elif(d1 == "cramps__na"):
        arr[13] = 1
  
    elif(d1 == "cramps__severe"):
        arr[14] = 1
     
    elif(d1 == "cramps__sudden"):
        arr[15] = 1
    
    elif(d1 == "dark_urine__na"):
        arr[16] = 1
      
    elif(d1 == "dehydration__na"):
        arr[17] = 1
      
    elif(d1 == "diarrhea__bloody"):
        arr[18] = 1
      
    elif(d1 == "diarrhea__na"):
       arr[19] = 1
       
    elif(d1 == "diarrhea__persistent"):
        arr[20] = 1
       
    elif(d1 == "distention__na"):
        arr[21] = 1
        
    elif(d1 == "dry_stools__na"):
        arr[22] = 1
     
    elif(d1 == "fatigue__na"):
        arr[23] = 1
      
    elif(d1 == "feeling_full_after_meal__na"):
        arr[24] = 1
      
    elif(d1 == "fever__frequent"):
         arr[25] = 1
         
    elif(d1 == "fever__high"):
        arr[26] = 1
       
    elif(d1 == "fever_high__with_chills"):
        arr[27] = 1
    
    elif(d1 == "fever__low"):
        arr[28] = 1
        
    elif(d1 == "fever__na"):
        arr[29] = 1
      
    elif(d1 == "fever__with_chills"):
        arr[30] = 1
     
    elif(d1 == "gas__acute"):
        arr[31] = 1
 
    elif(d1 == "gas__na"):
        arr[32] = 1
      
    elif(d1 == "headache__mild"):
        arr[33] = 1
     
    elif(d1 == "headache__na"):
        arr[34] = 1
     
    elif(d1 == "headache__severe"):
        arr[35] = 1

    elif(d1 == "heartburn__na"):
        arr[36] = 1
        
    elif(d1 == "irregular_heartbeat__na"):
        arr[37] = 1
        
    elif(d1 == "loss_of_appetite__na"):
        arr[38] = 1
       
    elif(d1 == "loss_of_appetite__persistent"):
        arr[39] = 1
      
    elif(d1 == "loss_of_appetite__poor"):
        arr[40] = 1
        
    elif(d1 == "loss_of_appetite__sudden"):
        arr[41] = 1
        
    elif(d1 == "nausea__acute"):
        arr[42] = 1
        
    elif(d1 == "nausea__long_term"):
        arr[43] = 1
    
    elif(d1 == "nausea__na"):
        arr[44] = 1
       
    elif(d1 == "nausea__severe"):
        arr[45] = 1
        
    elif(d1 == "vomiting__acute"):
        arr[46] = 1
      
    elif(d1 == "vomiting__dry_heaves"):
        arr[47] = 1
       
    elif(d1 == "vomiting__na"):
        arr[48] = 1
       
    elif(d1 == "vomiting__recurring"):
        arr[49] = 1
        
    elif(d1 == "vomiting__severe_and_forceful"):
        arr[50] = 1
      
    elif(d1 == "weightloss__na"):
        arr[51] = 1
        
    elif(d1 == "weightloss__quickly"):
        arr[52] = 1
        
    elif(d1 == "weightloss__unintentional"):
        arr[53] = 1
       
    elif(d1 == "yellow_eyes_and_skin__na"):
        arr[54] = 1
      
    elif(d1 == "yellow_eyes_and_skin__sudden"):
        arr[55] = 1
       

    d2 = request_data["S2"]
    if(d2 == "abdominal_pain__cramps"):
        arr[56] = 1
       
    
    elif(d2 == "abdominal_pain__na"):
        arr[57]=1
       
    
    elif(d2 == "abdominal_pain__severe"):
        arr[58] = 1
 
    
    elif(d2 == "bloating__na"):
        arr[59] = 1
        
    
    elif(d2 == "bloody_stools__na"):
        arr[60] = 1
        
    
    elif(d2 == "burping__na"):
        arr[61] = 1
        
    
    elif(d2 == "cramps__severe"):
        arr[62] = 1
        
    
    elif(d2 == "dark_urine__na"):
        arr[63] = 1
       
    
    elif(d2 == "dehydration__na"):
        arr[64] = 1
       
    
    elif(d2 == "diarrhea__bloody"):
        arr[65] = 1
        
    
    elif(d2 == "diarrhea__na"):
        arr[66] = 1
        
    elif(d2 == "dry_stools__na"):
        arr[67] = 1
     
    
    elif(d2 == "feeling_full_after_meal__na"):
        arr[68] = 1
     
    
    elif(d2 == "fever__low"):
        arr[69] = 1
      
    
    elif(d2 == "fever__na"):
        arr[70] = 1
       
    
    elif(d2 == "gas__na"):
        arr[71] = 1
      
    
    elif(d2 == "heartburn_na"):
        arr[72] = 1
    
    
    elif(d2 == "loss_of_appetite__poor"):
        arr[73] = 1
     
    
    elif(d2 == "loss_of_appetite__sudden"):
        arr[74] = 1
       
    
    elif(d2 == "nausea__acute"):
        arr[75] = 1
        
    
    elif(d2 == "nausea__long_term"):
        arr[76] = 1
        
    
    elif(d2 == "nausea__na"):
        arr[77] = 1
      
    
    elif(d2 == "vomiting__acute"):
        arr[78] = 1
        
    
    elif(d2 == "vomiting__dry_heaves"):
        arr[79] = 1
   
    
    elif(d2 == "vomiting__na"):
        arr[80] = 1
        
    
    elif(d2 == "vomiting__recurring"):
        arr[81] = 1
        
    
    elif(d2 == "vomiting__severe_and_forceful"):
        arr[82] = 1
      
    
 
    d3 = request_data["S3"]

    if(d3 == "abdominal_pain__bloating"):
        arr[83] = 1
       
    
    elif(d3 == "abdominal_pain__cramps"):
        arr[84] = 1
        
    
    elif(d3 == "abdominal_pain__na"):
        arr[85] = 1
       
    
    elif(d3 == "abdominal_pain__sharp"):
        arr[86] = 1
        
    
    elif(d3 == "abnormal_drowsiness__na"):
        arr[87] = 1
       
    
    elif(d3 == "bloating__na"):
        arr[88] = 1
       
    
    elif(d3 == "bloody_stools__na"):
        arr[89] = 1
        
    
    elif(d3 == "burping__na"):
        arr[90] = 1
       
    
    elif(d3 == "cramps_low"):
        arr[91] = 1
      

    elif(d3 == "cramps_severe"):
        arr[92] = 1
        
    
    elif(d3 == "dark_urine__na"):
        arr[93] = 1
       
    
    elif(d3 == "diarrhea__high"):
        arr[94] = 1
       
    
    elif(d3 == "diarrhea__na"):
        arr[95] = 1
        
    
    elif(d3 == "fatigue__na"):
        arr[96] = 1
       
    
    elif(d3 == "feeling_full_after_meal__na"):
        arr[97] = 1
       
    
    elif(d3 == "fever__high"):
        arr[98] = 1
        
    
    elif(d3 == "fever__na"):
        arr[99] = 1
       
    
    elif(d3 == "gas__na"):
        arr[100] = 1
       
    
    elif(d3 == "headache__mild"):
        arr[101] = 1
      
    
    elif(d3 == "loss_of_appetite__persistent"):
        arr[102] = 1
        
    
    elif(d3 == "loss_of_appetite__poor"):
        arr[103] = 1
     
    
    elif(d3 == "nausea__acute"):
        arr[104] = 1
      
    
    elif(d3 == "nausea__na"):
        arr[105] = 1
      
    

    elif(d3 == "vomiting__na"):
        arr[106] = 1
       
    
    elif(d3 == "weightloss__na"):
        arr[107] = 1
      
    
    elif(d3 == "weightloss__quickly"):
        arr[108] = 1
     
    

    elif(d3 == "weightloss__unintentional"):
        arr[109] = 1
       
    elif(d3 == "yellow_eyes_and_skin_tinted"):
        arr[110] = 1
   
    
   
    

    d4 = request_data["S4"]

    if(d4 == "abdominal_pain__cramps"):
        arr[111] = 1
       
    
    elif(d4 == "abdominal_pain__na"):
        arr[112] = 1
     
    
    elif(d4 == "abdominal_tenderness__na"):
        arr[113] = 1
       
    
    elif(d4 == "abdominal_tenderness__severe"):
        arr[114] = 1
      
    
    elif(d4 == "bloating__na"):
        arr[115] = 1
      
    
    elif(d4 == "burping__na"):
        arr[116] = 1
       
    
    elif(d4 == "cramps__low"):
        arr[117] = 1
      
    
    elif(d4 == "cramps__sudden"):
        arr[118] = 1
        
    
    elif(d4 == "dark_urine__na"):
        arr[119] = 1
    
    
    elif(d4 == "diarrhea__bloody"):
        arr[120] = 1
    
    
    elif(d4 == "diarrhea__na"):
        arr[121] = 1
    
    
    elif(d4 == "dry_stools__na"):
        arr[122] = 1
        
    elif(d4 == "feeling_full_after_meal__na"):
        arr[123] = 1
       
    
    elif(d4 == "fever__na"):
        arr[124] = 1
      
    
    elif(d4 == "gas__na"):
        arr[125] = 1
     
    
    elif(d4 == "heartburn__na"):
        arr[126] = 1
      
    
    elif(d4 == "irregular__heartbeat_na"):
        arr[127] = 1
       
    
    elif(d4 == "loss_of_appetite__poor"):
        arr[128] = 1
       
    

    elif(d4 == "loss_of_appetite__sudden"):
        arr[129] = 1
     
    
    elif(d4 == "nausea__acute"):
        arr[130] = 1
      
    
    elif(d4 == "nausea__na"):
        arr[131] = 1
   
    
    elif(d4 == "vomiting__recurring"):
        arr[132] = 1
       
    

    elif(d4 == "weightloss__na"):
        arr[133] = 1
      
    
    elif(d4 == "yellow_eyes_and_skin__na"):
        arr[134] = 1
    
    
   
    
    d5 = request_data["S5"]


    if(d5 == "abdominal drowsiness_na"):
        arr[135] = 1
   
    
    elif(d5 == "abdominal_pain__bloating"):
        arr[136] = 1

    
    elif(d5 == "abdominal_tenderness__na"):
        arr[137] = 1
       
    
    elif(d5 == "abdominal_tenderness__severe"):
        arr[138] = 1
        
    
    elif(d5 == "bloating__na"):
        arr[139] = 1
       
    

    elif(d5 == "bloody_stools__na"):
        arr[140] = 1
        
    

    elif(d5 == "burping__na"):
        arr[141] = 1
       
    
    
    elif(d5 == "constipation__na"):
        arr[142] = 1
        
    

    elif(d5 == "cramps__na"):
        arr[143] = 1
  
    
    elif(d5 == "dehydration__na"):
        arr[144] = 1
       
    

    elif(d5 == "diarrhea__na"):
        arr[145] = 1
      

    
    elif(d5 == "diarrhea__persistent"):
        arr[146] = 1
       
    

    elif(d5 == "distention__na"):
        arr[147] = 1

    
    elif(d5 == "fatigue__na"):
        arr[148] = 1
     
    
    elif(d5 == "fever__low"):
        arr[149] = 1
      
    

    elif(d5 == "gas__acute"):
        arr[150] = 1
       
    

    elif(d5 == "headache__severe"):
        arr[151] = 1
     
    

    elif(d5 == "heartburn__na"):
        arr[152] = 1
      
    

    elif(d5 == "loss_of_appetite__sudden"):
        arr[153] = 1
       
    
    elif(d5 == "muscle_ache__na"):
        arr[154] = 1
        
    

    elif(d5 == "nausea__acute"):
        arr[155] = 1
        
    


    elif(d5 == "nausea__long_term"):
        arr[156] = 1
     
    

    elif(d5 == "nausea__na"):
        arr[157] = 1
       
    
    elif(d5 == "nausea__severe"):
        arr[158] = 1

    

    elif(d5 == "vomiting__na"):
        arr[159] = 1
      
    
    elif(d5 == "vomiting__severe_and_forceful"):
        arr[160] = 1
      
    

    elif(d5 == "weightloss__na"):
        arr[161] = 1
    
    
    temp_array = temp_array + arr
    

 
    
    prediction = model.predict([temp_array])
    print(prediction)
    return jsonify(prediction[0])
    


    


    

if __name__ == "__main__":
  app.run()

    
    



    
    
    
    

    

    
