import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: "Kevin's Adventure Game",
  description: 'A modern web interface for the classic text adventure game',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-adventure-bg">
        {children}
      </body>
    </html>
  )
}

