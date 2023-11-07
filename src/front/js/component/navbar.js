import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
		<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Login
  </button>
  <ul class="dropdown-menu">
    <li><Link to="/login"><a class="dropdown-item" href="#">Login</a></Link></li>
    <li><Link to="/signup"><a class="dropdown-item" href="#">Signup</a></Link></li>
    <li><a class="dropdown-item" href="#">Logout</a></li>
  </ul>
</div>
		</nav>
	);
};
