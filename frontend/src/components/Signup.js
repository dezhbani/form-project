import React, { useState, useEffect } from 'react';
import { validate } from './validate';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { ToastContainer } from 'react-toastify';
import { notify } from './toast';

//styles
import 'react-toastify/dist/ReactToastify.css';
import style from'./Signup.module.css';

const Signup = ({state, setState}) => {

    const navigate = useNavigate();
    const [data, setData] = useState({phone: ""});
    const [erorrs, setErorrs] = useState({});
    const [touched, setTouched] = useState({});

    console.log(Object.keys(erorrs).length);

    useEffect(() =>{
        setErorrs(validate(data, "signup"));
        console.log(erorrs)
    }, [data, touched]);

    const focus = event =>{
        setTouched({ ...touched, [event.target.name]: true });
        // setErorrs(validate(data));
        // console.log(erorrs);
    }

    const change = event =>{
        setData({[event.target.name]: event.target.value});
    }

    const clicked = async () =>{
        if(!Object.keys(erorrs).length){
            const res = await axios.post("http://127.0.0.1:8000/otp/request/",{
                phone: data.phone
            });
            setState({id: res.data.request_id, phone: data.phone});
            console.log(res);
            console.log(state);
    
            if(res.status === 200){
                notify("success", "کد تایید ارسال شد")
                const navigat = () =>{
                    navigate('/sign-up/verify')
                }
                setTimeout(navigat, 5500);
            };

        }else{ 
            setTouched({phone: true});
            notify("error", "لطفا فرم را کامل کنید");
    };

    }



    return (
        <div className={style.maincontainer}>
            <div className={style.container}>
                <h2 className={style.header}>Sign Up</h2>
                <div className={style.formfield}>
                    <label className={style.label}>شماره تلفن:</label>
                    <input className={(touched.phone && erorrs.phone)? style.uncompleted : style.phone} type="tel" value={data.phone} onFocus={focus} onChange={change} name='phone' placeholder='شماره تلفن' />
                    {erorrs.phone && touched.phone && <span>{erorrs.phone}</span>}

                    <div className={style.buttons}>
                        <button onClick={clicked} type="submit">تایید</button>
                    </div>
                </div>
            </div>
            <ToastContainer />
        </div>
    );
};

export default Signup;