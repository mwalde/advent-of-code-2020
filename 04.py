test_passports = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

part_two_test_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

import re
                                
class passport:
    def __init__(self,passport_list):
        self.passport_dict = {'byr' : '', 
                                'iyr' : '', 
                                'eyr' : '', 
                                'hgt' : '', 
                                'hcl' : '', 
                                'ecl' : '', 
                                'pid' : '', 
                                'cid' : '' }
        self.reg_dict = {'byr' : r'19[2-9][0-9]|200[0-2]', 
                            'iyr' : r'201[0-9]|2020', 
                            'eyr' : r'202[0-9]|2030', 
                            'hgt' : r'((1[5-8][0-9])|(19[0-3]))cm|((59)|(6[0-9])|(7[0-6]))in', 
                            'hcl' : r'#[0-9[a-f]{6}', 
                            'ecl' : r'amb|blu|brn|gry|grn|hzl|oth', 
                            'pid' : r'[0-9]{9}', 
                            'cid' : '' }
        self.good_dict = {'byr' : False, 
                            'iyr' : False, 
                            'eyr' : False, 
                            'hgt' : False,
                            'hcl' : False, 
                            'ecl' : False, 
                            'pid' : False, 
                            'cid' : True }
        self.bad_passport = True
        self.good_passport = True
        self.fill_passport(passport_list)
                                                        
                                                        
    def fill_passport(self,passport_list):
        for item in passport_list:
            if item == '': continue
            pkey = item.split(':')[0]    
            pval = item.split(':')[1]
            self.passport_dict[pkey] = pval    
                    
    def check_passport_part1(self):                            
        for key in self.passport_dict:
            if key == 'cid': continue
            if self.passport_dict[key] == '': self.bad_passport = True

    def update_good_password(self):
        for key in self.good_dict:
            self.good_passport = self.good_passport and self.good_dict[key]

    def check_passport_part2(self):                            
        for key in self.passport_dict:
            if key == 'cid': continue
            if re.match(self.reg_dict[key], self.passport_dict[key]): 
                self.good_dict[key] = True
            #print(key, self.passport_dict[key], self.good_dict[key])
        self.update_good_password()
        return self.good_passport


file = open("./puzzles/input_04.txt")
passports = file.read()
file.close()

# passports = test_passports
# passports = part_two_test_passports

pp_array = []
for line in passports.split('\n\n'):
    line = line.replace('\r',' ').replace('\n',' ')
    pp_array.append(passport(line.split(' ')))

valid_passports = 0
for p in pp_array:
    if p.check_passport_part2(): 
    #if p.check_passport_part1():
    	valid_passports += 1
    else:
#        for key in p.good_dict:
#            print(key, p.good_dict[key], p.passport_dict[key], p.reg_dict[key])
        pass

print(valid_passports-1)


