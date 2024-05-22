import { useState } from "react"
import { useNavigate } from "react-router-dom"
import api from "../api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"


function Login() {
    const [email, SetEmail] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("")
    const navigate = useNavigate()
    
    const handleLogin = async (e) => {
        e.preventDefault()
        try {
            const response = await api.post("login", {email, password})
            if (response.status === 200) {
                const {access, refresh} = response.data
                localStorage.setItem("access", access)
                localStorage.setItem("refresh", refresh)
                // Fetch user information
                const userInfoResponse = await api.post("user", {
                    headers: {
                        Authorization: `Bearer ${access}`
                    }
                })
                const userInfo = userInfoResponse.data.role;
                
                if (userInfo === "coach"){
                    navigate("/coach-profile")
                }
                else {
                    navigate("/athlete-profile")
                }
            }else {
                setError("Failed to log in. Please try again.");
            }

        }catch (error) {
            if (error.response && error.response.status === 401){
                setError("Invalid Credentials.")
            }else {
                setError("Login error" + error.message)
            }
            console.log(error)
        }
    }

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleLogin} >
                <input 
                    type="email" 
                    value={email}
                    onChange={(e) => SetEmail(e.target.value)}
                    placeholder="email"
                    required
                />
                <input 
                    type="password" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
                <button type="submit">Login</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    )
}
export default Login