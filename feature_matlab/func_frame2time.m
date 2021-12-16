function frameTime=func_frame2time(frameNum,framelen,inc,fs)
% ================= 计算分帧后每一帧对应的时间=====================
% ================= 输     入 ===================================
%frameNum          :  总帧数
%framelen          ： 帧长
%inc               :  帧移
%fs                ： 采样频率
%================== 输     出 ====================================
%frametime         ： 每帧的时间，即取这一帧数据中间位置的时间
frameTime=(((1:frameNum)-1)*inc+framelen/2)/fs;