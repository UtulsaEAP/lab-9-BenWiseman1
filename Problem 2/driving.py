def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   return(miles_driven/miles_per_gallon)*dollars_per_gallon
   

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')

    x= driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    y= driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    z= driving_cost(miles_per_gallon, dollars_per_gallon, 400)

    print(f'{x:.2f}')
    print(f'{y:.2f}')
    print(f'{z:.2f}')
    
   