import React from "react";
import { Link } from "react-router-dom";
import { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Login = () => {
  
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false); 
  const navigate = useNavigate();

  const handleLogin = async () => {
   
    let result = await actions.login(email, password);

    if (result) {
      // Redirect to the private page
      navigate("/private");
    }
    setIsLoggedIn(true);
  };

  


  return (
    <div className="urlBackground">
      <div className="loginPage">
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">
            Email address
          </label>
          <input
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            type="email"
            name="emailInput"
            className="form-control"
            id="exampleInputEmail1"
            aria-describedby="emailHelp"
          />
        </div>
        <div className="mb-3">
          <label htmlFor="exampleInputPassword1" className="form-label">
            Password
          </label>
          <input
            onChange={(e) => setPassword(e.target.value)}
            value={password}
            type="password"
            name="passwordInput"
            className="form-control"
            id="exampleInputPassword1"
          />
        </div>

        <button onClick={handleLogin} type="submit" className="btn btn-primary">
          Submit
        </button>
      </div>
    </div>
  );
};
