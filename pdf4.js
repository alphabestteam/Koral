function starSign(date){

    const d = new Date(date)
    month = d.getMonth()
    day = d.getDate()
   
    if ((month == 0 && day >= 21) || (month == 1 && day <= 19)){
            return "Aquarius"
        }
        else if ((month == 1 && day >= 20) || (month == 2 && day <= 20)){
            return "Pisces"
        }
        else if ((month == 2 && day >= 21) || (month == 3 && day <= 20)){
            return "Aries"
        }
        else if ((month == 3 && day >= 21) || (month == 4 && day <= 21)){
            return "Taurus"
        }
        else if ((month == 4 && day >= 22) || (month == 5 && day <= 21)){
            return "Gemini"
        }
        else if ((month == 5 && day >= 22) || (month == 6 && day <= 21)){
            return "Cancer"
        }
        else if ((month == 6 && day >= 23) || (month == 7 && day <= 32)){
            return "Leo"
        }
        else if ((month == 7 && day >= 24) || (month == 8 && day <= 23)){
            return "Virgo"
        }
        else if ((month == 8 && day >= 24) || (month == 9 && day <= 23)){
            return "Libra"
        }
        else if ((month == 9 && day >= 24) || (month == 10 && day <= 22)){
            return "Scorpio"
        }
        else if ((month == 10 && day >= 23) || (month == 11 && day <= 21)){
            return "Sagittarius"
        }
        else if ((month == 11 && day >= 22) || (month == 0 && day <= 20)){
            return "Capricon"
        }

    }
