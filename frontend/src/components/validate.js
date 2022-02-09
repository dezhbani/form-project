export const validat = (data) =>{

    const erorrs = {};

    if(data.phone){
        erorrs.phone = "شماره تلفن نمیتونه خالی باشه";
    }else if(/\D/.test(data.phone)){
        erorrs.phone = "شماره تلفن باید فقط اعداد باشه";
    }else{
        delete erorrs.phone
    };

    if(data.code){
        erorrs.code = "کد تایید نمیتونه خالی باشه";
    }else if(/\D/.test(data.code)){
        erorrs.code = "کد تایید باید فقط اعداد باشه";
    };

    return erorrs;
}