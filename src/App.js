import logo from "./logo.svg";
import "./App.css";
import "./index";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Available Sites</h1>

        <button type="button" class="button">
          <span class="button_t">GitHub </span>
          <span class="button_i">
            <ion-icon name="logo-github"></ion-icon>
          </span>
        </button>

        <button type="button" class="button" onclick="document.location='./pages/steam.html'">
          <span class="button_t">Steam </span>
          <span class="button_i">
          <ion-icon name="logo-steam"></ion-icon>
          </span>
        </button>
      </header>
    </div>
  );
}

export default App;
