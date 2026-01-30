import {Link, Outlet} from "react-router-dom";

const navStyle = 'text-slate-600 hover:text-slate-900'

export function MainLayout() {
    return (
        <div className='min-h-screen flex flex-col'>
            {/*  Header */}
            <header className='bg-white border-b'>
                <div className='mx-auto max-w-7xl px-4 py-4 flex items-center justify-between'>
                    <Link to='/' className='text-xl font-bold text-brand'>RecommendAitions</Link>
                    <nav className='space-x-4'>
                        <Link to="/" className={navStyle}>Home</Link>
                        <Link to="/about" className={navStyle}>About</Link>
                        <Link to="/contact" className={navStyle}>Contact</Link>
                        <Link to="/recommend" className={navStyle}>Recommend</Link>
                        <Link to="/login" className='btn btn-primary'>Login</Link>
                    </nav>
                </div>
            </header>

            {/* Main */}
            <main className='flex-1 mx-auto w-full max-w-7xl px-4 py-8'>
                <Outlet/>
            </main>

            {/* Footer */}
            <footer className='bg-white border-t'>
                <div className='mx-auto max-w-7xl px-4 py-4 text-sm text-slate-500'>
                    &copy; {new Date().getFullYear()} RecommendAitions
                </div>
            </footer>
        </div>
    )
}