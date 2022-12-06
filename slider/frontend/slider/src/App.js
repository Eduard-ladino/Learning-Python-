import logo from './logo.svg';
import './App.css';
import SliderContent  from './components/SliderContent.js'
import {useState, useEffect} from 'react';
import axios from 'axios';

function App() {  
  const [slider, setSlider] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/slider',{
    }).then((res) => {
      setSlider(res.data.slider); 
    }); 
  }, []);


  return ( 
    <>
      {slider.map((data, index) => {
        return <SliderContent title={data.title} id={data.id}/>
      })}
    </>
  );
}

export default App;
