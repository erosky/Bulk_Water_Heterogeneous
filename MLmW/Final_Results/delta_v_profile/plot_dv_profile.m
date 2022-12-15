% Define a starting folder.
iceDir = genpath('1_atm/ice');

% Get list of all subfolders.
allSubFolders = genpath('1_atm/ice/');
% Parse into a cell array.
remain = allSubFolders;
% Initialize variable that will contain the list of filenames so that we can concatenate to it.
listOfFolderNames = {};
while true
	[singleSubFolder, remain] = strtok(remain, ':');
	if isempty(singleSubFolder)
		break;
	end
	listOfFolderNames = [listOfFolderNames singleSubFolder];
end
numberOfFolders = length(listOfFolderNames);

% Process all image files in those folders.
for k = 1 : numberOfFolders
	% Get this folder and print it out.
	thisFolder = listOfFolderNames{k};
	fprintf('Processing folder %s\n', thisFolder);
	
	% Get ALL files.
	filePattern = sprintf('%s/*.dat', thisFolder);
	baseFileNames = dir(filePattern);
	numberOfFiles = length(baseFileNames);
    
    ice_matrix = []
	if numberOfFiles >= 1
		% Go through all those files.
		for f = 1 : numberOfFiles
			fullFileName = fullfile(thisFolder, baseFileNames(f).name);
			fprintf('     Processing file %s\n', fullFileName);
            matrix = transpose(readmatrix(fullFileName,'Whitespace',' []'));
            ice_matrix = [ice_matrix; matrix(3,:)];
		end
	else
		fprintf('     Folder %s has no files in it.\n', thisFolder);
    end
end





% Define a starting folder.
liqDir = genpath('1_atm/liquid');

% Get list of all subfolders.
allSubFolders = genpath('1_atm/liquid/');
% Parse into a cell array.
remain = allSubFolders;
% Initialize variable that will contain the list of filenames so that we can concatenate to it.
listOfFolderNames = {};
while true
	[singleSubFolder, remain] = strtok(remain, ':');
	if isempty(singleSubFolder)
		break;
	end
	listOfFolderNames = [listOfFolderNames singleSubFolder];
end
numberOfFolders = length(listOfFolderNames);

% Process all image files in those folders.
for k = 1 : numberOfFolders
	% Get this folder and print it out.
	thisFolder = listOfFolderNames{k};
	%fprintf('Processing folder %s\n', thisFolder);
	
	% Get ALL files.
	filePattern = sprintf('%s/*.dat', thisFolder);
	baseFileNames = dir(filePattern);
	numberOfFiles = length(baseFileNames);
    
    liq_matrix = []
	if numberOfFiles >= 1
		% Go through all those files.
		for f = 1 : numberOfFiles
			fullFileName = fullfile(thisFolder, baseFileNames(f).name);
			%fprintf('     Processing file %s\n', fullFileName);
            matrix = transpose(readmatrix(fullFileName,'Whitespace',' []'));
            liq_matrix = [liq_matrix; matrix(3,:)];
		end
	else
		fprintf('     Folder %s has no files in it.\n', thisFolder);
    end
end


z_axis = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
ice_profile = mean(ice_matrix,1)
ice_std = std(ice_matrix,0,1);
liq_profile = mean(liq_matrix,1)
liq_std = std(liq_matrix,0,1);

del_profile = ice_profile - liq_profile

plot(z_axis, liq_profile, z_axis, ice_profile)
%plot(z_axis, del_profile)


    

edge_ice = mean(ice_profile(10:13))
center_ice = mean(ice_profile(16:23))
edge_liq = mean(liq_profile(10:13))
center_liq = mean(liq_profile(16:23))



e_ice_v = density_to_volume(edge_ice);
c_ice_v = density_to_volume(center_ice);
e_liq_v = density_to_volume(edge_liq);
c_liq_v = density_to_volume(center_liq);

dv_edge = e_ice_v - e_liq_v
dv_center = c_ice_v - c_liq_v






function vol = density_to_volume(dens)
    A3_to_cm3 = 1e+24;
    N_to_mol = 1.6605391e-24; 
    units = dens*A3_to_cm3*N_to_mol;
    vol = 1/units;
end