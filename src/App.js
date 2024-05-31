import { Route,Routes} from "react-router-dom"
import Header from './Components/Header';
import Home from './Components/Home';
import About from './Components/About';
import ContactUs from './Components/ContactUs';
import NotFound from "./Components/NotFound";
import './index.css'

const App = ()=> {
    return(
        <div className="bg-container">
            <Header/>
           <Routes>
           <Route  exact path="/" Component={Home}/>
           <Route  path="/home" Component={Home}/>
           <Route  path="/about" Component={About}/>
           <Route  path="/contact-us" Component={ContactUs}/>
           <Route  path="*" Component={NotFound}/>
           </Routes>
        </div>
    )
}

export default App;
