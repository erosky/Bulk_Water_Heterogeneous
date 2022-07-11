#!/usr/bin/awk -f

# each data point becomes average of N points
# with statistical uncertainty calculated
# uncertainty = sqrt[(x_i - x_avg)^2 / N]





BEGIN { N = 50 ; sum = 0 ; time_0 = 0 ; temp_0 = 215 }
{
	if (NR % N == 0) { 
		sum = sum+$7 ; time = ($2+time_0)/2 ; temp = ($3+temp_0)/2 ; avg = sum/N ; print time "\t" temp "\t" avg ; sum = 0 ; time_0 = $2 ; temp_0 = $3 
	} else { sum = sum+$7 }
}
