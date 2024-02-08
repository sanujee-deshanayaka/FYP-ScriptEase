"use client"
import Image from 'next/image'
import React, { useState } from 'react';

import CoverBG from '../assets/image/bdcover.jpg'
import Logo from '../assets/image/icon.png'
import uploadFile from '@/services/fileUploadService';

export default function Home() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadedFile, setUploadedFile] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [modalText, setModalText] = useState(null);
  const [downloadText, setDownloadText] = useState(null);
  const [loading, setLoading] = useState(null);
  const [downloadFile, setDownloadFile]=useState(null)

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (selectedFile) {
      setLoading(true);
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const uploadedFile = await uploadFile(formData);
        setDownloadFile(uploadedFile)
        console.log("File uploaded successfully:", uploadedFile);
        setModalText("File Upload Successfully")
        setDownloadText("Download Now")
        setShowModal(true);
      } catch (error) {
        setModalText("Error uploading file")
        setShowModal(true);
        console.error("Error uploading file:", error);
      }
      finally {
        setSelectedFile(null);
        setLoading(false);
      }
    } else {
      setModalText("Please select a file before uploading.")
      setShowModal(true);
    }
  }
  
  const closeModal = () => {
    setSelectedFile(null);
    setShowModal(false);
  };

  return (
    <div class="flex h-screen">
      <div class="w-2/3 md:w-1/2 lg:w-2/3 h-full">
        <Image src={CoverBG} alt='' quality={100} class="h-full object-cover"
        />
      </div>

      <div class="w-1/3 md:w-1/2 lg:w-1/3 h-full bg-zinc-800 sm:w-4/4">
        <div class="justify-content items-center">
          <Image src={Logo} width={300} height={54} class='mx-auto mt-10 ' />
          <p className='text-center my-5 text-light-500 text-xl font-black font-console tracking-widest'>SCRIPTEASE</p>
          <p class="mx-5 text-center text-light-500 ">
            Pariatur velit nisi enim non labore consequat exercitation do minim dolore nostrud aliquip. Laboris cupidatat tempor cillum nulla velit occaecat occaecat.
          </p>
        </div>
        <div class="mx-5 my-5">
          <form onSubmit={handleSubmit}>
            <div class="flex items-center justify-center w-full">
              <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-56 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-zinc-800 dark:hover:bg-zinc-600 dark:bg-zinc-800 hover:bg-zinc-800 dark:border-zinc-600 dark:hover:border-zinc-500 dark:hover:bg-zinc-600">
                <div class="flex flex-col items-center justify-center pt-3 pb-4">
                  <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                  </svg>
                  <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                    <span className="font-semibold">
                      {selectedFile ? `Selected file: ${selectedFile.name}` : 'Click to upload or drag and drop'}
                    </span>
                  </p>
                  <p class="text-xs text-gray-500 dark:text-gray-400">Only Allowed .json File</p>
                </div>
                <input id="dropzone-file" type="file" class="hidden" onChange={handleFileChange} accept=".json" />
              </label>
            </div>
            <div>
              <button type="submit" class="flex w-full justify-center rounded-md bg-zinc-600 my-3 px-3 py-3 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-gray-600 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:bg-amber-400">
                {loading ? (
                  <div role="status">
                    <svg aria-hidden="true" class="inline w-4 h-4 text-gray-200 animate-spin dark:text-gray-600 fill-gray-600 dark:fill-gray-300" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor" />
                      <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill" />
                    </svg>
                    <span class="sr-only">Loading...</span>
                  </div>) : "Upload"}
              </button>
            </div>
          </form>
        </div>
      </div>
      {showModal && (
        <div id="popup-modal" tabIndex="-1" className="fixed top-0 right-0 left-0 bottom-0 z-50 flex items-center justify-center bg-gray-700 bg-opacity-50">
          <div className="w-full max-w-md mx-auto rounded-lg p-4 bg-gray-700">
            <button
              type="button"
              className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
              onClick={closeModal}
            >
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
            <div className="text-center">
              <svg
                className="mx-auto mb-4 text-gray-400 w-12 h-12"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 20"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
                />
              </svg>
              <h3 className="mb-5 text-lg font-normal text-light">
                {modalText}
              </h3>
              {/* Display additional information about the uploaded file if needed */}
              {/* Example: <p>{uploadedFile.name}</p> */}
              {downloadText && (
                <button
                  type="button"
                  className="text-white bg-yellow-600 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 mx-2"
                  // onClick={handleDownload}
                  
                >
                  Download Script
                </button>
              )}
              <button
                type="button"
                onClick={closeModal}
                className="text-white bg-gray-600 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>

  )
}
