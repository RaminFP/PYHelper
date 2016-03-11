# -*- coding: utf-8 -*-
from khayyam.jalali_date import JalaliDate
import re


'''
    IsValid Function for check data is a valid or NO


'''

class IsValid(object):

    def IsValidString(self,feild, feildName, minLength, maxLength):
        try:


            if feild == None or feild == '':
                # Persion Message
                return [False, "مقدار " + feildName + " را وارد نمایید"] # Enter value of filename
                # English message
                # return [False, "pelase enter : " + feildName] # Enter value of filename
            if feild.strip() == "":
                # Persion Message
                return [False, "مقدار " + feildName + " را وارد نمایید"]
                # English Message
                #  return [False, "pelase enter : " + feildName] # Enter value of filename
            if len(feild) < minLength:
                return [False, "حداقل تعداد کاراکتر برای " + feildName + " " + str(minLength) + " کاراکتر می باشد"]
            if len(feild) > maxLength:
                return [False, "حداکثر تعداد کاراکتر برای " + feildName + " " + str(maxLength) + " کاراکتر می باشد"]

            return [True, None]
        except Exception as e:
            raise


    def IsValidInteger(self,feild, feildName, minLength, maxLength):

        try:
            if feild == None or feild == '':
                return [False, "مقدار " + feildName + " را وارد نمایید"]
            if type(feild) is int == False:
                return [False, "مقدار " + feildName + " معتبر نمی باشد"]
            if len(str(feild)) < minLength:
                return [False, "حداقل تعداد ارقام برای " + feildName + " " + str(minLength) + " کاراکتر می باشد"]
            if len(str(feild)) > maxLength:
                return [False, "حداکثر تعداد ارقام برای " + feildName + " " + str(maxLength) + " کاراکتر می باشد"]
            return [True, None]

        except Exception as e:
            raise


    def IsValidLong(self,feild, feildName, minLength, maxLength):
        try:
            if feild == None:
                return [False, "مقدار " + feildName + " را وارد نمایید"]
            if type(feild) is long == False:
                return [False, "مقدار " + feildName + " معتبر نمی باشد"]
            if len(str(feild)) < minLength:
                return [False, "حداقل تعداد ارقام برای " + feildName + " " + str(minLength) + " کاراکتر می باشد"]
            if len(str(feild)) > maxLength:
                return [False, "حداکثر تعداد ارقام برای " + feildName + " " + str(maxLength) + " کاراکتر می باشد"]

            return [True, None]
        except Exception as e:
            raise

    def DataValidation(self,persons):
        try:
            finalResult = True
            finalMessage = ""

            f = "نام"
            firstName = persons.FirstName
            result = Utility.Utillity.IsValidString(firstName, f, 0, 50)

            if result[0] == False:
                finalResult = False
                finalMessage += result[1] + '<br/>'

            f = None

            f = "نام خانوادگی"
            lastName = persons.LastName
            result = Utility.Utillity.IsValidString(lastName, f, 0, 100)

            if result[0] == False:
                finalResult = False
                finalMessage += result[1] + '<br/>'

            f = "کد ملی"
            nationalCode = persons.NationalCode
            result = Utility.Utillity.IsValidateNationalCode(nationalCode)
            if result == False:
                finalResult = False
                finalMessage += "کد ملی وارد شده معتبر نمی باشد" + '<br/>'

            f = "شهرستان"
            cityID = persons.CityID
            result = Utility.Utillity.IsValidInteger(cityID, f, 0, 8)

            if result[0] == False:
                finalResult = False
                finalMessage += result[1] + '<br/>'
            else:
                citiesBl = CitiesBL()
                cities = citiesBl.SelectOne_Cities(int(cityID))
                if cities.ID != None:
                    if cities.ParentID == None:
                        finalResult = False
                        finalMessage += "شهرستان وارد شده معتبر نمی باشد" + '<br/>'
                else:
                    finalResult = False
                    finalMessage += "شهرستان وارد شده معتبر نمی باشد" + '<br/>'

            f = "شماره همراه"
            mobile = persons.Mobile
            result = Utility.Utillity.IsValidLong(mobile, f, 11, 11)

            if result[0] == False:
                finalResult = False
                finalMessage += result[1] + '<br/>'

            f = "آدرس"
            address = persons.Address
            result = Utility.Utillity.IsValidString(address, f, 0, 255)

            if result[0] == False:
                finalResult = False
                finalMessage += result[1] + '<br/>'

            return [finalResult, finalMessage]

        except Exception as e:
            raise e


    def IsValidFlot(self,feild, feildName):
        try:
            if feild == None:
                return [False, "مقدار " + feildName + " را وارد نمایید"]
            if type(feild) is float == False:
                return [False, "مقدار " + feildName + " معتبر نمی باشد"]

            return [True, None]
        except Exception as e:
            raise

    def IsValidDate(self,pDate, pFeildName):
        try:

            result = [True, '']
            if pDate == "    /  /":
                result[1] = pFeildName + " سال، ماه و روز را کامل وارد نمایید"
                result[0] = False
                return result
            elif len(pDate.strip().replace(" ", "")) < 10:
                result[1] = pFeildName + "، عدد انتخابي براي روز اشتباه است"
                result[0] = False
                return result

            str = pDate[0: 4]
            if int(str) >= 1500 or int(str) <= 1300:
                result[1] = pFeildName + "، عدد انتخابي براي سال اشتباه است"
                result[0] = False
                return result

            m_Year = ""
            m_Month = ""
            m_Day = ""

            s = pDate.split('/')
            if len(s) == 3:
                m_Year = s[0]
                m_Month = s[1]
                m_Day = s[2]

            if (m_Year == "") or (m_Year == "13  ") or (m_Year[3:-6] == " ") or (m_Year[2:-7] == " "):
                result[1] = pFeildName + "، عدد انتخابي براي سال اشتباه است"
                result[0] = False
                return result

            if (int(m_Month) < 1) or (int(m_Month) > 12) or (m_Month[0:1] == " ") or (m_Month[1:] == " "):
                result[1] = pFeildName + "، عدد انتخابي براي ماه اشتباه است"
                result[0] = False
                return result

            if int(m_Month) < 7 and ((int(m_Day) < 1) or m_Day > 31 or (m_Day[0: 1] == " ") or (m_Day[1:] == " ")):
                result[1] = pFeildName + "، عدد انتخابي براي روز اشتباه است"
                result[0] = False
                return result

            if int(m_Month) >= 7 and ((int(m_Day) < 1 or int(m_Day) > 30) or (m_Day[0:1] == " ") or (
                        m_Day[1:] == " ")):
                result[1] = pFeildName + "، عدد انتخابي براي روز اشتباه است"
                result[0] = False
                return result

            return result

        except Exception as e:
            raise

    '''

        Check valid time

    '''
    def IsValidTime(self,pTime, pFeildName):
        try:

            result = [True, '']
            if pTime == "" and pTime == None:
                result[1] = pFeildName + " زمان را کامل وارد نمایید"
                result[0] = False
                return result

            str = pTime.split(':')

            # str = pTime[0: 2]
            if int(str[0]) > 23 or int(str[0]) < 0:
                result[1] = pFeildName + "، عدد انتخابي براي ساعت اشتباه است"
                result[0] = False
                return result

            # str = pTime[3: 0]
            if int(str[1]) > 59 or int(str[1]) < 0:
                result[1] = pFeildName + "، عدد انتخابي براي دقیقه اشتباه است"
                result[0] = False
                return result


            return result

        except Exception as e:
            raise

    '''

        Check IsValidateNationalCode Number less 10 number

    '''

    def IsValidateNationalCode(self,input):
        try:
            if not re.search(r'^\d{10}$', input):
                return False

            check = int(input[9])
            s = sum(map(lambda x: int(input[x]) * (10 - x), range(0, 9))) % 11
            return s < 2 and check == s or s >= 2 and check + s == 11
        except Exception as e:
            raise


    '''

        Convert DateDecimal To String

    '''

    def ConvertDateDecimalToString(self,pDateDecimal):
        return str(pDateDecimal)[0: 4] + "/" + str(pDateDecimal)[4: -2] + "/" + str(pDateDecimal)[6:]


    def ConvertShamsiDateToDateTime(self,pDateDecimal):
        return JalaliDate(int(str(pDateDecimal)[0: 4]),
                          int(str(pDateDecimal)[4: -2]),
                          int(str(pDateDecimal)[6:])).todate()
