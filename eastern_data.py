from browser import document, window
Plotly = window.Plotly

def unpack(rows,key):
	res = []
	for row in rows:
		res.append(row[key])
	return res

def csv_load_callback(err, rows):
	dates = unpack(rows, 'date')
	
	tc = unpack(rows, 'total_cases')
	
	tc_data = [
			{
	        "x": dates,
	        "y": tc,
	        "mode": 'markers',
	        "type": 'scatter'
	    }];
	
	Plotly.newPlot('tc', tc_data);

Plotly.d3.csv("https://raw.githubusercontent.com/Jack2104/covid-data/main/eastern_hemisphere_data_copy.csv", csv_load_callback)