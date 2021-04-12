import React from 'react';

class Addbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      list: []

    };
    this.addItem = this.addItem.bind(this);
    this.removeItem = this.removeItem.bind(this);
  }


  addItem(e) {
    // Prevent button click from submitting form
    e.preventDefault(); 

    // Create variables for our list, the item to add, and our form
    let list = this.state.list;
    const newItem = document.getElementById("addInput");
    const form = document.getElementById("addItemForm");

    // If our input has a value
    if (newItem.value != "") {
      // Add the new item to the end of our list array
      list.push(newItem.value);
      this.props.parentCallback(list);
      // Then we use that to set the state for list
      this.setState({
        list: list
      });

      // Finally, we need to reset the form
      form.reset();
    }
  }

  removeItem(item) {
    // Put our list into an array
    console.log("deleting", item);
    const list = this.state.list.slice();
    // Check to see if item passed in matches item in array
    list.some((el, i) => {
      if (el === item) {
        // If item matches, remove it from array
        list.splice(i, 1);
        return true;
      }
    });
    this.props.parentCallback(list);
    // Set state to list
    this.setState({
      list: list
    });
    
  }

  render() {
    return (
      <div className="content">
        <div className="container">
          

          <section className="section">
            <form className="form" id="addItemForm">
              <input
                type="text"
                className="input"       
                id="addInput"
                placeholder="Add Ingredients"
              />
              <button className="button-is-info" onClick={this.addItem}>
                Add Item
              </button>
            </form>
          </section>

          <section className="section">
            <List items={this.state.list} delete={this.removeItem} />
          </section>

        </div>
      </div>
    );
  }
}

class List extends React.Component {
  constructor(props) {
    super(props);  
  }
  
  render()
   {
    return (

      <div>
          <ul>
            {this.props.items.map(item => (
              <li key={item}>
                
                <div className = "ingredient_box"
                  onClick={() => this.props.delete(item)}
                  >{item} &nbsp;</div>    
              </li>
            ))}
          </ul>
        </div>
    )
  }
}

export default Addbar;
