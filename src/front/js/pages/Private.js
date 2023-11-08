import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";



export const Private = () => {
    const { store, actions } = useContext(Context);


    const navigate = useNavigate();

    useEffect(() => {
        if (store.access_token && store.access_token !== "" && store.access_token !== undefined) {
            navigate("/login")
        }


    }, [store.access_token]);
    return (
        <div className="PrivatePageBackGroung">
            <h1> This is a private page "HI"</h1>
            



        </div>
    )


};