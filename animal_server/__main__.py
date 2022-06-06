from create_app import create_app


def main():
    create_app().run(host='localhost', port=8092)


if __name__ == '__main__':
    main()