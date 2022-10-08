opts = delimitedTextImportOptions("Delimiter", ',');
data = readmatrix("1820000000_Hz.csv", opts);
num_samples = size(data);

for i=1:num_samples(1)
    m = data(i, 2:end);
    m = str2double(m);
    top_m = m(1:1024);
    bottom_m = m(1025:2048);
    m = [bottom_m top_m];
    
    plot(m); 
    pause;
end