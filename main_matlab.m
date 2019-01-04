function result = main_matlab(name)
    cd ../matlab;
%    try
        if strcmp(name, 'laura')
            cd ../matlab/laura;
            temp = mainglcm(2);
        elseif strcmp(name, 'vita')
            cd ../matlab/vita;
            temp = mainSURF(2);
        elseif strcmp(name, 'fika')
            cd ../matlab/fika;
            temp = mainglcm(2);
        elseif strcmp(name, 'farisa')
            cd ../matlab/farisa;
            temp = mainDWT(3);
        end
        cd ../../server;
        result = temp;
%    catch
%        cd ../../server;
%        result = 'ERROR';
%    end
end

