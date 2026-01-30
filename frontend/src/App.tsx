import './App.css'
import {Route, Routes} from "react-router-dom";
import Home from "./pages/Home.tsx";
import Login from "./pages/Login.tsx";
import MovieDetail from "./pages/MovieDetail.tsx";
import {MainLayout} from "./layout/MainLayout.tsx";
import ProtectedRoute from "./components/ProtectedRoute.tsx";
import NotFound from "./pages/NotFound.tsx";

function App() {
  return (
      <Routes>
          <Route element={<MainLayout />}>
              <Route path="/" element={<Home />} />
              <Route path="/movie/:id" element={<MovieDetail />} />
          </Route>

          <Route element={<ProtectedRoute />}>
              <Route path="/movie2/:id" element={<MovieDetail />} />
          </Route>

          <Route path="/login" element={<Login />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
  )
}

export default App
