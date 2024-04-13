import csv
import random
import argparse

def filter_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Lấy header
        
        # Tạo một list chứa tất cả các dòng (trừ header)
        lines = [line for line in reader]

    # Tính toán số dòng cần lọc
    num_lines_to_keep = int(len(lines) * 0.1)
    
    # Lọc ra 10% dòng ngẫu nhiên
    random_lines = []
    for i in range(num_lines_to_keep):
        random_lines.append(lines[i])

    # Ghi vào file output
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Viết header
        writer.writerows(random_lines)

def main():
    parser = argparse.ArgumentParser(description='Filter CSV file to keep 10% of lines')
    parser.add_argument('input_file', help='Input CSV file path')
    parser.add_argument('output_file', help='Output CSV file path')
    args = parser.parse_args()

    filter_csv(args.input_file, args.output_file)
    print("Done!")

if __name__ == "__main__":
    main()
