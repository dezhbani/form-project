export const validate = (data, type) =>{

    const erorrs = {};
if(type === "signup")
        if(!data.phone){
            erorrs.phone = "شماره تلفن نمیتونه خالی باشه";
        }else if(/\D/.test(data.phone)){
            erorrs.phone = "شماره تلفن باید فقط اعداد باشه";
        }else{
            delete erorrs.phone
        };

    if(type === "verify"){
        if(data.code1?.length < 4){
            erorrs.code = "کد تایید نمیتونه خالی باشه";
        }else if(/\D/.test(data.code1)){
            erorrs.code = "کد تایید باید فقط اعداد باشه";
        }else{
            delete erorrs.code
        }
    }

    return erorrs;
}