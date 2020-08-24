from src import scrap


if __name__ == "__main__":
    data = scrap("pe", "recife")
    
    print(data.relatorio())
    print(data.min())
    print(data.max())