def convert_p6_to_p3(input_path):
    with open(input_path, 'rb') as f:
        def readline_skip_comments():
            while True:
                line = f.readline()
                if not line.startswith(b'#') and line.strip():
                    return line

        magic = f.readline().strip()
        if magic != b'P6':
            raise ValueError("Not a valid P6 file")

        dimensions = readline_skip_comments()
        width, height = map(int, dimensions.strip().split())

        maxval_line = readline_skip_comments()
        maxval = int(maxval_line.strip())

        pixel_data = f.read()
        expected_len = width * height * 3
        if len(pixel_data) < expected_len:
            raise ValueError("Pixel data too short")
        elif len(pixel_data) > expected_len:
            pixel_data = pixel_data[:expected_len]

    output_path = "/home/s32217109/colorP6File_p3.ppm"
    with open(output_path, 'w') as f:
        f.write("P3\n")
        f.write(f"# Converted from P6 to P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for i in range(0, expected_len, 3):
            r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
            f.write(f"{r} {g} {b}\n")

if __name__ == "__main__":
    convert_p6_to_p3("/home/data/colorP6File.ppm")

