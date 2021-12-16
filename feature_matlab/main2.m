% 自动读取文件夹中的音频，生成频域图、短时能量图、和语谱图，时频域图。并且保存
clear all;
close all;
clc;

[MU,fs]=audioread("test.wav");
y=MU;
N=length(y);
wlen=200; inc=80;
win=hanning(wlen);
X=func_enframe(y,win,inc)';   %分帧
fn=size(X,2);        %1是行 2是列
time=(0:N-1) / fs;
for i=1:fn
    u=X(:,i);
    u2=u.*u;
    En(i)=sum(u2);
end

figure(1);
%画出时域图
subplot 221; plot(time,y);
title('signal of audio');
ylabel('Amplitute');
%画出频域图
subplot 222;
[YfreqDomain,frequencyRange] = positiveFFT(y,fs);
stem(frequencyRange,abs(YfreqDomain)*2,'marker','none');
axis([0,8000,-inf,inf]);
title('频域');
%画出时频图曲线，平稳语音信号为20ms，所以取882点为窗
subplot 223;
window=hamming(882);
overlap=441;
nfft=2^nextpow2(length(window));
[s,f,t,p]=spectrogram(y,window,overlap,nfft,fs,'yaxis');
f1=sort(f,'descend');
surf(t,f1,10*log(p));
colorbar;%色标
[m n]=find(p==max(p));
plot(t,f(m));
xlabel('时间 t/s');
ylabel('频率 f/Hz');
title('时频图')
%画出短时能量
subplot 224;
plot(En);
title('短时能量');
%     saveas(gcf,['C:\Users\Zhoue\Desktop\12_9\pic\',int2str(j),'.fig']);
%画出三维时频图，x-时间 y-频率 z-功率谱
gcf=figure (2);
spectrogram(y,window,overlap,nfft,fs,'yaxis');
h=colorbar;
axis tight;
h.Label.String = 'Power/Frequency(dB/Hz)';
%     saveas(gcf,['C:\Users\Zhoue\Desktop\12_12\pic\',int2str(100+j),'.fig']);


