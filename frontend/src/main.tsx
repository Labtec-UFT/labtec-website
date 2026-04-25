import './index.css'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router-dom";

import {AuthProvider} from "./context/AuthContext.tsx";
// import ProtectedRoute from "./components/protection/ProtectedRoute.tsx";

import App from "./App.tsx";
import Contact from "./pages/Contact"
import Login from "./pages/management/auth/Login.tsx"
import Logout from "./pages/management/auth/Logout.tsx"
// import Dashboard from "./pages/management/Dashboard.tsx"
import NotFound from "./pages/NotFound.tsx";
import Project from "./pages/Project.tsx"

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <AuthProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/login" element={<Login />}/>
                    <Route path="/logout" element={<Logout />}/>
                    <Route path="/" element={<App />}/>
                    <Route path="/contact" element={<Contact />}/>
                    <Route path="*" element={<NotFound />} />
                    <Route path="/project/" element={<Project />}/>

                    {/*<Route path="/dashboard" element={*/}
                    {/*    <ProtectedRoute>*/}
                    {/*        <Dashboard />*/}
                    {/*    </ProtectedRoute>*/}
                    {/*} />*/}
                </Routes>
            </BrowserRouter>
        </AuthProvider>
    </StrictMode>
)