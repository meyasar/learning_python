

def greater_than_0(num):
    while num < 0:
        num = int(input("Please enter valid number : "))
    
    return num

def greater_than_previous(num1,num2):
    while num2 < num1:
        num2 = int(input(f"Please enter a number equal or greater than {num1} : "))

    return num2

def get_previous_daytime_period():
    previous_daytime_period = int(input("Please enter your previous daytime period meter value : "))# Has to be greater than or equal to 0
    previous_daytime_period = greater_than_0(previous_daytime_period)
    return previous_daytime_period

def get_previous_peak_period():
    previous_peak_period = int(input("Please enter your previous peak period meter value : "))
    previous_peak_period = greater_than_0(previous_peak_period)
    return previous_peak_period

def get_previous_night_period():
    previous_night_period = int(input("Please enter your previous night period meter value : "))
    previous_night_period = greater_than_0(previous_night_period)
    return previous_night_period

def get_current_daytime_period():
    current_daytime_period = int(input("Please enter your current daytime period meter value : "))
    current_daytime_period = greater_than_previous(previous_daytime_period,current_daytime_period)
    return current_daytime_period

def get_current_peak_period():
    current_peak_period = int(input("Please enter your current peak period meter value : "))
    current_peak_period = greater_than_previous(previous_peak_period, current_peak_period)
    return current_peak_period

def get_current_night_period():
    current_night_period = int(input("Please enter your current night period meter value : "))
    current_night_period = greater_than_previous(previous_night_period, current_night_period)
    return current_night_period

def type_abbreviation(type):
    if type == "I" or type == "i":
        return "Industry"
    elif type == "P" or type == "p":
        return "Public and Private Services Sector and Other"
    elif type == "R" or type == "r":
        return "Residential"
    elif type == "A" or type == "a":
        return "Agricultural Activities"
    elif type == "L" or type == "l":
        return "Lightning"

        
def valid_character(char,*characters):
    while char not in characters:
        char = input(f"Enter valid character {characters} : ")
        
    return char
    
def save_highest_amount_consumer(consumer_no, total_electricity_consumption_this_period,highest_amount_consumed_bill,highest_amount_consumed_type, highest_amount_residential_consumer, highest_amount_consumed,consumer_type_code):
    if is_consumer_type_residential:

        return save_highest_amount_residential_consumer(consumer_no, total_electricity_consumption_this_period,highest_amount_consumed_bill, highest_amount_residential_consumer, highest_amount_consumed)
            
        
    else:
        return save_highest_amount_other_consumer(consumer_no, total_electricity_consumption_this_period,highest_amount_consumed_bill,highest_amount_consumed_type, highest_amount_residential_consumer, highest_amount_consumed,consumer_type_code)

def save_highest_amount_residential_consumer(consumer_no, total_electricity_consumption_this_period,highest_amount_consumed_bill, highest_amount_residential_consumer, highest_amount_consumed):
    if total_electricity_consumption_this_period > highest_amount_consumed:

        if is_preferred_tariff_multi:
            highest_amount_consumed_bill = multi_final_price
        else:
            highest_amount_consumed_bill = single_final_price

        return consumer_no, total_electricity_consumption_this_period, highest_amount_consumed_bill
        
    else:

        return highest_amount_residential_consumer, highest_amount_consumed, highest_amount_consumed_bill
    
def save_highest_amount_other_consumer(consumer_no, total_electricity_consumption_this_period,highest_amount_consumed_bill,highest_amount_consumed_type, highest_amount_consumer_other, highest_amount_consumed,consumer_type_code):

    if is_preferred_tariff_multi:
        consumed_bill = multi_final_price
    else:
        consumed_bill = single_final_price

    if consumed_bill > highest_amount_consumed_bill:

        highest_amount_consumed_type = consumer_type_code

        return consumer_no, total_electricity_consumption_this_period, consumed_bill, highest_amount_consumed_type

    else:

        return highest_amount_consumer_other, highest_amount_consumed, highest_amount_consumed_bill, highest_amount_consumed_type

def final_prices(singletime_energy_fee, unit_distribution_fee, total_electricity_consumption_this_period, ect_rate, vat_rate):
    taxless_price = singletime_energy_fee * total_electricity_consumption_this_period#Didn't multiply by 100 because we are using TL
    with_ect_price = taxless_price * ect_rate
    final_price = (with_ect_price + unit_distribution_fee*total_electricity_consumption_this_period) * vat_rate
    return taxless_price, with_ect_price, final_price

def print_final_calculations():# While loopundan çıktıktan sonra printlenecek bilgiler.
    total_consumer = industrial_consumer_counter + residential_consumer_counter + public_and_private_consumer_counter + agriculture_consumer_counter + lighting_consumer_counter
    bornova_electricity_consumption = industrial_electricity_consumption + residential_electricity_consumption + public_and_private_electricity_consumption + agriculture_electricity_consumption + lighting_electricity_consumption

    print("-------------------------------------------")
    print(f"The number of consumers who chose industry is {industrial_consumer_counter}. Their percentage is {industrial_consumer_counter/total_consumer*100}%. ")
    print(f"The number of consumers who chose public and private services sector and other is {public_and_private_consumer_counter}. Their percentage is {public_and_private_consumer_counter/total_consumer*100}%. ")
    print(f"The number of consumers who chose residential is {residential_consumer_counter}. Their percentage is {residential_consumer_counter/total_consumer*100}%. ")
    print(f"The number of consumers who chose agricultural activies is {agriculture_consumer_counter}. Their percentage is {agriculture_consumer_counter/total_consumer*100}%. ")
    print(f"The number of consumers who chose lighting is {lighting_consumer_counter}. Their percentage is {lighting_consumer_counter/total_consumer*100}%. ")

    if industrial_day_counter != 0:
        print(f"Industrial total electricity consumption is {industrial_electricity_consumption}. Average Industrial electricity consumption in this period is: {industrial_electricity_consumption/industrial_day_counter:.2f}")
    if public_and_private_day_counter != 0:
        print(f"Public and private total electricity consumption is {public_and_private_electricity_consumption}. Average Public and Private electricity consumption in this period is: {public_and_private_electricity_consumption/public_and_private_day_counter:.2f}")
    if residential_day_counter != 0:
        print(f"Residential electricity total electricity consumption is {residential_electricity_consumption}. Average  Residential electricity consumption in this period is: {residential_electricity_consumption/residential_day_counter:.2f}")
    if agricultural_day_counter != 0:
        print(f"Agricultural activities total electricity consumption is {agriculture_electricity_consumption}. Average Agricultural electricity activities electricity consumption in this period is: {agriculture_electricity_consumption/agricultural_day_counter:.2f}")
    if lightning_day_counter != 0:
        print(f"Lighting total electricity consumption is {lighting_electricity_consumption}. Average Lighting electricity consumption in this period is: {lighting_electricity_consumption/lightning_day_counter:.2f}")

    print(f"Total electricity consumption in Bornova is {bornova_electricity_consumption}.")

    if public_and_private_consumer_counter > 0:
        print(f"Number of public and private services sector and other type consumers who prefer single-time is {single_time_public_and_private_counter}. Their percentage among public and private services sector and other type consumers is {single_time_public_and_private_counter/public_and_private_consumer_counter*100}%")
        print(f"Number of public and private services sector and other type consumers who prefer multi-time is {multi_time_public_and_private_counter}. Their percentage among public and private services sector and other type consumers is {multi_time_public_and_private_counter/public_and_private_consumer_counter*100}%")
    if industrial_consumer_counter > 0:
        print(f"The number of consumers who chose industry whose electricity consumption amount is more than 10000 kWh or whose electricity bill is more than 100000 TL in the relevant period is {industry_over_10000kw_or_over_100000_tl_counter}. Their percentage among industry type consumers {industry_over_10000kw_or_over_100000_tl_counter/industrial_consumer_counter*100}%.")

    print(f"Consumer no of the residential type consumer with the highest daily average electricity consumption amount in the relevant period : {highest_amount_residential_consumer}.")
    print(f"This consumer's daily average electricity consumption amount is {highest_amount_consumed_residential:.2f}. His total bill amount for this period is {(highest_amount_consumed_residential_bill):.2f}.")
    print(f"Consumer no of the consumer other than the residential type with the highest total bill amount in the relevant period is {highest_amount_consumer_other}. This consumer's consumer type is {type_abbreviation(highest_amount_consumed_type)}. Daily average electricity consumption amount is {highest_amount_consumed_other}. Total bill amount is {highest_amount_consumed_other_bill:.2f}.  ")

    if is_preferred_tariff_multi:
        print(f"Total revenue obtained by the GDZ corporation is {multi_taxless_price:.2f}")
        print(f"Total revenue obtained by the municipality is {multi_with_ect_price - multi_taxless_price:.2f}")
        print(f"Total revenue obtained by the state is {multi_final_price - multi_with_ect_price:.2f}")
    else:
        print(f"Total revenue obtained by the GDZ corporation is {single_taxless_price:.2f}")
        print(f"Total revenue obtained by the municipality is {single_with_ect_price - single_taxless_price:.2f}")
        print(f"Total revenue obtained by the state is {single_final_price - single_with_ect_price:.2f}")

    print(f"Among consumers other than residential (family of martyrs or veterans) type and lighting type, the percentage of those who made a loss despite choosing multi-time tarif is {made_loss_counter/(total_consumer - (residential_marty_or_veteran_counter + lighting_consumer_counter))*100}%")

    print("-------------------------------------------")

if __name__ == "__main__": # Bu güvenli olmasını sağlıyormuş, başkalarının import etmesini engelliyormuş.
    industrial_consumer_counter = 0
    public_and_private_consumer_counter = 0
    public_and_private_consumer_low_tariff_counter = 0
    public_and_private_consumer_high_tariff_counter = 0
    residential_consumer_counter = 0
    residential_consumer_low_tariff_counter = 0
    residential_consumer_high_tariff_counter = 0
    agriculture_consumer_counter = 0
    lighting_consumer_counter = 0
    industrial_electricity_consumption = 0
    public_and_private_electricity_consumption = 0
    residential_electricity_consumption = 0
    agriculture_electricity_consumption = 0
    lighting_electricity_consumption = 0
    multi_time_public_and_private_counter = 0
    single_time_public_and_private_counter = 0
    free_consumer_counter = 0
    industry_over_10000kw_or_over_100000_tl_counter = 0
    made_loss_counter = 0
    residential_marty_or_veteran_counter = 0
    is_free_consumer = False
    highest_amount_residential_consumer = -1
    highest_amount_consumed = -1
    highest_amount_consumed_bill = -1
    highest_amount_consumed_other = -1
    highest_amount_consumed_other_bill = -1
    highest_amount_consumer_other = -1
    highest_amount_consumed_type = ""
    highest_amount_consumed_residential = -1
    highest_amount_consumed_residential_bill = -1
    industrial_day_counter = 0
    public_and_private_day_counter = 0
    residential_day_counter = 0
    agricultural_day_counter = 0
    lightning_day_counter = 0




    consumer_no = int(input("Please enter your consumer no : "))
    consumer_no = greater_than_0(consumer_no)

    while consumer_no > 0:
        consumer_type_code = input("Please enter your consumer type code (I/i/P/p/R/r/A/a/L/l) : ")
        consumer_type_code = valid_character(consumer_type_code,"I","i","P","p","R","r","A","a","L","l")

        is_martyr_or_veteran = ""
        preferred_tariff = "s" # This is 's' because of light and Families of martyr and veterans we don't ask their preferred tariff.

        is_consumer_type_industry = consumer_type_code == "I" or consumer_type_code == "i"
        is_consumer_type_agriculture = consumer_type_code == "A" or consumer_type_code == "a"
        is_consumer_type_public_and_private = consumer_type_code == "P" or consumer_type_code == "p"
        is_consumer_type_lighting = consumer_type_code == "L" or consumer_type_code == "l"
        is_consumer_type_residential = consumer_type_code == "R" or consumer_type_code == "r"

        is_consumer_martyr_or_veteran = False

        if is_consumer_type_residential:
            is_martyr_or_veteran = input("Do you have a martyr or a veteran in your family?(Y/y/N/n) : ") #Checks if the consumer is a family of a martyr or a veteran
            is_martyr_or_veteran = valid_character(is_martyr_or_veteran,"Y","y","N","n")

        is_consumer_martyr_or_veteran = is_martyr_or_veteran == "y" or is_martyr_or_veteran == "Y"

        if is_consumer_martyr_or_veteran:
            residential_marty_or_veteran_counter += 1

        
        if (not is_consumer_martyr_or_veteran) and not is_consumer_type_lighting:
            preferred_tariff = input("What is your preferred tariff?(S/s/M/m) : ")
            preferred_tariff = valid_character(preferred_tariff,"S","s","M","m")

        is_preferred_tariff_multi = preferred_tariff == "M" or preferred_tariff == "m"
        is_preferred_tariff_single = preferred_tariff == "S" or preferred_tariff == "s"

        previous_daytime_period = get_previous_daytime_period()
        current_daytime_period = get_current_daytime_period()
        previous_peak_period = get_previous_peak_period()
        current_peak_period = get_current_peak_period()
        previous_night_period = get_previous_night_period()
        current_night_period = get_current_night_period()

        day_time_period = current_daytime_period - previous_daytime_period
        peak_period = current_peak_period - previous_peak_period
        night_period = current_night_period - previous_night_period
        
        total_electricity_consumption_this_period = day_time_period + peak_period + night_period
        days_between_reading_dates = int(input("Please enter how many days has it been since the last reading date : "))
        total_electricity_consumption_this_year = int(input("Please enter how much electricity you consumed this year : "))

        daily_electricity_consumption = total_electricity_consumption_this_period / days_between_reading_dates

        if total_electricity_consumption_this_year > 1000:
                is_free_consumer = True
                free_consumer_counter += 1

        if is_consumer_type_public_and_private:

            if daily_electricity_consumption <= 30:
                low_or_high_tariff = "Low tariff"
            else:
                low_or_high_tariff = "High tariff"

        if is_consumer_type_residential and not is_consumer_martyr_or_veteran:

            if daily_electricity_consumption <= 8:
                low_or_high_tariff = "Low tariff"
            else:
                low_or_high_tariff = "High tariff"

        if is_consumer_type_industry:
            #We used TL here instead of kr
            singletime_energy_fee = 3.053828
            daytime_energy_fee = 3.091833
            peak_energy_fee = 4.909037
            night_energy_fee = 1.625171
            unit_distribution_fee = 0.647998
            ect_rate = 1.01
            vat_rate = 1.20
            industrial_consumer_counter += 1
            industrial_electricity_consumption += total_electricity_consumption_this_period
            industrial_day_counter += days_between_reading_dates

            single_taxless_price, single_with_ect_price, single_final_price = final_prices(singletime_energy_fee,
                                                                                           unit_distribution_fee,
                                                                                           total_electricity_consumption_this_period,
                                                                                           ect_rate, vat_rate)

        elif is_consumer_type_public_and_private:

            ect_rate = 1.05
            vat_rate = 1.20
            public_and_private_consumer_counter += 1
            public_and_private_electricity_consumption += total_electricity_consumption_this_period
            public_and_private_day_counter += days_between_reading_dates

            singletime_energy_fee = 1.912220
            daytime_energy_fee = 2.858616
            peak_energy_fee = 4.588843
            night_energy_fee = 1.481941
            unit_distribution_fee = 0.878175

            if daily_electricity_consumption > 30:
                low_tariff_cons = 30
            else:
                public_and_private_consumer_low_tariff_counter += 1
                low_tariff_cons = daily_electricity_consumption

            single_taxless_price, single_with_ect_price, single_final_price = final_prices(singletime_energy_fee,
                                                                                           unit_distribution_fee,
                                                                                           low_tariff_cons * days_between_reading_dates,
                                                                                           ect_rate, vat_rate)

            if low_or_high_tariff == "High tariff":
                extra_consumption = (daily_electricity_consumption - 30) * days_between_reading_dates
                singletime_energy_fee = 2.828414
                daytime_energy_fee = 2.858616
                peak_energy_fee = 4.588843
                night_energy_fee = 1.481941
                unit_distribution_fee = 0.878175
                public_and_private_consumer_high_tariff_counter += 1

                high_single_taxless_price, high_single_with_ect_price, high_single_final_price = final_prices(
                    singletime_energy_fee,
                    unit_distribution_fee,
                    extra_consumption,
                    ect_rate, vat_rate)
                single_taxless_price, single_with_ect_price, single_final_price = (
                            single_taxless_price + high_single_taxless_price), (
                            single_with_ect_price + high_single_with_ect_price), (
                            single_final_price + high_single_final_price)



        elif is_consumer_type_residential:

            ect_rate = 1.05
            vat_rate = 1.1
            residential_consumer_counter += 1
            residential_electricity_consumption += total_electricity_consumption_this_period
            residential_day_counter += days_between_reading_dates

            if not is_consumer_martyr_or_veteran:

                singletime_energy_fee = 0.482187
                daytime_energy_fee = 1.157700
                peak_energy_fee = 2.083645
                night_energy_fee = 0.417225
                unit_distribution_fee = 0.858883


                if daily_electricity_consumption > 8:
                    low_tariff_cons = 8
                else:
                    residential_consumer_low_tariff_counter += 1
                    low_tariff_cons = daily_electricity_consumption

                single_taxless_price, single_with_ect_price, single_final_price = final_prices(singletime_energy_fee,
                                                                                               unit_distribution_fee,
                                                                                               low_tariff_cons*days_between_reading_dates,
                                                                                               ect_rate, vat_rate)

                if low_or_high_tariff == "High tariff":
                    extra_consumption = (daily_electricity_consumption - 8) * days_between_reading_dates
                    singletime_energy_fee = 1.132271
                    daytime_energy_fee = 1.157700
                    peak_energy_fee = 2.083645
                    night_energy_fee = 0.417225
                    unit_distribution_fee = 0.858883
                    residential_consumer_high_tariff_counter += 1
                    high_single_taxless_price, high_single_with_ect_price, high_single_final_price = final_prices(
                        singletime_energy_fee,
                        unit_distribution_fee,
                        extra_consumption,
                        ect_rate, vat_rate)
                    single_taxless_price, single_with_ect_price, single_final_price = (single_taxless_price + high_single_taxless_price), (single_with_ect_price + high_single_with_ect_price), (single_final_price + high_single_final_price)
                
            else:
                singletime_energy_fee = 0.061590
                unit_distribution_fee = 0.582521
                single_taxless_price, single_with_ect_price, single_final_price = final_prices(singletime_energy_fee,
                                                                                               unit_distribution_fee,
                                                                                               total_electricity_consumption_this_period,
                                                                                               ect_rate, vat_rate)


        elif is_consumer_type_agriculture:
            
            singletime_energy_fee = 1.653096
            daytime_energy_fee = 1.704822
            peak_energy_fee = 2.800325
            night_energy_fee = 0.771882
            unit_distribution_fee = 0.721579
            ect_rate = 1.05
            vat_rate = 1.1
            agriculture_consumer_counter += 1
            agriculture_electricity_consumption += total_electricity_consumption_this_period
            agricultural_day_counter += days_between_reading_dates

            single_taxless_price, single_with_ect_price, single_final_price = final_prices(singletime_energy_fee,
                                                                                           unit_distribution_fee,
                                                                                           total_electricity_consumption_this_period,
                                                                                           ect_rate, vat_rate)

        else:
            singletime_energy_fee = 2.595835
            unit_distribution_fee = 0.841099
            ect_rate = 1.05
            vat_rate = 1.20
            lighting_consumer_counter += 1
            lighting_electricity_consumption += total_electricity_consumption_this_period
            lightning_day_counter += days_between_reading_dates

            single_taxless_price, single_with_ect_price, single_final_price = final_prices(singletime_energy_fee,
                                                                                           unit_distribution_fee,
                                                                                           total_electricity_consumption_this_period,
                                                                                           ect_rate, vat_rate)

        
        #Multi Time Unit Energy Prices
        if not is_consumer_type_lighting and (not is_consumer_martyr_or_veteran):
            multi_taxless_price = (daytime_energy_fee*day_time_period) + (peak_energy_fee*peak_period) + (night_energy_fee*night_period)
            multi_with_ect_price = multi_taxless_price * ect_rate
            multi_final_price = (multi_with_ect_price + unit_distribution_fee*total_electricity_consumption_this_period) * vat_rate

        if is_consumer_type_residential:
            highest_amount_residential_consumer, highest_amount_consumed_residential, highest_amount_consumed_residential_bill = save_highest_amount_consumer(consumer_no, daily_electricity_consumption,highest_amount_consumed_residential_bill,highest_amount_consumed_type, highest_amount_residential_consumer, highest_amount_consumed_residential,consumer_type_code)
        else:
            highest_amount_consumer_other, highest_amount_consumed_other, highest_amount_consumed_other_bill, highest_amount_consumed_type = save_highest_amount_consumer(consumer_no, daily_electricity_consumption, highest_amount_consumed_other_bill,highest_amount_consumed_type, highest_amount_consumer_other, highest_amount_consumed_other,consumer_type_code)
        print("-------------------------------------------")
        print(f"Consumer no : {consumer_no}")
        print(f"Consumer Type : {type_abbreviation(consumer_type_code)}")
        if is_preferred_tariff_multi:
            print(f"Your daytime period electricity consumption in this period is : {day_time_period} ")  # ??????
            print(f"Peak period electricity consumption amount in this period : {peak_period}")
            print(f"Night period electricity consumption amount in this period : {night_period}")
        print(f"Total electricity consumption amount in this period : {total_electricity_consumption_this_period}")

        if is_preferred_tariff_multi:
            if is_consumer_type_public_and_private:
                multi_time_public_and_private_counter += 1

            print(f"Total electricity consumption fee for this period : {multi_taxless_price:.2f}")
            print(f"ECT amount to be transferred to the municipality this period : {(multi_with_ect_price - multi_taxless_price):.2f}")
            print(f"VAT amount to be transferred to the state this period : {multi_final_price - (multi_with_ect_price + unit_distribution_fee * total_electricity_consumption_this_period):.2f}")
            print(f"Total invoice amount for this period : {multi_final_price:.2f}")
            
            if multi_final_price > single_final_price:
                print(f"If you used single time tariff your profit would be {multi_final_price - single_final_price:.2f}")
            elif multi_final_price < single_final_price:
                print(f"If you used single time tariff your loss would be {single_final_price - multi_final_price:.2f}")
            else:
                print(f"If you used single time tariff you would have paid the same price!")

            print(f"Total electricity consumption in this years is {total_electricity_consumption_this_year:.2f}")

        else:
            if is_consumer_type_public_and_private:
                single_time_public_and_private_counter += 1

            
            print(f"Total electricity consumption fee for this period : {single_taxless_price:.2f}")
            print(f"ECT amount to be transferred to the municipality this period : {(single_with_ect_price - single_taxless_price):.2f}")
            print(f"VAT amount to be transferred to the state this period : {(single_final_price - (single_with_ect_price + unit_distribution_fee*total_electricity_consumption_this_period)):.2f}")
            print(f"Total invoice amount for this period : {single_final_price:.2f}")

            if not is_consumer_type_lighting and (not is_consumer_martyr_or_veteran):
                if single_final_price > multi_final_price:
                    print(f"If you used multi time tariff your profit would be {(single_final_price - multi_final_price):.2f}")
                elif single_final_price < multi_final_price:
                    print(f"If you used multi time tariff your loss would be {(multi_final_price - single_final_price):.2f}")
                else:
                    print(f"If you used multi time tariff you would have paid the same price")

            print(f"Total electricity consumption in this years is {total_electricity_consumption_this_year:.2f}")

            if is_free_consumer:
                print("You deserve to be a free consumer!")

        if is_consumer_type_industry:

            if is_preferred_tariff_multi:
                is_over_10000kw_or_over_100000_tl = total_electricity_consumption_this_period > 10_000 or multi_final_price > 100_000
            else:
                is_over_10000kw_or_over_100000_tl = total_electricity_consumption_this_period > 10_000 or single_final_price > 100_000
            
            if is_over_10000kw_or_over_100000_tl:
                industry_over_10000kw_or_over_100000_tl_counter += 1


        

        if is_consumer_martyr_or_veteran or is_consumer_type_lighting:
            if is_preferred_tariff_multi:
                if multi_final_price < single_final_price:
                    made_loss_counter += 1

        is_free_consumer = False

        print("-------------------------------------------")
        consumer_no = int(input("Please enter your consumer no (Enter 0 if you want to leave) : "))

        if (consumer_no == 0):
            
            print_final_calculations()
            
