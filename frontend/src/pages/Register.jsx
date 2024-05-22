import { useState } from "react"
import { useNavigate } from "react-router-dom"
import api from "../api"


function Register() {
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [password2, setPassword2] = useState("")
    const [role, setRole] = useState("athlete")
    const [error, setError] = useState("")
    const navigate = useNavigate()


    const handleRegister = async (e) => {
        e.preventDefault();

        if (password !== password2){
            setError("Password does not match");
            return;
        }

        try {
            const response = await api.post("register", {username, email, password, password2, role});
            if (response.status === 201) {
                navigate("/login")

            }else {
                setError('Failed to register. Please try again.');
              }
        }catch (error) {
            console.log("Registration error", error)
        }
    }


    return (
        <div>
            <h1>Register Here</h1>
            <form onSubmit={handleRegister}>

                <input 
                type="username" 
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
                /><br/>

                <input 
                type="email" 
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                required
                /><br/>

                <input 
                type="password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
                /><br/>

                <input 
                type="password" 
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}
                placeholder="Confirm password"
                required
                /><br/>
                
                <select value={role} onChange={(e) => setRole(e.target.value)} required>
                    <option value="coach">Coach</option>
                    <option value="athlete">Athlete</option>
                </select><br/>

                {error && <p>{error}</p>}
                <button type="submit">Register</button>
            </form>
        </div>
    )
}
export default Register