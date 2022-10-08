opts = delimitedTextImportOptions("Delimiter", ',');
data = readmatrix("1820000000_Hz.csv", opts);
num_samples = size(data);

center_freq = 940;

energies = zeros(num_samples(1), 1);

for i=1:num_samples(1)
    m = data(i, 2:end);
    m = str2double(m);
    top_m = m(1:1024);
    bottom_m = m(1025:2048);
    m = [bottom_m top_m];
    m = m(512:1536);
    m = db2mag(m);
    x = (center_freq - 15) + 0:30/2047:(center_freq + 15);
    x = x(512:1536);

    energies(i) = sum(m) / 1024;
end

plot(mag2db(energies));
