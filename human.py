class Human:
    def __init__(self, keypoints):
        
        #{0,  "Nose"},
        self.Nose = keypoints[0][0]
        #{1,  "Neck"},
        self.Neck = keypoints[0][1]
        #{2,  "RShoulder"},
        self.RS = keypoints[0][2]
        #{3,  "RElbow"},
        self.RE = keypoints[0][3]
        #{4,  "RWrist"},
        self.RW = keypoints[0][4]
        #{5,  "LShoulder"},
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
        #{11, "RAnkle"},
        self.RA = keypoints[0][11]
        #{12, "LHip"},
        self.LH = keypoints[0][12]
        #{13, "LKnee"},
        self.LK = keypoints[0][13]
        #{14, "LAnkle"},
        self.LA = keypoints[0][14]

    def test(self):
        return self.LS;

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

