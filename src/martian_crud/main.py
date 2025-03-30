from .app import app

def main():
    """This is what martian-compiler will run"""
    app.run(debug=True)

# running with python -m martian_crud.main
if __name__ == '__main__':
    main()
