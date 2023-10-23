/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    fontSize: {
      '4xs': '0.125rem',
      '3xs': '0.25rem',
      '2.5xs': '0.375rem',
      '2xs': '0.5rem',
      '1.5xs': '0.625rem',
      'xs': '0.75rem',
      'sm': '0.875rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
      '2.5xl': '1.6875rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

