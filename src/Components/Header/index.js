import { Link } from 'react-router-dom'
import './index.css'

const Header = ()=>{
    return(
        <div className="header-cont">
           <Link to="/" className='nav-link'>
           <div className="logo-cont">
            <img src="https://assets.ccbp.in/frontend/react-js/wave-logo-img.png"
                     alt="pavan" className="logo"/>
                <p>Super Wave</p>
            </div>
           </Link>
           <ul className="logo-cont">
            <li><Link to="/" className='nav-link'>Home</Link></li>
            <li><Link to="/about" className='nav-link'>About</Link></li>
            <li><Link to="/contact-us" className='nav-link'>Contact Us</Link></li>
           </ul>
        </div>
    )
}

export default Header