from workshop_profit import Material, MaterialUnit, MaterialUsage

if __name__ == "__main__":
    carbon = Material("carbon", 25, MaterialUnit.SQUARE_METER)
    print(carbon)
    print(MaterialUsage(carbon, 20.5))
