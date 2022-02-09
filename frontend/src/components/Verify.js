import React,{ useState } from 'react';
import axios from 'axios';

const Verify = ({state}) => {

    const [data, setData] = useState({
        code1:"", 
        code2:"", 
        code3:"", 
        code4:""
        });

    const change = event =>{
        setData({...data, [event.target.name]: event.target.value});
        console.log({...data, [event.target.name]: event.target.value})
    }
    
    
    const send = async () =>{
        const code = data.code1 + data.code2 + data.code3 + data.code4
        // console.log(state.length)
        console.log(typeof state.id);
        console.log(typeof state.phone);
        if(code.length === 4){
            const res = await axios.post("http://127.0.0.1:8000/otp/verify/",{
                request_id: state.id,
                phone: state.phone,
                password: code
            });
            console.log(res);
        }
    }
    return (
        <div>
            <input maxLength="1" onChange={change} name='code1' value={data.code1} type="text" />
            <input maxLength="1" onChange={change} name='code2' value={data.code2} type="text" />
            <input maxLength="1" onChange={change} name='code3' value={data.code3} type="text" />
            <input maxLength="1" onChange={change} name='code4' value={data.code4} type="text" />
            <button type="submit" onClick={send}>send</button>
        </div>
    );
};

export default Verify;