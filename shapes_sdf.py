import sys
import pyvips


def main():
    if len(sys.argv) < 2:
        print('Usage: python shapes_sdf.py output.png')
        sys.exit(1)

    outpath = sys.argv[1]

    try:
        # Create a rounded rectangle
        box = pyvips.Image.sdf(1000, 1000, "rounded-box",
                               a=[300, 400],
                               b=[700, 600],
                               corners=[100, 0, 0, 0])

        # Create a circle
        circle = pyvips.Image.sdf(1000, 1000, "circle",
                                  a=[500, 300],
                                  r=100)

        # Create a line
        line = pyvips.Image.sdf(1000, 1000, "line",
                                a=[500, 500],
                                b=[600, 900])

        # Union all shapes (minpair builds SDF unions)
        sdf = box.minpair(circle).minpair(line)

        # Create an outline effect by shrinking the signed distance field
        sdf = sdf.abs() - 15

        # Clamp and convert to uchar image for saving
        out = sdf.clamp().linear(-255, 255, uchar=True)
        out.write_to_file(outpath)

        print(f'Wrote {outpath}')

    except Exception as e:
        print('Error creating SDF shapes:', e)
        print('Make sure libvips is installed and pyvips can load it (libvips-42.dll on Windows).')
        sys.exit(2)


if __name__ == '__main__':
    main()
