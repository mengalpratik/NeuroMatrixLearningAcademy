/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        dark: {
          950: '#07090b',
          900: '#0d1117',
          850: '#11161f',
          800: '#161b22',
          700: '#21262d',
          600: '#30363d',
          500: '#484f58',
          400: '#8b949e',
          300: '#c9d1d9',
          200: '#e6edf3',
          100: '#f0f6fc',
        },
        cyber: {
          green: '#10b981',
          greenHover: '#059669',
          greenLight: '#34d399',
          greenMuted: '#064e3b',
          cyan: '#06b6d4',
          amber: '#f59e0b',
          red: '#ef4444',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Menlo', 'monospace'],
      },
      boxShadow: {
        'cyber-sm': '0 0 10px rgba(16, 185, 129, 0.1)',
        'cyber-md': '0 0 20px rgba(16, 185, 129, 0.15)',
        'cyber-card': '0 4px 20px -2px rgba(0, 0, 0, 0.5)',
      }
    },
  },
  plugins: [],
}
