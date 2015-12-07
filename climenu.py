import pypodder

__VERSION__ = 'v0.1.0'

def main():
    '''
    Provides a basic CLI approach to interacting with the user
    '''
    print('pypodder %s' % __VERSION__)
    inp = input('Please input RSS URL: ')

    if inp is not None:
        running = True
        xm = pypodder.getXML(inp)
        flist = pypodder.fileList(xm)
        flist.reverse()
        downfiles = []

        # Show the interface
        while running:
            for i in range(len(flist)):
                print('%d) %s' % (i, flist[i][0]))

            sel = input('Download what? (q)uit or [0-%d]: ' % (len(flist)-1))

            if sel == '':
                continue
            elif sel == 'q':
                running = False
            else:
                sel = int(sel)
                downfiles.append((sel, flist[sel][1]))

        # Sanity checking
        if len(downfiles) == 0:
            return

        # Remove duplicates
        downfiles = list(set(downfiles))

        # Tell the user what they're going to download
        print('Will download the following: ')
        print(', '.join(map(lambda i: flist[i[0]][0], downfiles)), '\n')

        # Download the files
        fmt = input('Please input download location (use %d): ')

        if fmt.find('%d') >= 0 or len(downfiles) == 1:
            for (s, u) in downfiles:
                print('Downloading "%s"' % flist[s][0])
                if len(downfiles) == 1:
                    pypodder.downloadFile(u, fmt)
                else:
                    pypodder.downloadFile(u, fmt % s)


main()
