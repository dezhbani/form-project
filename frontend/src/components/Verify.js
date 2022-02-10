import React,{ useState, useEffect } from 'react';
import axios from 'axios';
import { validate } from './validate';
import { ToastContainer } from 'react-toastify';
import { notify } from './toast';

//style
import 'react-toastify/dist/ReactToastify.css';
import style from './Verify.module.css';

const Verify = ({state}) => {

    const [data, setData] = useState({code1: ""});
    const [erorrs, setErorrs] = useState({});
    const [touched, setTouched] = useState({});


    useEffect(() =>{
        setErorrs(validate(data, "verify"));
    }, [data, touched]);

    const focus = () =>{
        setTouched({ code: true });
    }


    const change = event =>{
        setData({[event.target.name]: event.target.value});
    }

    const send = async () =>{
        if(!Object.keys(erorrs).length){
            const res = await axios.post("http://127.0.0.1:8000/otp/verify/",{
                request_id: state.id,
                phone: state.phone,
                password: data.code1
            });
            if(res.data.new_user){
                notify("success", "ثبت نامت تکمیل شد")
            }else{ 
                notify("success", "خوش آمدی");
        }
        }else{
            setTouched({code: true});
            notify("error", "لطفا فرم رو کامل کن");
        }

    }

    return (
        <div className={style.maincontainer}>
            <div className={style.container}>
                <div className={style.form}>
                    <label className={style.label}>کد تایید:</label>
                    <input className={(touched.code && erorrs.code)? style.code : style.uncompleted} maxLength="4" onChange={change}  onFocus={focus} name='code1' value={data.code1} type="text" />
                    {erorrs.code && touched.code && <span>{erorrs.code}</span>}
                    <div className={style.button}>
                        <button type="submit" onClick={send}>send</button>
                    </div>
                </div>
            </div>
            <ToastContainer />
        </div>
    );
};

export default Verify;