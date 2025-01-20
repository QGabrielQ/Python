import time
import os
import sys
import threading
from datetime import datetime

def logo():
    # Design logo of the program (Japanese Candle Chart Creator - J3C for short)
    print(r"""-------------------------------------------------------------
          JJJJJJJJJJJ 333333333333333           CCCCCCCCCCCCC
          J:::::::::J3:::::::::::::::33      CCC::::::::::::C
          J:::::::::J3::::::33333::::::3   CC:::::::::::::::C
          JJ:::::::JJ3333333     3:::::3  C:::::CCCCCCCC::::C
            J:::::J              3:::::3 C:::::C       CCCCCC
            J:::::J              3:::::3C:::::C              
            J:::::J      33333333:::::3 C:::::C              
            J:::::j      3:::::::::::3  C:::::C              
            J:::::J      33333333:::::3 C:::::C              
JJJJJJJ     J:::::J              3:::::3C:::::C              
J:::::J     J:::::J              3:::::3C:::::C              
J::::::J   J::::::J              3:::::3 C:::::C       CCCCCC
J:::::::JJJ:::::::J  3333333     3:::::3  C:::::CCCCCCCC::::C
 JJ:::::::::::::JJ   3::::::33333::::::3   CC:::::::::::::::C
   JJ:::::::::JJ     3:::::::::::::::33      CCC::::::::::::C
     JJJJJJJJJ        333333333333333           CCCCCCCCCCCCC
-------------------------------------------------------------""")

class Candle:
    def __init__(self, Date, Volume, Open, High, Low, Close, Color, IndexOpen, IndexHigh, IndexLow, IndexClose):
       self.Date = Date
       self.Volume = Volume
       self.Open = Open
       self.High = High
       self.Low = Low
       self.Close = Close
       self.Color = Color
       self.IndexOpen = IndexOpen
       self.IndexHigh = IndexHigh
       self.IndexLow = IndexLow
       self.IndexClose = IndexClose
class bcolors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    WHITE = '\033[97m'
   

def log_time(file):
    now = datetime.now()
    file.write(now.strftime("%d.%m.%Y %H:%M:%S | "))
    

def read_file(file, file2):
    line_count = 1
    file_location = input("Insert file Directory: ")
    try:
        with open(file_location, 'r') as plik, open("data.txt", 'w') as data_write:
            log_time(file)
            file.write(f"Correct file directory inserted: {file_location}\n")
            log_time(file2)
            file2.write(f"Correct file directory inserted: {file_location}\n")
            
            output_file_name = input("Make sure the name ends with .txt!\nInsert name of the output graph file: ")
            log_time(file)
            file.write(f"Output file name inserted: {output_file_name}\n")
            log_time(file2)
            file2.write(f"Output file name inserted: {output_file_name}\n")
            
            height = int(input("Make sure the height is an int!\nInput the height of the chart: "))
            
            log_time(file2)
            file2.write("File conversion 1 (out of 2) started...\n")
            for line in plik:
                data_write.write(line.replace(',', ' '))
                line_count += 1
            log_time(file2)
            file2.write("File conversion 1 (out of 2) finished.\n")
            
            line_count -=1
            log_time(file2)
            file2.write(f"Number of lines in file: {line_count}\n")

            with open("data.txt", 'r') as data_read, open("data2.txt", 'w') as data2:
                log_time(file2)
                file2.write("File conversion 2 (out of 2) started...\n")
                for row in data_read:
                    data2.write(row.replace('\0', ' '))
                log_time(file2)
                file2.write("File conversion 2 (out of 2) finished.\n")
            
            with open("data.txt", 'r') as data2:
                data2.readline()
                candles = []
                count = 0
                log_time(file2)
                file2.write("Inserting data to structure:\n")
                for i in range(line_count):
                    line = data2.readline().split(' ')
                    
                    if len(line)<6:
                        print(f"Skipping malformed line: {line}")
                        count += 1
                        continue
                    try:
                      print(line)
                      candles.append(Candle(
                                   Date=line[0],
                                   Volume=float(line[5].strip('\n')),
                                   Open=float(line[1]),
                                   High=float(line[2]),
                                   Low=float(line[3]),
                                   Close=float(line[4]),
                                   Color="unknown",  # Determined later
                                   IndexOpen=0,      # Placeholder 
                                   IndexHigh=0,      # Placeholder 
                                   IndexLow=0,       # Placeholder 
                                   IndexClose=0      # Placeholder 
                                                ))
                    except ValueError as e:
                        print(f"Error parsing line: {line}. Error: {e}")
                log_time(file2)
                file2.write("Data successfully loaded. Check data2.txt for more details.\n")
            print(count)
            print(line_count)
            line_count -= count 
            # Min/Max algorithm
            log_time(file2)
            file2.write("Candle Min/Max algorithm started...\n")
            maxOpen = maxHigh = maxLow = maxClose = 0
            for i in range(line_count):
                maxOpen = max(maxOpen, candles[i].Open)
                maxHigh = max(maxHigh, candles[i].High)
                maxLow = max(maxLow, candles[i].Low)
                maxClose = max(maxClose, candles[i].Close)
            log_time(file2)
            file2.write(f"Max values found: {maxOpen} {maxHigh} {maxLow} {maxClose}\n")

            minOpen = minHigh = minLow = minClose = maxOpen
            for i in range(line_count):
                minOpen = min(minOpen, candles[i].Open)
                minHigh = min(minHigh, candles[i].High)
                minLow = min(minLow, candles[i].Low)
                minClose = min(minClose, candles[i].Close)
            log_time(file2)
            file2.write(f"Min values found: {minOpen} {minHigh} {minLow} {minClose}\n")

            # Overall Min/Max algorithm
            tabMax = [maxOpen, maxHigh, maxLow, maxClose]
            tabMin = [minOpen, minHigh, minLow, minClose]
            maxOverall = max(tabMax)
            log_time(file2)
            file2.write(f"Overall Max value found: {maxOverall}\n")
            minOverall = min(tabMin)
            log_time(file2)
            file2.write(f"Overall Min value found: {minOverall}\n")

            scale = (maxOverall - minOverall) / height
            log_time(file2)
            file2.write(f"Scale calculated. ({maxOverall}-{minOverall}) / {height} = {scale}\n")

            # schematic = [[0] * line_count for _ in range(height)]
            # for i in range(height):
            #     for j in range(line_count):
            #         schematic[i][j] = 0

            with open(output_file_name, 'w') as chart:
                scale_values = [maxOverall - i * scale for i in range(height)]
                print()
                log_time(file2)
                file2.write("Transforming data to fit scale...\n")
                log_time(file2)
                file2.write("Index administration started...\n")
                log_time(file2)
                file2.write("Evaluating candle color...\n")
                blackCandles = whiteCandles = 0
                with open("TransformedData.txt", 'w') as transf_data:
                    for i in range(line_count):
                        for j in range(height - 1, -1, -1):
                            current = scale_values[j]
                            next_value = scale_values[j - 1] if j > 0 else None
                            if next_value is not None and next_value > candles[i].Open > current:
                                candles[i].Open = current
                                candles[i].IndexOpen = j
                            if next_value is not None and next_value > candles[i].High > current:
                                candles[i].High = current
                                candles[i].IndexHigh = j
                            if next_value is not None and next_value > candles[i].Low > current:
                                candles[i].Low = current
                                candles[i].IndexLow = j
                            if next_value is not None and next_value > candles[i].Close > current:
                                candles[i].Close = current
                                candles[i].IndexClose = j
                            if j == height - 1 and current > candles[i].Open:
                                candles[i].Open = scale_values[height - 1]
                                candles[i].IndexOpen = height - 1
                            if j == height - 1 and current > candles[i].High:
                                candles[i].High = scale_values[height - 1]
                                candles[i].IndexHigh = height - 1
                            if j == height - 1 and current > candles[i].Low:
                                candles[i].Low = scale_values[height - 1]
                                candles[i].IndexLow = height - 1
                            if j == height - 1 and current > candles[i].Close:
                                candles[i].Close = scale_values[height - 1]
                                candles[i].IndexClose = height - 1
                            if j == 0 and current == candles[i].Open:
                                candles[i].Open = scale_values[0]
                                candles[i].IndexOpen = 0
                            if j == 0 and current == candles[i].High:
                                candles[i].High = scale_values[0]
                                candles[i].IndexHigh = 0
                            if j == 0 and current == candles[i].Low:
                                candles[i].Low = scale_values[0]
                                candles[i].IndexLow = 0
                            if j == 0 and current == candles[i].Close:
                                candles[i].Close = scale_values[0]
                                candles[i].IndexClose = 0
                        if candles[i].Open < candles[i].Close:
                            candles[i].Color = 'W'
                            whiteCandles += 1
                        else:
                            candles[i].Color = 'B'
                            blackCandles += 1
                        transf_data.write(f"Candle {i+1}: Date: {candles[i].Date}, Volume: {candles[i].Volume}, Open: {candles[i].Open}, High: {candles[i].High}, Low: {candles[i].Low}, Close: {candles[i].Close}, Color: {candles[i].Color}, IndexOpen: {candles[i].IndexOpen}, IndexHigh: {candles[i].IndexHigh}, IndexLow: {candles[i].IndexLow}, IndexClose: {candles[i].IndexClose}\n")
                log_time(file2)
                file2.write("Transforming to scale completed.\n")
                log_time(file2)
                file2.write("Indexes administered.\n")
                log_time(file2)
                file2.write(f"Colors evaluated. White candles total: {whiteCandles} Black candles total: {blackCandles} Candles total: {blackCandles + whiteCandles}\n")

                log_time(file2)
                file2.write("Encoding the Schematic table...\n")
                schematic = [[0] * line_count for _ in range(height)]
                for i in range(height):
                    for j in range(line_count):
                        schematic[i][j] = 0
                column = 0
                for i in range(line_count):
                    for j in range(height):
                        if candles[i].Color == 'W':
                            for k in range(candles[i].IndexHigh, candles[i].IndexClose + 1):
                                schematic[k][column] = 1
                            for k in range(candles[i].IndexOpen, candles[i].IndexLow + 1):
                                schematic[k][column] = 1
                            for k in range(candles[i].IndexClose, candles[i].IndexOpen + 1):
                                schematic[k][column] = 2
                        if candles[i].Color == 'B':
                            for k in range(candles[i].IndexHigh, candles[i].IndexOpen + 1):
                                schematic[k][column] = 1
                            for k in range(candles[i].IndexClose, candles[i].IndexLow + 1):
                                schematic[k][column] = 1
                            for k in range(candles[i].IndexOpen, candles[i].IndexClose + 1):
                                schematic[k][column] = 3
                    column += 1

                log_time(file2)
                file2.write("Schematic table encoded.\n")
                with open("Schematic.txt", 'w') as schema:
                    for i in range(height):
                        for j in range(line_count):
                            schema.write(str(schematic[i][j]))
                        schema.write('\n')
                log_time(file2)
                file2.write("Schematic filled. check Schematic.txt for details.\n")
                log_time(file2)
                file2.write(f"Printing chart into {output_file_name}...\n")
                max_temp = maxOverall
                for i in range(height):
                    if(max_temp < 10):
                        chart.write(f"{max_temp:.3f}  ")
                    elif(max_temp < 100 and max_temp > 10):
                        chart.write(f"{max_temp:.3f} ")
                    else:
                        chart.write(f"{max_temp:.3f}")
                    for j in range(line_count):
                        if schematic[i][j] == 0:
                            chart.write(" ")
                        elif schematic[i][j] == 1:
                            chart.write("|")
                        elif schematic[i][j] == 3:
                            chart.write("#")
                        elif schematic[i][j] == 2:
                            chart.write("O")
                    # print(f"{max_temp:.3f} ", end="")
                    # for k in range(line_count):
                    #     if schematic[i][k] == 0:
                    #         print(" ", end="")
                    #     elif schematic[i][k] == 1:
                    #         print("|", end="")
                    #     elif schematic[i][k] == 3:
                    #         print("#", end="")
                    #     elif schematic[i][k] == 2:
                    #         print("O", end="")
                    # print()
                    max_temp -= scale
                    chart.write('\n')
                
                date_parts = [candle.Date for candle in candles]  # Assuming candle.Date is in YYYY-MM-DD format
                # Print the entire date vertically under each candle
                date_height = 10  # YYYY-MM-DD is 10 characters long
                # Printing the full date vertically beneath each candle
                for i in range(date_height):
                    chart.write("       ")  # Initial space for alignment
                    for j in range(line_count):
                        if i < len(date_parts[j]):
                           chart.write(f"{date_parts[j][i]}")  # Print each character vertically under each candle
                        else:
                           chart.write(" ")  # Leave space if date is shorter
                    chart.write("\n")
                chart.write(f"Scale - {scale}\n")
                chart.write(f"Extreme values: {scale_values[height - 1]} {scale_values[0]}\n")

                log_time(file2)
                file2.write("Chart completed.\n")
                log_time(file2)
                file2.write("Deleting dynamic structures - Freeing up memory\n")

    except FileNotFoundError:
        log_time(file)
        file.write("Invalid file inserted...\n")
        log_time(file2)
        file2.write("Invalid file inserted...\n")
        read_file(file, file2)

def choice(input_char, file, file2):
    if input_char.lower() == 'q':
        log_time(file)
        file.write(f"{input_char} Pressed. Program terminated\n")
        log_time(file2)
        file2.write(f"{input_char} Pressed. Program terminated\n")
        sys.exit()
    elif input_char.lower() == 'g':
        log_time(file)
        file.write(f"Correct key inserted: {input_char}\n")
        log_time(file2)
        file2.write(f"Correct key inserted: {input_char}\n")
        read_file(file, file2)

def menu(input_char, file, file2):
    while input_char.lower() not in ['q', 'g']:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        print("Welcome to J3C! - Japanese Candle Chart Creator")
        print("Coded by: Aleksander Gabriel Piotrzkowski, Field of Study: IT, Group 4")
        print("'q/Q': Terminates Program")
        print("'g/G': Downloads data from given directory and generates a chart which is saved to chart.txt")
        input_char = input("Input: ")
        if input_char.lower() not in ['q', 'g']:
            log_time(file)
            file.write(f"Incorrect key pressed: {input_char}\n")
            log_time(file2)
            file2.write(f"Incorrect key pressed: {input_char}\n")
    choice(input_char, file, file2)

def intro(file, file2):
    log_time(file)
    file.write("Loading started...\n")
    log_time(file2)
    file2.write("Loading started...\n")
    progress = 0
    for _ in range(20):
        print("Loading...")
        print(f"[{'■' * progress}{' ' * (20 - progress)}] {progress * 5}%")
        log_time(file2)
        file2.write(f"{progress * 5}%\n")
        progress += 1
        time.sleep(0.09)
        os.system('cls' if os.name == 'nt' else 'clear')
    log_time(file)
    file.write("Loading completed.\n")
    log_time(file2)
    file2.write("Loading completed.\n")

def main():
    with open("log.txt", 'w') as log, open("debug.txt", 'w') as debug:
        log_time(log)
        log_time(debug)
        log.write("Program executed...\n")
        debug.write("Program executed..\n")
        input_char = 'a'
        intro(log, debug)
        menu(input_char, log, debug)
        log_time(log)
        log_time(debug)
        debug.write("Finished. Program terminated.\n")
        log.write("Finished. Program terminated.\n")
    print("Data read. Data converted. Chart completed. Please head to project directory to view the results.")

if __name__ == "__main__":
    main()
