import React from 'react'

const SideBar = () => {
  return (
    <aside className="w-72 bg-slate-900 text-white p-5">

            <h2 className="text-xl font-bold mb-6">

                📚 Documents

            </h2>

            <button
                className="w-full rounded-lg bg-blue-600 py-2 hover:bg-blue-700"
            >

                Upload PDF

            </button>

            <div className="mt-8">

                No documents uploaded

            </div>

        </aside>
  )
}

export default SideBar
