import json
from os import path

is_train = False

if is_train:
	# Parameters to determin where and what is stored
	input_file = 'SpillageData/train/via_region_data.json'
	image_output_file = 'data/my_data/train.txt'
	image_store = '/home/nmashkoor/spill-detect/SpillageData/train/'
else:
	input_file = 'SpillageData/val/via_region_data.json'
	image_output_file = 'data/my_data/val.txt'
	image_store = '/home/nmashkoor/spill-detect/SpillageData/val/'	

class_output_file = 'data/my_data/data.names' # names
class_file_json = 'class_labels.json'
id_output_dump = 'data/my_data/file_name.json'
class_labels = {}
id_to_name = {}
image_width = 640 
image_height = 480 
class_counter = 0
id_counter = 0

# Loading class labels
if path.exists(class_file_json):
	with open(class_file_json) as json_file:
		class_labels  = json.load(json_file)

# Loading files json
with open(input_file) as f:
	data_content = json.load(f)

# Wrting Converted file
with open(image_output_file, 'w') as o:
	for  data_val in data_content.values():
		current_file = data_val['filename']
		current_file = current_file.replace(' ', '_')
		id_to_name[id_counter] = current_file
		possible_regions = []
		region_id = 0
		for region in data_val['regions']:
			current_x_points = region['shape_attributes']['all_points_x']
			current_y_points = region['shape_attributes']['all_points_y']
			min_X = min(current_x_points)
			max_X = max(current_x_points)
			min_Y = min(current_y_points)
			max_Y = max(current_y_points)
			current_class = region['region_attributes']['type']
			
			if current_class not in class_labels:
				class_labels[current_class] = class_counter
				class_counter+=1
			current_class_counter = class_labels[current_class]

			possible_regions.append(str(current_class_counter) + ' ' + str(min_X) + ' ' + str(min_Y) + ' ' + str(max_X) +' '+str(max_Y) )
		
		image_regions = ' '.join(possible_regions)

		if len(possible_regions) != 0:
			o.write(str(id_counter) + ' ' + image_store + current_file + ' ' + str(image_width) + ' ' + str(image_height) + ' ' \
				+ image_regions)
			o.write('\n')
			id_counter+=1
	print('{} images processed'.format(id_counter))

# Printing Class labels Txt
with open(class_output_file, 'w') as o:
	for c in class_labels:
		o.write(c)
		o.write('\n')
print('Following classes found: {}'.format(class_labels))

if is_train:
	# Printing Class labels Json
	with open(class_file_json, 'w') as json_file:
		json.dump(class_labels, json_file)


	# Dumping image encoding
	with open(id_output_dump, 'w') as json_file:
		json.dump(id_to_name, json_file)


