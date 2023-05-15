import { useState } from 'react';
import React from 'react';
import { createRoot } from 'react-dom/client';

import 'bootstrap/dist/css/bootstrap.min.css';

// ReactDOM.render(
//   <h1>teste</h1>,
//   document.getElementById('root')
// );

// Clear the existing HTML content
// document.body.innerHTML = '<div id="app"></div>';


const root = createRoot(document.getElementById('app'));
root.render(<h1>Hello, world</h1>);

// function NavigationBar() 
//   // TODO: Actually implement a navigation bar
//   return <h1 className="teste">Hello from React!</h1>;
// }

function FormControl() {
  return <input type="text" className="form-control" name="tese" ></input>;
}

function MyButton() {
  return (
    <button>I'm a button</button>
  );
}

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}


function FormToggle() {
  const [showForm, setShowForm] = useState(true);

  const toggleForm = () => setShowForm(!showForm);

  const handleSubmit = (event) => {
    event.preventDefault();
    // add your form submission logic here
  }

  return (
    <div>
      {showForm && (
        <form onSubmit={handleSubmit}>
          <input type="text" className="form-control" />
          <input type="text" className="form-control" />
          <input type="text" className="form-control" />
          <input type="text" className="form-control" />
          <input type="text" className="form-control" />
          <button type="submit">Submit</button>
        </form>
      )}

      <button onClick={toggleForm}>
        {showForm ? 'Hide Form' : 'Show Form'}
      </button>

    </div>
  );
}

const domNode = document.getElementById('navigation');
const root2 = createRoot(domNode);
root2.render(<FormToggle/>);