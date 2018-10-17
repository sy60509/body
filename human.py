class Human:
    def __init__(self, keypoints):
        #{0,  "Nose"},
        self.Nose = keypoints[0][0]
        #{1,  "Neck"},
        self.Neck = keypoints[0][1]
        #{2,  "RShoulder"},!!
        self.RS = keypoints[0][2]
        #{3,  "RElbow"},
        self.RE = keypoints[0][3]
        #{4,  "RWrist"},
        self.RW = keypoints[0][4]
        #{5,  "LShoulder"},!!
        self.LS = keypoints[0][5]
        #{6,  "LElbow"},
        self.LE = keypoints[0][6]
        #{7,  "LWrist"},
        self.LW = keypoints[0][7]
        #{8,  "MidHip"},
        self.MH = keypoints[0][8]
        #{9,  "RHip"},
        self.RH = keypoints[0][9]
        #{10, "RKnee"},
        self.RK = keypoints[0][10]
        #{11, "RAnkle"},!!
        self.RA = keypoints[0][11]
        #{12, "LHip"},
        self.LH = keypoints[0][12]
        #{13, "LKnee"},
        self.LK = keypoints[0][13]
        #{14, "LAnkle"},!!
        self.LA = keypoints[0][14]

        

    def test(self):
        return self.LS
    
    def getTArch(self):
        return {'RS':self.RS, 'LS':self.LS, 'Neck':self.Neck, 'MH':self.MH}
		
		
    def hwidth_fwidth(self):
	hwidth = abs(self.RW[0]-self.LW[0]);
	fwidth = abs(self.RA[0]-self.LA[0]);
	if hwidth > fwidth:
		return 1;
	else:
		return 0;
			
    def parallel(self):
		
			#陣列(肩膀)
	c1=self.RS;
	c2=self.LS;
		#存放兩個陣列的變數
	ans = list(map(lambda x: (x[0]-x[1]), zip(c2,c1)))
		#進行陣列內第0跟1位置的計算
	results= float(ans[1])/float(ans[0])
		#得出肩膀之斜率
	print(results)
		#印出肩膀結果

		#陣列(雙腳)
	d1=self.RA
	d2=self.LA
		#存放兩個陣列的變數
	ans2 = list(map(lambda x: (x[0]-x[1]), zip(d2,d1)))
		#進行陣列內第0跟1位置的計算
	results2= float(ans2[1])/float(ans2[0])
		#得出雙腳之斜率
	print(results2)
		#印出雙腳結果
	if abs(results-results2)<0.2:
		return 1
	else :
		return 0

    def shoulder_foot_distance(self):
        
        sxx=math.pow((self.RS[0]-self.LS[0]), 2)
        syy=math.pow((self.RS[1]-self.LS[1]), 2)
        s_dis=cmath.sqrt(sxx+syy)

        axx=math.pow((self.RA[0]-self.LA[0]), 2)
        ayy=math.pow((self.RA[1]-self.LA[1]), 2)
        a_dis=cmath.sqrt(axx+ayy)

        if a_dis>=s_dis:
            return 1
        else:
            return 0

