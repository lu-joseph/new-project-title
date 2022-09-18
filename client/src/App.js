import './App.css';
import { BrowserRouter} from "react-router-dom";
import MyRouters from './MyRouters';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <MyRouters/>
      </BrowserRouter>
    </div>
  );
}

export default App;
