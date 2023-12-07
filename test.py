input_file_path = "C:\\Users\\trann\\OneDrive\\Máy tính\\AI train\\templates\\LOC_synset_mapping.txt"
output_file_path = "C:\\Users\\trann\\OneDrive\\Máy tính\\AI train\\templates\\LOC_synset_mapping2.txt"


with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # Tách dòng thành các phần, sử dụng dấu ',' làm dấu phân cách
        parts = line.strip().split(', ')

        # Nếu có đủ phần tử, chỉ lấy cột đầu
        if len(parts) > 0:
            column1 = parts[0]
            output_file.write(f"{column1}\n")
        else:
            # Nếu không có đủ phần tử, chỉ ghi cả dòng vào file mới
            output_file.write(line)