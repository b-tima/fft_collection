opts = delimitedTextImportOptions("Delimiter", ',');
data = readmatrix("2630000000_Hz.csv", opts);
m = data(1, 2:end);
m = str2double(m);
top_m = m(1:1024);
bottom_m = m(1025:2048);
m = [bottom_m top_m];

plot(m);