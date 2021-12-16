close all
clear all
clc
%画出语音信号的时域图
[MU,fs]=audioread('test.wav'); %读取音频
sound(MU,fs);          %音频发声
n=length(MU);
figure(1);
subplot(2,1,1);
time=[1:n]/44100;
plot(time,MU);
title("原始信号");
%画出语音信号对应的频域图
subplot(2,1,2);
y=MU;
En1=sum(abs(y).^2);    %E=sum(x.*conj(x));或 E=sum(abs(x).^2)能量
[YfreqDomain,frequencyRange] = positiveFFT(y,fs);
stem(frequencyRange,abs(YfreqDomain)*2,'marker','none');
xlabel('Freq (Hz)');
ylabel('Amplitude');
title('Using the positiveFFT function');
axis([0 5000 -inf inf]);

%画出原始语音信号经过滤波器之后的时域信号
%该滤波为一个带通滤波，留下1100-5900的频域信号，函数见bandpass_filter
figure (2);
subplot 211;
Hd=bandpass_filter;
output=filter(Hd,MU);
En2=sum(abs(output).^2);   %滤波之后的能量
plot(time,output);
title('滤波之后的信号');
[YfreqDomain,frequencyRange] = positiveFFT(output,fs);
axis([-inf inf -0.2 0.3]);
%stem(frequencyRange,abs(YfreqDomain));
%画出经过滤波之后的语音信号的频域
subplot 212;
stem(frequencyRange,abs(YfreqDomain)*2,'marker','none');
xlabel('Freq (Hz)');
ylabel('Amplitude');
title('Using the positiveFFT function');
axis([0 5000 -inf inf]);

rate=En2/En1