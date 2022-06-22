import './App.css';
import Nav from './components/Sidebar';
import Rsidebar from './components/Rsidebar';
import Feeds from './components/Feeds';

function App() {
  return (
    <div className="App">

      <div class="navcontainer">
        <Nav />
        <Feeds />
        <Rsidebar />
      </div>


    </div>
  );
}

export default App;
