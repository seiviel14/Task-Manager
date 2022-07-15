function List(props){
    function handleClick() {
        props.deletion(props.id)
    }

    function statusChange() {
        props.change(props.id)
    }

    return(
        <div className="task">
            <h1 >Task: {props.title}</h1>
            <p>Description: {props.content}</p>
            <label>Status<input onChange={statusChange} type="checkbox" checked={props.status}/></label>
            <br />
            <button onClick={handleClick}>Delete</button>
        </div>
    )
}
export default List;