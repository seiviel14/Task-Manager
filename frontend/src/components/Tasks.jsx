import {useState, useEffect} from "react"
import axios from "axios"
import List from "./List"

function Task() {
    const [task, setNewTask] = useState(null)
    const [formTask, setFormTask] = useState({
        taskName: "",
        description: "",
    })

    useEffect(() => {
        getTasks()
    },
    [])

    function getTasks() {
        axios({
            method: "GET",
            url: "/task/",
        })
        .then((response) => {
            const data = response.data
            setNewTask(data)
        })
        .catch((error) => {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
        })
    }

    function createTask() {
        axios({
            method: "POST",
            url: "/task/",
            data:{
                taskName: formTask.taskName,
                description: formTask.description,
                status: formTask.status
            }
        })
        .then((response) => {
            getTasks()
        })

        setFormTask(({
            taskName: "",
            description: "",
        }))
        Event.preventDefault()
    }

    function deleteTask(id) {
        axios({
            method: "DELETE",
            url: `/task/${id}/`,
        })
        .then((response) => {
            getTasks()
        });
    }

    function changeStatus(id) {
        axios({
            method: "GET",
            url: `/task/${id}`,
        })
        .then((response) => {
            getTasks()
        })
    }

    function handleChange(event) {
        const {value, name} = event.target
        setFormTask(prevTask => ({
            ...prevTask, [name]: value
        }))
    }

    return (
        <div className="">
            <form className="create-task">
                <input onChange={handleChange} text={formTask.taskName} name="taskName" placeholder="" value={formTask.taskName} />
                <textarea onChange={handleChange} name="description" placeholder="" value={formTask.description} />
                <button onClick={createTask}>Create Task</button>
            </form>
                {
                    task && task.map(task => <List
                    key={task.id}
                    id={task.id}
                    title={task.taskName}
                    content={task.description}
                    status={task.status}
                    change={changeStatus}
                    deletion={deleteTask}
                    />
                )}
        </div>
    )
}

export default Task;